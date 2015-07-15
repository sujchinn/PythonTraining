__author__ = 'sujchinn'
#prompt the user for DOB in dd-mm-yyyy
# if it is today print "Happy Birthday"
# else Adv or Belated wishes
import time
sys_date = time.localtime()[2]
sys_month = time.localtime()[1]
sys_year = time.localtime()[0]
dob = raw_input("Please enter you Date of Birthday in dd-mm-yyyy : ")
if int(dob.split("-")[0])==sys_date and int(dob.split("-")[1])==sys_month:
    print "Happy Birthday"
elif int(dob.split("-")[1])<sys_month:
    print "Belated Wishes"
else:
    print "Advance Wishes"