__author__ = 'sujchinn'
names=["hari","manu","john","amar","raja"]
result=[]
for name in names:
    result.append(name[0].upper()+name[1:-1]+name[-1].upper())
print result