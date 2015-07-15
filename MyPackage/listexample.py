__author__ = 'sujchinn'

#values=[]
#get 5 integers and add to array and print it
#print sum, max and min without inbuilt

values=[]
for i in xrange(5):
    values.append(int(raw_input("Enter "+str(i+1)+" element : " )))
print values
print "The sum is",sum(values)
values.sort()   #self -assignment
print "The max value is",values[-1]
print "The min value is",values[1]


