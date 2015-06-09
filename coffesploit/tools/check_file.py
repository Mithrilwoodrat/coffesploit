import os
from config import EXP_FOLDER

def read_date(filename):
    f = open(filename,'r')
    for line in f.readlines():
        if 'date=' in line:
            date=line.split('=')[1]
            date = date.strip()
            return date
    return None

def read_name(filename):
    f = open(filename,'r')
    for line in f.readlines():
        if 'name=' in line:
            name = line.split('=')[1]
            name = name.strip()
            return name
    return None

file_list = os.listdir(EXP_FOLDER)

def list_date(file_list):
    date_list = []
    for f in file_list:
        date = read_date(EXP_FOLDER+f)
        if date:
            date_list.append(date)
    return date_list

date_list = list_date(file_list)


def list_name(file_list):
    name_list = []
    for f in file_list:
        name = read_name(EXP_FOLDER+f)
        if name:
            name_list.append(name)
    return name_list

name_list = list_name(file_list)

def update_lists():
    global file_list,date_list,name_list
    file_list = os.listdir(EXP_FOLDER)
    date_list = list_date(file_list)
    name_list = list_name(file_list)

def check_file(filename):
    date = read_date(filename)
    name = read_name(filename)
    if filename in file_list:
        return False
    elif (date and date not in date_list) and (name and name in name_list) :
        return False
    elif name in name_list and date in date_list:
        return False
    else:
        update_lists()
        return True