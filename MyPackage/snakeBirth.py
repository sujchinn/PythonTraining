__author__ = 'sujchinn'

#write a program to add two numbers given from the keyboard and display the formatted result
a=raw_input("Enter a Value : ")
b=raw_input("Enter b Value : ")
c=int(a)+int(b)
print "The sum of {0} and {1} is {2}".format(a,b,c)
print "The sum of %s and %s is %d" %(a,b,c)
print "The sum of "+a+" and "+b+" is "+str(c)
print "The sum of "+a+" and "+b+" is "+repr(c)
print "The sum of",a,"and",b,"is",c            #no space required after and before constant string

