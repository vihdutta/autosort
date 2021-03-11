import os
import shutil
import time
from PyQt5.QtWidgets import QFileDialog
from tkinter import Tk, filedialog
from asfuncs import numgenerator, dstsort, filesnumrenamer, filesidrenamer

ignoredirs = ('$RECYCLE.BIN', 'System Volume Information')
metadata = False
srcnames = []
dstname = []
srcfilesfound = []
dstfilesfound = []
renamerfilelist = []
filelist = []

# base of the copyfromallusbs() function
def copyfromdirs(metadata, replace, sortmethod, dstname):
    filelist.clear()

    for srcname in srcnames:
        for root, dirs, files in os.walk(srcname):
            dirs[:] = [d for d in dirs if d not in ignoredirs]
            for file in files:
                filelist.append(file)
    filelistlen1 = len(filelist)
    filelistlen2 = len(filelist)

    for root, dirs, files in os.walk(dstname):
        for file in files:
            dstfilesfound.append(file)
    
    for srcname in srcnames:
        for root, dirs, files in os.walk(srcname):
            dirs[:] = [d for d in dirs if d not in ignoredirs]
            for file in files:
                srcfilesfound.append(file)
            for file in files:
                if not replace:
                    num = numgenerator(srcfilesfound, dstfilesfound)
                    try:
                        srcrename = file.split('.')[0] + num + '.' + file.split('.')[1]
                    except IndexError:
                        srcrename = file + num
                else:
                    srcrename = file
                if metadata:
                    shutil.copy2(os.path.join(root, file), os.path.join(dstname, srcrename))
                else:
                    shutil.copy(os.path.join(root, file), os.path.join(dstname, srcrename))
                dstfilesfound.append(srcrename)
                filelistlen1 -= 1
                yield f'Copied {file}. {filelistlen1} of {filelistlen2} files remaining.'
        if sortmethod == 2:
            if not replace:
                filesnumrenamer(dstname, srcfilesfound, dstfilesfound, renamerfilelist)
            dstsort(dstname)
    if sortmethod == 1:
        if not replace:
            filesnumrenamer(dstname, srcfilesfound, dstfilesfound, renamerfilelist)
        dstsort(dstname)
    elif sortmethod == 0:
        if not replace:
            filesnumrenamer(dstname, srcfilesfound, dstfilesfound, renamerfilelist)

    renamerfilelist.clear()
    

'''testing items'''
# tic = time.perf_counter()
# toc = time.perf_counter()
# with open('filenamehere.txt', 'a') as f:
#    f.write(f'File copied in {toc - tic:0.4f} seconds\n')