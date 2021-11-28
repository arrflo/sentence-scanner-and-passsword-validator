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
    _sentence = input("Enter a sentence here:")
    return _sentence

def display (w,v,c):
    print (f"words: {w}")
    print (f"vowels: {v}")
    print (f"consonants: {c}")

sentence = sentEnce ()

def numberWords (string):
    string1 = string.strip()
    count = 1 
    for i in string1:
        if i ==" ":
            count = count + 1
    return count

def numberVowels (string):
    string2 = string.strip()
    count = 0
    for i in string2:
        if i=="a" or i=="e" or i=="i" or i == "o" or i=="u" and i != " ":
            count = count + 1
    return count


def numberConsonants (string):
    string3 = string.strip()
    count = 0
    for i in string3:
        if i !="0" != "1" != "2" != "3" != "4" != "5" != "6"  != "7" != "8" != "9" !="a" != "e" != "i" != "o" !="u":
            count = count + 1
    return count

words = numberWords (sentence)
vowels = numberVowels (sentence)
consonants = numberConsonants (sentence)

display (words, vowels, consonants)

# words = numberWords (sentence)
# vowels = numberVowels (sentence)
# consonants = numberConsonants (sentence)
# display (words, vowels, consonants)
