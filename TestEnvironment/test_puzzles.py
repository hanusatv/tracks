import os
import time
import pytest
from pexpect import *
from run import run_commands

def read_puzzle(path):
    """ read and format the puzzle. In this case the puzzle is stripped"""
    with open(path, 'r') as puzzle_file:
        lines = (line.rstrip() for line in puzzle_file.readlines())
        data = ' '.join(l for l in lines if l) # skip blank lines
    return data

@pytest.mark.parametrize("file_name", sorted(os.listdir('/data/ikt212/puzzles')))
def test_single_puzzle(file_name,request):
    print('\n' + '-'*120)

    full_name = str(request.node.name)
    full_name = full_name[full_name.find('[') + 1:full_name.rfind('-')]
    full_name = full_name.replace('.txt', '').replace('/', '-') + '.txt'

    puz_file = os.path.join('/data/ikt212/puzzles', file_name)
    ans_file = os.path.join('/data/ikt212/answers', full_name)
    sol_file = os.path.join('/data/ikt212/solutions', file_name)

    commands = run_commands(puz_file, ans_file) # get the commands for the test runs
    
    try:
        for command in commands:
            print ('########## executing ',end='')
            print(command)
            child = spawn(command[0], args=command[1], timeout=300, encoding='utf-8') # wait 300 sec = 5 min
            assert child.expect([TIMEOUT, EOF]) == 1, 'Program failed to execute in the allotted time!'
            print (child.before,end='')
            child.terminate(force=True)
    except Exception as e:
        print(e)

    print('-'*120)

    assert read_puzzle(ans_file) == read_puzzle(sol_file), 'Output doesn\'t match solution.'