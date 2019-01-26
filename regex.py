import re

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

mo = phoneRegex.search("My number is 996-721-7718")
print("Phone number found : "+mo.group())

phoneRegex1 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

mo1 = phoneRegex1.search("My number is 996-721-7718 My number is 996-721-7719 My number is 996-721-7720")

print(mo1.group(1))
print(mo1.group(2))
areaCode, actualNum = mo1.groups()
print("areaCode : "+areaCode)
print("Phone Number : "+actualNum)