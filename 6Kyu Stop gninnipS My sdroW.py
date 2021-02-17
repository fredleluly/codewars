def spin_words(sentence):
    returned = sentence.split()
    for i in range(len(returned)):
        if len(returned[i]) >= 5:
            returned[i] = ''.join([c for c in reversed(returned[i])])
    return(' '.join(returned))
    return None
def spin_words(sentence):
    return ' '.join([''.join([c for c in reversed(i)]) if len(i) >= 5 else i for i in sentence.split()])
#print(solve())
print(spin_words("Welcome"), "emocleW")

