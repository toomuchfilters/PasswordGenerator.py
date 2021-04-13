import random
import string
print()
print()
print("RANDOM PASSWORD GENERATOR BY TOOMUCHFILTERS")
print()
print('DISCLAIMER!!')
print('PLS PASTE THE GENERATED PASSWORD ON A HAVEIBEENPAWNED WEBSITE TO CHECK IT ITS SAFE')
length = int(input('\nEnter The Length Of The Password: '))
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
numbers = string.digits
symbols = string.ascii_letters
all = lowercase + uppercase + numbers + symbols
temp = random.sample(all,length)
password = "".join(temp)

print("YOUR NEW PASSWORD HAS BEEN RANDOMLY GENERATED") 
print(password)
