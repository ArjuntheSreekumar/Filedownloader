from os import scandir

source_dir = "C:\\Users\\arjun\\Downloads"
with scandir(source_dir) as entries:
    for entry in entries:
        print(entry.name)
