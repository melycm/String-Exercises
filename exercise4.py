newchar = (('A','4'), ('E', '3'), ('G','6'), ('I','1'), ('O','0'), ('S', '5'), ('T', '7'))
phrase = "MY NAME IS MELISSA CANTU, GOODBYE"
new_phrase = phrase
for old, new in newchar:
    new_phrase = new_phrase.replace(old, new)

print(new_phrase)