def run_commands(inf, outf):
    commands = []
    commands.append(['scala', ['run', 'PuzzleSolver', inf, outf]])
#    commands.append(['ls', ['-lisa']])
    return commands