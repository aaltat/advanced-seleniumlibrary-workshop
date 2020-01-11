import argparse
import os
import shutil
import sys
from pathlib import Path

from robot.run import run_cli

shutil.rmtree('./output', ignore_errors=True)
test_dir = '6-page-object'

parser = argparse.ArgumentParser()
parser.add_argument('--include', '-i')
cmd_args = parser.parse_args()
include = cmd_args.include

robot_args = ['--outputdir', 'output',
              '--loglevel', 'debug',
              test_dir]
if include:
        robot_args.insert(0, '--include')
        robot_args.insert(1, include)
src = Path(os.path.dirname(os.path.realpath(__file__))) / test_dir / 'src'
sys.path.append(str(src))
run_cli(robot_args)
