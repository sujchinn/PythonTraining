__author__ = 'sujchinn'
user = raw_input("Enter the date\n")
#assume the user input format is  one of the following
#15-may-2015
#15-MAY-2015
#15-May-2010

month={
    'jan':1,
    'feb':2,
    'mar':3,
    'apr':4
}
dd,mm,yy = user.split("-")
#print dd,mm,yy
inp_month = user.split("-")[1].lower()
#print "your month",user.split("-")[1],"is",month[inp_month],"month in the year"
print user.split("-")[0]+"-"+str(month[inp_month])+"-"+user.split("-")[2]