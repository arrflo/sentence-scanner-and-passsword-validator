# Program 1:
# Create a program that ask for a sentence as input.
# Display the number of words, vowels and consonants in the input 
# ex.
# input: Bahala kayo dyan
# output:
# words: 3
# vowels: 6
# consonants: 8

def sentEnce():
    _sentence = input("Insert an idea here (sentence): ")
    return _sentence

def display (w,v,c):
    print (f"words: {w}")
    print (f"vowels: {v}")
    print (f"consonants: {c}")

sentence = sentEnce ()


#word count
def numberWords (string):
    string1 = string.strip()
    count = 1 
    for i in string1:
        if i ==" ":
            count += 1
    return count


#vowels
def numberVowels (string):
    string2 = string.strip()
    count = 0
    for i in string2:
        if i in ('a','e','i','o','u') or i in ('A','E','I','O','U'):
            count += 1
    return count


#consonants
def numberConsonants (string):
    string3 = string.strip()
    count = 0
    for i in string3: 
        if i in ('b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z'):
            count = count + 1
        elif i in ('B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z'):
            count += 1
    return count 


words = numberWords (sentence)
vowels = numberVowels (sentence)
consonants = numberConsonants (sentence)

display (words, vowels, consonants)

