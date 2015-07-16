__author__ = 'sujchinn'
zones = ['north','south','east','west']

def getfirstchar(name):
    return name[0]

firstchar=map(getfirstchar,zones)
print firstchar