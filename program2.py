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

def header():
    print ("Password Validator")

header()

def password ():
   _password = input("Enter Password here: ")
   return _password

pword = password ()

def uprLetters ():
    alphabets_in_capital = []
    for i in range (65,91):
       alphabets_in_capital.append(chr(i))
    return alphabets_in_capital

capitalLetters = uprLetters ()

def lwrLetters ():
    alphabets_not_in_capital = []
    for i in range (97,123):
       alphabets_not_in_capital.append(chr(i))
    return alphabets_not_in_capital

notCapitalLetters = lwrLetters ()

def numericCharacters ():
    _numbers = ['0','1','2','3','4','5','6','7','8','9']
    return _numbers

numbers = numericCharacters ()

#countletters

def countLetters (string):
    string1 = string.strip()
    count = 0
    for i in string1:
        if i in capitalLetters or i in notCapitalLetters:
            count += 1
    return count

cntLetters = countLetters (pword)

#capital letters

def countCapLetters (string):
    string2 = string.strip()
    count = 0
    for i in string2:
        if i in capitalLetters:
            count += 1
    return count

cntcapLetters = countCapLetters (pword)

#numbers

def countNumbers (string):
    string3 = string.strip()
    count = 0
    for i in string3:
        if i in numbers:
            count += 1
    return count

cntNumbers = countNumbers (pword)

#special character

def countSpecialCharacters (string):
    string4 = string.strip()
    count = 0
    for i in string4:
        if i not in numbers and i not in capitalLetters and i not in notCapitalLetters:
            count += 1
    return count

cntSpecialCharacters = countSpecialCharacters (pword)


print(cntLetters,cntcapLetters,cntNumbers,cntSpecialCharacters)