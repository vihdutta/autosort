import os
import shutil
from pathlib import Path, PurePath
from random import randint

RICH_TEXT_FORE_NL = '<span style=\' font-family:"Segoe UI Light"; font-size:18pt; font-weight:400; color:#a89769;\' ><br>'
RICH_TEXT_FORE = '<span style=\' font-family:"Segoe UI Light"; font-size:18pt; font-weight:400; color:#a89769;\' >'
PLAIN_TEXT_FORE = '<span style=\' font-family:"Segoe UI Light"; font-size:18pt; font-weight:400; color:#ffffff;\' >'
TEXTBACK = '</span>'

def filesnumrenamer(dstname, srcfiles, dstfiles, truepath, id_filelist):
    filesidrenamer(dstname, srcfiles, dstfiles, truepath)

    for file in Path(truepath).iterdir():
        name, extension = PurePath(file).stem, PurePath(file).suffix #error #1
        name = name.split('---', 1)[0]
        id_filelist.append(name + '---' + extension)
        fileamount = id_filelist.count(name + '---' + extension) - 1
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
                    file_ider = file.split('(')[0] + num + file.split('(')[1]
                except IndexError:
                    file_ider = file + num 
            else:
                try:
                    file_ider = file.split('.')[0] + num + '.' + file.split('.')[1]
                except IndexError:
                    file_ider = file + num
            os.rename(os.path.join(truepath, file), os.path.join(truepath, file_ider))



def dstsort(dstname, truepath):
    files = [f for f in os.listdir(truepath) if os.path.isfile(os.path.join(truepath, f))]
    for file in files:
        name, extension = PurePath(file).stem, PurePath(file).suffix
        new_dir = PurePath(truepath, extension).joinpath()
        if not Path(new_dir).exists():
            Path(new_dir).mkdir()
        filename = name + extension
        old_path = Path(truepath) / file
        new_path = Path(truepath) / extension / filename
        shutil.move(old_path, new_path)


def createid(srcfiles, dstfiles):
    i1 = len(srcfiles) + len(dstfiles)
    i2 = int(str(i1) + '0')
    return '---' + str(randint(i1, i2))
