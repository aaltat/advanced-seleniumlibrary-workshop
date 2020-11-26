import argparse
import os
import shutil
import subprocess
import tempfile
import time

import requests

OUTPUT_DIR = './output'
TEST_DIR = './3-parallel-execution'


def run_tests(grid: bool, pabot: bool):
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
    os.mkdir(OUTPUT_DIR)
    if grid:
        hub, node = start_grid()
    command = ['python', '-m']
    if pabot:
        command.extend(['pabot.pabot', '--verbose', '--processes', '2'])
    else:
        command.extend(['robot.run'])
    command.extend(['--outputdir', 'output', '--loglevel', 'debug'])
    if grid:
        command.append('--variable')
        command.append('REMOTE_URL:http://localhost:4444/wd/hub')
    command.append(TEST_DIR)
    rc = subprocess.run(command, shell=True)
    print(rc.returncode)
    if grid:
        print('Stop gird.')
        hub.kill()
        node.kill()


def start_grid():
    node_file = tempfile.TemporaryFile()
    hub_file = tempfile.TemporaryFile()
    for file in os.listdir(TEST_DIR):
        if file.startswith('selenium-server-standalone'):
            selenium_jar = os.path.join(TEST_DIR, file)
            break
    else:
        raise ValueError(f'Selenium server jar not found in {TEST_DIR}')
    hub = subprocess.Popen(['java', '-jar', selenium_jar, '-role', 'hub', '-host', 'localhost'],
                           stderr=subprocess.STDOUT, stdout=hub_file)
    time.sleep(2)  # It takes about two seconds to start the hub.
    ready = _grid_status(False, 'hub')
    if not ready:
        hub.kill()
        raise ValueError('Selenium grid hub was not ready in 60 seconds.')
    node = subprocess.Popen(['java', '-jar', selenium_jar, '-role', 'node'],
                            stderr=subprocess.STDOUT, stdout=node_file)
    ready = _grid_status(True, 'node')
    if not ready:
        hub.kill()
        node.kill()
        raise ValueError('Selenium grid node was not ready in 60 seconds.')
    return hub, node


def _grid_status(status=False, role='hub'):
    count = 0
    while True:
        try:
            response = requests.get('http://localhost:4444/wd/hub/status')
            data = response.json()
            if data['value']['ready'] == status:
                print('Selenium grid %s ready/started.' % role)
                return True
        except Exception:
            pass
        count += 1
        if count == 12:
            raise ValueError(f'Selenium grid {role} not ready/started in 60 seconds.')
        print('Selenium grid %s not ready/started.' % role)
        time.sleep(5)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--grid', dest='grid', action='store_true', default=False)
    parser.add_argument('--pabot', dest='pabot', action='store_true', default=False)
    cmd_args = parser.parse_args()
    run_tests(cmd_args.grid, cmd_args.pabot)
