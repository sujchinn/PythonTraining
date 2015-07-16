__author__ = 'sujchinn'
studs = {
    "arun":50,
    "chet":30,
    "john":80,
    "mani":20,
    "elan":20
}

print studs
print studs['chet']
print'amar' in studs
print 'john' in studs
del studs['john']
print studs
print studs.keys()
print studs.values()
studs['anup'] = 50
print studs
del studs
try:
    print studs
except NameError:
    print "Studs unavailable because it was deleted"