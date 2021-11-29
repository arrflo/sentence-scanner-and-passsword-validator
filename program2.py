# Program 2: Password validator
# Create a program that check if password is valid
# The password is valid if all criteria are met:
# a. Greater than 15 letters
# b. Have at least one capital letter
# c. Have at least one number
# d. Have at least one special char (!@#$%^&*()_+ etc)
# ex.
# input: P@ssw0rd+P@ssw0rd
# ouput: Valid

# Tip: loop through each character of the input then process it letter by letter

def password ():
   _password = input("Enter Password here!: ")
   return _password

pword = password ()
#countletters

def countLetters (string):
    string1 = string.strip()
    count = 0
    for i in string1:
        count = count + 1
    return count

cLetters = countLetters (pword)