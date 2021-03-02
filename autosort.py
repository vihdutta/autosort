import os
import shutil
from tkinter import Tk, filedialog
from asfuncs import numgenerator, dstsort, filesnumrenamer, filesidrenamer

ignoredirs = ('$RECYCLE.BIN', 'System Volume Information')
metadata = False
srcnames = []
srcfilesfound = []
dstfilesfound = []
filelist = []

# open file dialog box to choose folder
root = Tk()
root.withdraw()
getsrc = filedialog.askdirectory(title='source')
srcnames.append(getsrc)
getsrc2 = filedialog.askdirectory(title='source')
srcnames.append(getsrc2)
dstname = filedialog.askdirectory(title='destination')

# base of the copyfromallusbs() function
def copyfromusb(metadata, replace, sortmethod):
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

        if sortmethod == 1:
            if not replace:
                filesnumrenamer(dstname, srcfilesfound, dstfilesfound, filelist)
            dstsort(dstname)
            filelist.clear()

    if sortmethod == 2:
        if not replace:
            filesnumrenamer(dstname, srcfilesfound, dstfilesfound, filelist)
        dstsort(dstname)
        filelist.clear()

    elif sortmethod == 0:
        if not replace:
            filesnumrenamer(dstname, srcfilesfound, dstfilesfound, filelist)


copyfromusb(metadata=True, replace=False, sortmethod=2)


'''testing items'''
# tic = time.perf_counter()
# toc = time.perf_counter()
# with open('filenamehere.txt', 'a') as f:
#    f.write(f'File copied in {toc - tic:0.4f} seconds\n')