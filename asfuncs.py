import os
import shutil
from datetime import datetime
from random import randint

richtextforenl = '<span style=\' font-family:"Segoe UI Light"; font-size:18pt; font-weight:400; color:#a89769;\' ><br>'
richtextfore = '<span style=\' font-family:"Segoe UI Light"; font-size:18pt; font-weight:400; color:#a89769;\' >'
plaintextfore = '<span style=\' font-family:"Segoe UI Light"; font-size:18pt; font-weight:400; color:#ffffff;\' >'
textback = '</span>'

def filesnumrenamer(dstname, srcfiles, dstfiles, truepath, idfilelist):
    filesidrenamer(dstname, srcfiles, dstfiles, truepath)

    for i, file in enumerate(os.listdir(truepath)):
        name, extension = os.path.splitext(file) #error #1
        name = name.split('---', 1)[0]
        idfilelist.append(name + '---' + extension)
        fileamount = idfilelist.count(name + '---' + extension) - 1
        if fileamount > 0:
            iparentheses = '(' + str(fileamount) + ')'
        else:
            iparentheses = ''
        filerename = ''.join([name, iparentheses, extension])
        os.rename(os.path.join(truepath, file), os.path.join(truepath, filerename))


def filesidrenamer(dstname, srcfiles, dstfiles, truepath):
    for root, dirs, files in os.walk(dstname):
        for file in os.listdir(truepath):
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
            os.rename(os.path.join(truepath, file), os.path.join(truepath, fileider))



def dstsort(dstname, truepath):
    files = [f for f in os.listdir(truepath) if os.path.isfile(os.path.join(truepath, f))]
    for file in files:
        name, extension = os.path.splitext(file)
        newpath = os.path.join(truepath, extension)
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        shutil.move(os.path.join(truepath, file), os.path.join(truepath, extension, name+extension))


def createid(srcfiles, dstfiles):
    i1 = len(srcfiles) + len(dstfiles)
    i2 = int(str(i1) + '0')
    return '---' + str(randint(i1, i2))
