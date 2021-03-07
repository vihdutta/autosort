import os
import shutil
from datetime import datetime
from random import randint


def filesnumrenamer(dstname, srcfilesfound, dstfilesfound, renamerfilelist):
    filesidrenamer(dstname, srcfilesfound, dstfilesfound)
    files = os.listdir(dstname)
    for i, file in enumerate(files):
        name, extension = os.path.splitext(file) #error #1
        name = name.split('---', 1)[0]
        renamerfilelist.append(name + '---')
        fileamount = renamerfilelist.count(name + '---') - 1
        if fileamount > 0:
            iparentheses = '(' + str(fileamount) + ')'
        else:
            iparentheses = ''
        filerename = ''.join([name, iparentheses, extension])
        os.rename(os.path.join(dstname, file), os.path.join(dstname, filerename))


def filesidrenamer(dstname, srcfilesfound, dstfilesfound):
    for root, dirs, files in os.walk(dstname):
        for file in os.listdir(dstname):
            num = numgenerator(srcfilesfound, dstfilesfound)
            if '(' in file:
                try:
                    srcrename = file.split('(')[0] + num + file.split('(')[1]
                except IndexError:
                    srcrename = file + num 
            else:
                try:
                    srcrename = file.split('.')[0] + num + '.' + file.split('.')[1]
                except IndexError:
                    srcrename = file + num
            os.rename(os.path.join(dstname, file), os.path.join(dstname, srcrename))


def dstsort(dstname):
    timenow = datetime.now().strftime('%H-%M-%S-%f')#[:-2]
    foldername = f'autosort {timenow}'
    makenewfolder = os.mkdir(f'{dstname}/{foldername}')
    files = [f for f in os.listdir(dstname) if os.path.isfile(os.path.join(dstname, f))]
    
    for file in files:
        base, extension = os.path.splitext(file)
        newpath = f'{dstname}/{foldername}/{extension}'
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        shutil.move(os.path.join(dstname, file), f'{dstname}/{foldername}/{extension}/{base}{extension}') #error #2


def numgenerator(srcfilesfound, dstfilesfound):
    i1 = len(srcfilesfound) + len(dstfilesfound)
    i2 = int(str(i1) + '0')
    return '---' + str(randint(i1, i2))
