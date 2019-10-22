#!/usr/bin/python3

import cgi
# o receive data from web  http protocol

print("Content-type:text/html")
print("")

html_data=cgi.FieldStorage()
# only looking for form data and those variables data as well
username=html_data.getvalue('u')
password=html_data.getvalue('p')



if  username == 'adhoc' and password =='devops' :
    print("<meta http-equiv='refresh' content='1;url=http://3.92.229.39/service.html'>")

else :
    print(" no hello at all ")
