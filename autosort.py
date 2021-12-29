import os
import shutil
from pathlib import Path, PurePath
from datetime import datetime
from asfuncs import (createid, dstsort, filesnumrenamer, 
RICH_TEXT_FORE_NL, RICH_TEXT_FORE, PLAIN_TEXT_FORE, TEXTBACK)

IGNORE_DIRS = ('$RECYCLE.BIN', 'System Volume Information')

metadata = False
srcdirs = []
srcfiles = []
dstfiles = []
id_filelist = []

# base of the copyfromallusbs() function
def copyfromdirs(metadata, replace, fcmethod, sort, dstname):
    all_srcfiles_len = 0

    if fcmethod == 'Single-folder creation':
        folder_name = f'autosort {datetime.now().strftime("%H-%M-%S-%f")}'
        Path(PurePath(dstname, folder_name).joinpath()).mkdir()

    for srcdir in srcdirs:
        for root, dirs, files in os.walk(srcdir):
            dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
            for file in files:
                all_srcfiles_len += 1
    
    yield f'{RICH_TEXT_FORE}Discovered {all_srcfiles_len} files in directory(s): {", ".join(srcdirs)}{TEXTBACK}'
    temp_all_srcfiles_len = all_srcfiles_len

    for root, dirs, files in os.walk(dstname):
        for file in files:
            dstfiles.append(file)
    
    for srcdir in srcdirs:
        if fcmethod == 'Multi-folder creation':
            folder_name = f'autosort {datetime.now().strftime("%H-%M-%S-%f")}'
            Path(PurePath(dstname, folder_name).joinpath()).mkdir()

        if 'folder_name' in locals():
            truepath = PurePath(dstname, folder_name).joinpath()
        else:
            truepath = dstname

        yield f'{RICH_TEXT_FORE_NL}In directory {srcdir}{TEXTBACK}'

        for root, dirs, files in os.walk(srcdir):
            dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
            for file in files:
                srcfiles.append(file)

            for file in files:
                if not replace:
                    try:
                        file_ider = file.split('.')[0] + createid(srcfiles, dstfiles) + '.' + file.split('.')[1]
                    except IndexError:
                        file_ider = file + createid(srcfiles, dstfiles)
                else:
                    file_ider = file

                yield f'{PLAIN_TEXT_FORE}Copying "{file}"... {temp_all_srcfiles_len} of {all_srcfiles_len} remain.{TEXTBACK}'
                temp_all_srcfiles_len -= 1
                
                if metadata:
                    shutil.copy2(PurePath(root, file).joinpath(), PurePath(truepath, file_ider).joinpath())
                else:
                    shutil.copy(PurePath(root, file).joinpath(), PurePath(truepath, file_ider).joinpath())
                dstfiles.append(file_ider)

        if fcmethod == 'Multi-folder creation':
            if not replace:
                yield f'{RICH_TEXT_FORE_NL}Enumerating...{TEXTBACK}'
                filesnumrenamer(dstname, srcfiles, dstfiles, truepath, id_filelist)
            if sort:
                dstsort(dstname, truepath)
            yield f'{RICH_TEXT_FORE}Finished{TEXTBACK}'
            id_filelist.clear()

    if fcmethod == 'Single-folder creation':
        if not replace:
            yield f'{RICH_TEXT_FORE_NL}Enumerating...{TEXTBACK}'
            filesnumrenamer(dstname, srcfiles, dstfiles, truepath, id_filelist)
        if sort:
            dstsort(dstname, truepath)
        yield f'{RICH_TEXT_FORE}Finished{TEXTBACK}'

    elif fcmethod == 'No folder creation':
        if not replace:
            yield f'{RICH_TEXT_FORE_NL}Enumerating...{TEXTBACK}'
            filesnumrenamer(dstname, srcfiles, dstfiles, truepath, id_filelist)
        if sort:
            dstsort(dstname, truepath)
        yield f'{RICH_TEXT_FORE}Finished{TEXTBACK}'

    id_filelist.clear()
    

'''testing items'''
# tic = time.perf_counter()
# toc = time.perf_counter()
# with open('testing/filenamehere.txt', 'a') as f:
#    f.write(f'File copied in {toc - tic:0.4f} seconds\n')