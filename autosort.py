import os
import shutil
from PyQt5.QtWidgets import QFileDialog
from asfuncs import createid, dstsort, filesnumrenamer, filesidrenamer
import time

ignoredirs = ('$RECYCLE.BIN', 'System Volume Information')
metadata = False

srcdirs = []
srcfiles = []
dstfiles = []
idfilelist = []
allsrcfileslen = 0

# base of the copyfromallusbs() function
def copyfromdirs(metadata, replace, sortmethod, dstname):
    allsrcfileslen = 0

    for srcdir in srcdirs:
        for root, dirs, files in os.walk(srcdir):
            dirs[:] = [d for d in dirs if d not in ignoredirs]
            for file in files:
                allsrcfileslen += 1 #allsrcfiles only used for the number of files, make += 1?
    tempallsrcfileslen = allsrcfileslen

    for root, dirs, files in os.walk(dstname):
        for file in files:
            dstfiles.append(file)
    
    for srcdir in srcdirs:
        for root, dirs, files in os.walk(srcdir):
            yield f'In directory {root}'
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
                if metadata:
                    shutil.copy2(os.path.join(root, file), os.path.join(dstname, fileider))
                else:
                    shutil.copy(os.path.join(root, file), os.path.join(dstname, fileider))
                dstfiles.append(fileider)
                tempallsrcfileslen -= 1
                yield f'Copied "{file}" - {tempallsrcfileslen} of {allsrcfileslen} remain.'
        if sortmethod == 2:
            if not replace:
                filesnumrenamer(dstname, srcfiles, dstfiles, idfilelist)
            dstsort(dstname)
    if sortmethod == 1:
        if not replace:
            filesnumrenamer(dstname, srcfiles, dstfiles, idfilelist)
        dstsort(dstname)
    elif sortmethod == 0:
        if not replace:
            filesnumrenamer(dstname, srcfiles, dstfiles, idfilelist)

    idfilelist.clear()
    

'''testing items'''
# tic = time.perf_counter()
# toc = time.perf_counter()
# with open('testing/filenamehere.txt', 'a') as f:
#    f.write(f'File copied in {toc - tic:0.4f} seconds\n')