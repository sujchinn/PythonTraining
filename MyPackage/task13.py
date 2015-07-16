__author__ = 'sujchinn'

with open("..\doc\citydetails.txt") as f1: #need not close the file
    for element in f1: #no need to read from file
        print element.split("-")[0]