__author__ = 'sujchinn'
with open("../doc/prods.txt","r") as f1:
    arr=map(lambda x: int(x.split()[1]),f1)
    print sum(arr)