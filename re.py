import re
print (re.findall(r'\S','fyit syit tyit 123456'))
print (re.findall(r'\d','fyit syit tyit 123456'))
print (re.findall(r'\D','fyit syit tyit 123456'))
print (re.split(r'\s','fyit syit tyit 123456'))
print (re.findall(r'\s','fyit syit tyit 123456'))
print (re.findall(r'\A','fyit syit tyit 123456'))
print (re.findall(r'\z','fyit syit tyit 123456'))
print (re.findall(r'\t|t','fyit syit tyit 123456'))
