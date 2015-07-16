__author__ = 'sujchinn'
snacks = {
    'vada':40,
    'bhel':35,
    'pizza':25,
    'puri':35,
    'idli':50
}
try:
    user_choice=raw_input("Enter snacks : ")
    print "The price of "+user_choice+" is "+str(snacks[user_choice.lower()])
except KeyError:
    print "Item unavailable"
finally:
    print "Bye!"
