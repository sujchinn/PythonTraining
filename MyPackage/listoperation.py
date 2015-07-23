__author__ = 'sujchinn'

def addnames(a,b):
    #pass   kust return nothing
    if b in a:
        raise Exception("Name already exists")
    else:
        a.append(b)

def delnames(a,b):
    if b not in a:
        raise Exception("Names doesn't exist in the list")
    else:
        a.remove(b)

names_list=["john","john","banu","lala","arun"]
try:
    new_name=raw_input("Enter a name to be Added: ")
    addnames(names_list,new_name)
    print names_list
    del_name = raw_input("Enter the name to deleted :")
    delnames(names_list,del_name)
    print names_list
except Exception as e:
    print e
