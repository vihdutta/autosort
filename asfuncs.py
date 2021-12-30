from datetime import datetime
from pathlib import Path, PurePath
from shutil import move

# styling
RICH_TEXTFORE_NL = '<span style=\' font-family:"Segoe UI Light"; font-size:18pt; font-weight:400; color:#a89769;\' ><br>'
RICH_TEXTFORE = '<span style=\' font-family:"Segoe UI Light"; font-size:18pt; font-weight:400; color:#a89769;\' >'
PLAIN_TEXTFORE = '<span style=\' font-family:"Segoe UI Light"; font-size:18pt; font-weight:400; color:#ffffff;\' >'
TEXTBACK = '</span>'

# add number file for the directory
def duplicate_tagger(file, filecount_id, dstdir, folder, name, extension):
    dst_filepath = Path(dstdir) / folder / file
    if dst_filepath.is_file():
        filecount_id += 1
        return duplicate_tagger(f"{name}({filecount_id}){extension}", filecount_id, dstdir, folder, name, extension)
    else:
        if filecount_id == 0:
            return f"{name}{extension}"
        else:
            return f"{name}({filecount_id}){extension}"


# gets filecount for src and destination directories
def total_filecount(srcdirs):
    filecount = 0
    for srcdir in srcdirs:
        for path in Path(srcdir).rglob("*"):
            if path.is_file():
                filecount += 1
    return filecount, filecount


# sorts files in directory
def sortdirs(dstdir, folder):
    path = Path(dstdir) / folder
    for filepath in path.iterdir():
        if filepath.is_file():
            name, extension = PurePath(filepath).stem, PurePath(filepath).suffix
            new_dir = Path(dstdir) / folder / extension
            if not Path(new_dir).exists():
                Path(new_dir).mkdir()
            filename = name + extension
            old_path = Path(dstdir) / folder / filepath
            new_path = Path(dstdir) / folder / extension / filename
            move(old_path, new_path)


# creates folder
def folder_create(dstdir):
    folder_name = f'autosort {datetime.now().strftime("%H-%M-%S-%f")}'
    Path(PurePath(dstdir, folder_name).joinpath()).mkdir()
    return folder_name