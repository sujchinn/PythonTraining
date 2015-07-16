__author__ = 'sujchinn'
#f1 = open("C:\Users\sujchinn\PycharmProjects\PythonTraining\doc\hello.txt","w")
#print f1
#f1.write("Hello World")

f2= open("..\doc\hello.txt","r")
print f2
arr=f2.read()
f2= open("..\doc\hello.txt","r")
arr1 = f2.readlines()
f3 = open("..\doc\hello.txt","r")
arr2=f3.readline(12)
print arr
print arr1
print arr2

try:
    f1=open("..\doc\hello.txt","r")
    arr=f1.readlines()    # we can also directly do foreach on f1
    for element in arr:
        print element.split()[0]
except IOError as e:
    print e
else:    #if f1 is not null
    f1.close()
