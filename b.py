import random
import string

leng = 5
string_pool = string.ascii_uppercase
string_int_pool = string.digits
result = ''
for i in range(leng):
    result+=random.choice(string_pool)
for i in range(leng):
    result+=random.choice(string_int_pool)
print(result)

