from os import scandir, path, mkdir
from datetime import datetime
from os.path import exists
from shutil import move

# Enter path to Sort here
source_dir = "PATHTOSORT"


def print_hi():
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, i will sort your Images :-)')  # Press ⌘F8 to toggle the breakpoint.
    with scandir(source_dir) as entries:
        for entry in entries:
            if not entry.name.startswith('.') and entry.is_file():
                namepath = path.join(source_dir, entry.name)
                filetimestamp = path.getmtime(namepath)
                filedate = datetime.fromtimestamp(filetimestamp)
                year = filedate.strftime("%Y")
                month = filedate.strftime("%m")
                pathyear = path.join(source_dir,year)
                pathyearmonth = path.join(pathyear,month)
                if exists(pathyear):
                    if not exists(pathyearmonth):
                        mkdir(pathyearmonth)
                else:
                    mkdir(pathyear)
                    mkdir(pathyearmonth)
                print(f'Move file: {entry.name} to {pathyearmonth}')
                move(entry, pathyearmonth)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
