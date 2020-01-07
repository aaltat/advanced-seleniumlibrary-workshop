import argparse
import shutil

from robot.run import run_cli

shutil.rmtree('./output')

parser = argparse.ArgumentParser()
parser.add_argument('--include', '-i')
cmd_args = parser.parse_args()
include = cmd_args.include

robot_args = ['--outputdir', 'output',
              '--loglevel', 'debug',
              './2-debugging']
if include:
        robot_args.insert(0, '--include')
        robot_args.insert(1, include)
run_cli(robot_args)
