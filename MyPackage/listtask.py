__author__ = 'sujchinn'
fruits = [
    "apple=5",
    "banana=10",
    "orange=2",
    "pineapple=5",
    "payaya=10",
    "chickoo=3"
]
weight = []
for fruit in fruits:
    if len(fruit.split("=")) ==2:
        print fruit.split("=")[0]
        weight.append(int(fruit.split("=")[1]))
    else:
        continue
print "Total weight",sum(weight)