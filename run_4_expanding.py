import argparse
import shutil

from robot.run import run_cli

shutil.rmtree('./output', ignore_errors=True)

parser = argparse.ArgumentParser()
parser.add_argument('--include', '-i')
cmd_args = parser.parse_args()
include = cmd_args.include

robot_args = ['--outputdir', 'output',
              '--loglevel', 'debug',
              './4-expanding']
if include:
        robot_args.insert(0, '--include')
        robot_args.insert(1, include)
run_cli(robot_args)
