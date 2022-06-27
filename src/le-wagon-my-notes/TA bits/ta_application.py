'''
spinWords("Hey fellow Le Wagon alumni") => "Hey wollef Le nogaW inmula"
spinWords("Rake it until you make it") => "Rake it litnu you make it"
spinWords("Change your life, learn to code") => "egnahC your life, nrael to code"
'''
import re
import string
# >>> re.findall(r"[\w']+|[.,!?;]", "Hello, I'm a string!")
# x = re.findall(r"[\w']+|[.,!?;]", input_sentence)

def spinWords(input_sentence):
    output_sentence = []
    worker = input_sentence.split()
    for word in worker:
        if len(word) < 5:
            output_sentence.append(word)
            continue
        no_chars = sum([1 for x in string.ascii_letters if x in word])
        if no_chars >= 5:
            word = word[::-1]
        output_sentence.append(word)
    return ' '.join(output_sentence)



print(spinWords("Hey fellow Le Wagon alumni"))
print(spinWords("Rake it until you make it"))
print(spinWords("Change your life, learn to code"))
