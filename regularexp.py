# + one or more
# * zero or more
# abcde...z = a-z
# \w alphanumeric characters
# \W other than alpha numeric
# ^ means negation
# \d digit characters
# length '\d{10}' or '\d{10,20}'

import re

pattern = r'[A-Z]+\w+\d+'

sequence = 'zxcklnzxjcklz ashish@gmail.com  asjkdhsajkhd kritika@xzc.com'

print(re.findall(pattern, sequence))