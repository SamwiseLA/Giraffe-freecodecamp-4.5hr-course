def f_translate(s_phrase):
    # This Function will take in a phrase
    # examine each letter and if the letter is a vowel
    # it will replace it with a correct case "G", or "g"
    #
    s_translation = ""
    s_vowels = "AEIOU"
    for s_letter in s_phrase:
        if s_letter.upper() in s_vowels:
            if s_letter.isupper():
                s_translation = s_translation + "G"
            else:
                s_translation = s_translation + "g"
        else:
            s_translation = s_translation + s_letter

    return s_translation


print("Translated Phrase: " + f_translate(input("Beginning  Phrase: ")))
