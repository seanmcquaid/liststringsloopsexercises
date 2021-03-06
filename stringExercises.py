# Uppercase a string

my_string = "sean mcquaid"
print my_string.upper()

#capitalize a string
print my_string.capitalize()

# Reverse a string
print my_string[::-1]

list_string = list(my_string)
list_string.reverse()

print "".join(list_string)

lengthOfString = len(my_string)
print lengthOfString

reversed_string = ""

for i in range (0, lengthOfString):
    reversed_string += my_string[lengthOfString - (i+1)]
    print reversed_string

# Leetspeak

#with replace
leet_string = my_string.upper()

print leet_string.replace("A", "4").replace("E", "3").replace("G", "6").replace("I", "1").replace("O", "0").replace("S", "5").replace("T", "7")

# with a dictionary

leetDict = {
    "A" : 4,
    "E" : 3,
    "G" : 6,
    "I" : 1,
    "O" : 0,
    "S" : 5,
    "T" : 7,
}

final_string = ""

for i in range(0, len(leet_string)):
    current_letter = leet_string[i]
    if current_letter in leetDict:
        current_letter = str(leetDict[current_letter])
    final_string += current_letter

print final_string

# long-long vowels

vowels = {
    "a" : "aaaaa",
    "e" : "eeeee",
    "i" : "iiiii",
    "o" : "ooooo",
    "u" : "uuuuu"
}

long_vowel_string = ""

for i in range(0,len(my_string)):
    current_letter = my_string[i]
    nextLetter = my_string[i+1]
    if(current_letter == nextLetter) and (i != len(my_string) -1):
        if current_letter in vowels:
            current_letter = vowels[current_letter]
            long_vowel_string += current_letter

print long_vowel_string

# caesar cipher

caesar_string = "lbh zhfg hayrnea jung lbh unir yrnearq"

decoded_string = ""

alphabet = {
   
}