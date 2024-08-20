
import shutil


from pathlib import Path

def walk(path): 
    for p in Path(path).iterdir(): 
        if p.is_dir(): 
            yield from walk(p)
            continue
        yield p.resolve()


# the function returns a generator so if you need a list you need to build one
all_files = list(walk(Path('.'))) 

for file in all_files:
    if not str(file).endswith(".png") and not str(file).endswith(".txt") and not ":" in str(file):
        continue
    filename = file.stem.split(":")

    print(filename)
    if len(filename) != 2:
        continue
    filename = filename[0] + file.suffix
    new_path = file.parent.absolute().joinpath(filename)
    print(new_path)
    file.rename(new_path)
