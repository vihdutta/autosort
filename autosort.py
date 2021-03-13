import os
import shutil
from datetime import datetime
from asfuncs import (createid, dstsort, filesnumrenamer, filesidrenamer, 
richtextforenl, richtextfore, plaintextfore, textback)

ignoredirs = ('$RECYCLE.BIN', 'System Volume Information')

metadata = False
srcdirs = []
srcfiles = []
dstfiles = []
idfilelist = []

# base of the copyfromallusbs() function
def copyfromdirs(metadata, replace, sortmethod, dstname):
    allsrcfileslen = 0

    for srcdir in srcdirs:
        for root, dirs, files in os.walk(srcdir):
            dirs[:] = [d for d in dirs if d not in ignoredirs]
            for file in files:
                allsrcfileslen += 1
    
    yield f'{richtextfore}Discovered {allsrcfileslen} files in directory(s): {", ".join(srcdirs)}{textback}'
    tempallsrcfileslen = allsrcfileslen

    for root, dirs, files in os.walk(dstname):
        for file in files:
            dstfiles.append(file)
    
    for srcdir in srcdirs:
        yield f'{richtextforenl}In directory {srcdir}{textback}'

        for root, dirs, files in os.walk(srcdir):
            dirs[:] = [d for d in dirs if d not in ignoredirs]
            for file in files:
                srcfiles.append(file)

            for file in files:
                if not replace:
                    try:
                        fileider = file.split('.')[0] + createid(srcfiles, dstfiles) + '.' + file.split('.')[1]
                    except IndexError:
                        fileider = file + createid(srcfiles, dstfiles)
                else:
                    fileider = file

                yield f'{plaintextfore}Copying "{file}"... {tempallsrcfileslen} of {allsrcfileslen} remain.{textback}'
                tempallsrcfileslen -= 1

                if metadata:
                    shutil.copy2(os.path.join(root, file), os.path.join(dstname, fileider))
                else:
                    shutil.copy(os.path.join(root, file), os.path.join(dstname, fileider))
                dstfiles.append(fileider)

        if sortmethod == 2:
            if not replace:
                yield f'{richtextforenl}Enumerating...{textback}'
                filesnumrenamer(dstname, srcfiles, dstfiles, idfilelist)
            dstsort(dstname)
            yield f'{richtextfore}Finished{textback}'

    if sortmethod == 1:
        if not replace:
            yield f'{richtextforenl}Enumerating...{textback}'
            filesnumrenamer(dstname, srcfiles, dstfiles, idfilelist)
        dstsort(dstname)
        yield f'{richtextfore}Finished{textback}'

    elif sortmethod == 0:
        if not replace:
            yield f'{richtextforenl}Enumerating...{textback}'
            filesnumrenamer(dstname, srcfiles, dstfiles, idfilelist)
        yield f'{richtextfore}Finished{textback}'

    idfilelist.clear()
    

'''testing items'''
# tic = time.perf_counter()
# toc = time.perf_counter()
# with open('testing/filenamehere.txt', 'a') as f:
#    f.write(f'File copied in {toc - tic:0.4f} seconds\n')