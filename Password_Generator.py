#Task1:-Random Password Generator

#import necessary modules
import random
import string

#create strings of alphabets,digits & punctuation
str1 = string.ascii_lowercase
str2 = string.ascii_uppercase
str3 = string.digits
str4 = string.punctuation

#define length of the password
length = int(input("Enter the length of password: "))

#create a list 'str' which stores all the values after concatenation
str = []
str.extend(str1)
str.extend(str2)
str.extend(str3)
str.extend(str4)

print("Password is: ")
#shuffle the characters and print them as random password
print("".join(random.sample(str, length)))
