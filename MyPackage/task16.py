__author__ = 'sujchinn'
zones={
    'north':56,
    'south':86,
    'east':74,
    'west':46
}

res = zones.keys()
res.sort()              #sort by key

for key in res:
    print key,zones[key]

#sort by values
print "\n\nSorting by value"
for key in sorted(zones,key =lambda x: zones[x]):
    print key,zones[key]