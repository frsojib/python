numOfWords = 0
numOfLetters = 0
numOfDigits = 0

text = input("Enter a text of numbers: ")

for x in text:
    x = x.lower()
    if x >= 'a' and x<= 'z':
        numOfLetters= numOfLetters+1
    elif x >= '0' and x<= '9':
        numOfDigits= numOfDigits + 1
    elif x == " ":
        numOfWords= numOfWords + 1

print("Number of letetrs: ", numOfLetters)
print("Number of Digits: ", numOfDigits)
print("Number of Words: ", numOfWords)