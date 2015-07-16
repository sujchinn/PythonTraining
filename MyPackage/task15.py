__author__ = 'sujchinn'
with open("..\doc\zones.txt","r") as f1:
    arr=map(lambda x:x.split(",")[0].strip()+" "+str(len(x.split(",")[1].split()))+" "+str(sum(map(int,(x.split(",")[2].split())))),f1)
    print "\n".join(arr)