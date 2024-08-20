def run_commands(inf, outf):
    infbin=outf.replace(".txt",".in.bin")
    outfbin=outf.replace(".txt",".out.bin")
    commands = []
    commands.append(['python3', ['PythonEncoder.py', inf, infbin]])
    commands.append(['scala', ['-cp','.:/usr/share/java/protobuf.jar','PuzzleSolver', infbin, outfbin]])
    commands.append(['python3', ['PythonDecoder.py', outfbin, outf]])
#    commands.append(['ls', ['-lisa']])
    return commands