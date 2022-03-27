import os
with open('palavras.txt') as f:
    lines = f.readlines()
    palavras = []

    for element in lines:
        palavras.append(element.strip())
    f.close()



