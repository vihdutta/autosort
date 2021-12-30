from os import walk
from shutil import copy, copy2
from pathlib import Path
from asfuncs import (total_filecount, duplicate_tagger, folder_create, 
sortdirs, RICH_TEXTFORE_NL, RICH_TEXTFORE, PLAIN_TEXTFORE, TEXTBACK)
from time import perf_counter

# copies from srcdirs to dstdir + creates filenumber for files
def copy_from_dirs(srcdirs, dstdir, fcmethod, sort, metadata, replace):
    start_time = perf_counter()
    folder = ""
    filecount, filecount_temp = total_filecount(srcdirs)
    yield f'{RICH_TEXTFORE}Discovered {filecount} files in directory(s): {", ".join(srcdirs)}{TEXTBACK}'

    if fcmethod == "Single-folder creation":
        folder = folder_create(dstdir)
    for srcdir in srcdirs: # for each source directory
        yield f'{RICH_TEXTFORE_NL}In directory {srcdir}{TEXTBACK}'
        if fcmethod == "Multi-folder creation":
            folder = folder_create(dstdir)
        for root, _, files in walk(srcdir): # get data for source directory
            for file in files: # iterate through each file
                yield f'{PLAIN_TEXTFORE}Copying "{file}"... {filecount} of {filecount_temp} remain.{TEXTBACK}'
                filecount_temp -= 1
                filecount_id = 0
                src_filepath = Path(root) / file
                name, extension = src_filepath.stem, src_filepath.suffix

                if replace:
                    new_filename = file
                else:
                    new_filename = duplicate_tagger(file, filecount_id, dstdir, folder, name, extension)
                old_path = Path(root) / file
                new_path = Path(dstdir) / folder / new_filename

                if metadata:
                    copy2(old_path, new_path)
                else:
                    copy(old_path, new_path)
        if sort:
            yield f'{RICH_TEXTFORE}Sorting files...{TEXTBACK}'
            sortdirs(dstdir, folder)
    
    end_time = perf_counter()
    yield f'{RICH_TEXTFORE}Finished in {start_time-end_time} seconds.{TEXTBACK}'
