__author__ = 'sujchinn'
f2=open("C:\Users\sujchinn\Pictures\service manager\homepage1.png","w")
with open("C:\Users\sujchinn\Pictures\service manager\homepage.png") as f1:
    for record in f1:
        print record
        f2.write(record)