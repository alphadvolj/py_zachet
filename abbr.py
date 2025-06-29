def abbr(phrase: str) -> str:
    words = phrase.split()
    abbr = ''
    for word in words:
        if word and word[0].isalpha():
            abbr += word[0].upper()
    return abbr


phrase = input()
print(abbr(phrase))
