def run_commands(inf, outf):
    commands = []
    commands.append(['scala', ['PuzzleSolver.scala', inf, outf]])
#    commands.append(['ls', ['-lisa']])
    return commands