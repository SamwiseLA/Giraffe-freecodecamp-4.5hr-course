print("Giraffe Academy")
# New Line \n
print("Giraffe\nAcademy")
# Use " in string, \"
print("Giraffe \"Academy\"")

print("===========")

phrase = "Giraffe Academy Rules"

print(phrase)
# Concatingation -> use +
print(phrase+" is cool!")

# . Notation function
print("=== .lower() & .upper() ========")
print(phrase.lower())
print(phrase.upper())

print("=== .isupper ========")
print(phrase.isupper())

print("=== .upper().isupper() ========")
print(phrase.upper().isupper())

print("=== __len__() ========")
print(phrase.__len__())

print("=== len() ========")
print(len(phrase))

print("==== character at [0] ======== 1 character ")
print(phrase[0])
print("=== chjaracters at [0:4] ======== 1st param, character start with, through 2nd position end with subtract 1")
print(phrase[0:4])
print("=======")

# find first space location
second_word_start = phrase.find(" ") + 1
second_word_end = phrase.find(" ",second_word_start+1)
phraselen = len(phrase)

print("2nd word starts: "+str(second_word_start))
print("2nd word ends: "+str(second_word_end))
print("Lengh of phrase is: "+str(phraselen))

print("")

second_word_on = phrase[second_word_start:]
print("Phrase starting at 2nd word: ["+second_word_on+"]")
second_word_on = phrase[second_word_start:second_word_end]
print("2nd word in Phrase: ["+second_word_on+"]")

print("====== index(\"my\") What position is string my")
print(phrase.index("my"))
print("====== index(\"ac\") What position is string ac")
print(phrase.lower().index("ac"))

print("=================")
print("====== .replace(\"emy\", str(1000)) ====== ")
phrase2 = phrase.replace("emy", str(1000))
print(phrase2)
