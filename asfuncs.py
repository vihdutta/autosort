import os
import shutil
from datetime import datetime
from random import randint


def filesnumrenamer(dstname, srcfiles, dstfiles, idfilelist):
    filesidrenamer(dstname, srcfiles, dstfiles)
    files = os.listdir(dstname)
    for i, file in enumerate(files):
        name, extension = os.path.splitext(file) #error #1
        name = name.split('---', 1)[0]
        idfilelist.append(name + '---')
        fileamount = idfilelist.count(name + '---') - 1
        if fileamount > 0:
            iparentheses = '(' + str(fileamount) + ')'
        else:
            iparentheses = ''
        filerename = ''.join([name, iparentheses, extension])
        os.rename(os.path.join(dstname, file), os.path.join(dstname, filerename))


def filesidrenamer(dstname, srcfiles, dstfiles):
    for root, dirs, files in os.walk(dstname):
        for file in os.listdir(dstname):
            num = createid(srcfiles, dstfiles)
            if '(' in file:
                try:
                    fileider = file.split('(')[0] + num + file.split('(')[1]
                except IndexError:
                    fileider = file + num 
            else:
                try:
                    fileider = file.split('.')[0] + num + '.' + file.split('.')[1]
                except IndexError:
                    fileider = file + num
            os.rename(os.path.join(dstname, file), os.path.join(dstname, fileider))


def dstsort(dstname):
    foldername = f'autosort {datetime.now().strftime("%H-%M-%S-%f")}'
    os.mkdir(os.path.join(dstname, foldername))
    files = [f for f in os.listdir(dstname) if os.path.isfile(os.path.join(dstname, f))]
    
    for file in files:
        name, extension = os.path.splitext(file)
        newpath = os.path.join(dstname, foldername, extension)
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        shutil.move(os.path.join(dstname, file), os.path.join(dstname, foldername, extension, name+extension))


def createid(srcfiles, dstfiles):
    i1 = len(srcfiles) + len(dstfiles)
    i2 = int(str(i1) + '0')
    return '---' + str(randint(i1, i2))
