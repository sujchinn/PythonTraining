__author__ = 'sujchinn'
try:
    text=raw_input("Enter a number")
    num = int(text)
except ValueError :
    num=0
except EOFError :
    num=0
except Exception as e: #Generic catch block
    #we also have else: and finally:
    print e
print "fine",num