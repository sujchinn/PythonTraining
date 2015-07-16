__author__ = 'sujchinn'
nums=[10,20,30,40,50]

def sqr(num):
    return num*num
sqrval = map(sqr,nums)
print sqrval

data=[123,541,76,34,78]
dataStr=map(str,data)
def getfirstchar(name):
    return name[0]

firstchar = map(getfirstchar,dataStr)
print firstchar

names = ["john","raja","tara","ramu","elan"]
def changeStr(name):
    return (name[0].upper()+name[1:-1]+name[-1].upper())
names[:]=map(changeStr,names)
print names

def getmonth(date):
    return date.split("-")[1]

date = ['10-may-2015','18-june-2014']
res = map(getmonth,date)
print res
