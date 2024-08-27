def run_commands(inf, outf):
    commands = []
    commands.append(['scala', ['solver.jar', inf, outf]])
#    commands.append(['ls', ['-lisa']])
    return commands