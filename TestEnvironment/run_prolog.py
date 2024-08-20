from os.path import exists

def run_commands(inf, outf):
    commands = []
    if exists('./PuzzleSolver.pl'):
        print ('--> using PuzzleSolver.pl')
        commands.append(['swipl', ['PuzzleSolver.pl', '--io', inf, outf]])
    else:
        print ('--> using PuzzleSolver.pro')
        commands.append(['swipl', ['PuzzleSolver.pro', '--io', inf, outf]])
#    commands.append(['ls', ['-lisa']])
    return commands