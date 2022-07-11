# At least 8 char long 
# contain any sort of letters, numbers, +%#@

import re

#Minimum eight characters, at least one letter, one number and one special character
pattern = re.compile(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$")

a = pattern.fullmatch("bbaaaqqq123#")
print(a)