from Lista_de_Palavras import palavras
import random

def escolher_palavra():
    palavra = random.choice(palavras)
    return  palavra.upper()

def play(palavra):
    palavra_conclusao = "_" * len(palavra)
    chutadas = False
    chutadas_letras = []
    chutadas_palavras = []
    tentativas = 6
    print('Partiu jogar forca!')
    print(display_hangman(tentativas))
    print(palavra_conclusao)
    print('\n')
    while not chutadas and tentativas >0:
        chute = input('Chute uma letra ou uma palavra! ').upper()
        if len(chute) == 1 and chute.isalpha(): #isalpha é uma função que retorna o 'TRUE' se o chute for uma LETRA.
            if chute in chutadas_letras:
                print("Essa aí já foi, mermão. Presta atenção, porra.")
            elif chute not in palavra:
                print('ERRRRRRRRRRRRRRRRRROOOOOOOOOOOOU!!!!')
                tentativas -=1
                chutadas_letras.append(chute)
            else:
                print('Ae, caraio! Certin, irmão!')
                chutadas_letras.append(chute)
                palavraaslist = list(palavra_conclusao)
                indices = [i for i, letra in enumerate(palavra) if letra == chute]
                for index in indices:
                    palavraaslist[index] = chute
                palavra_conclusao = "".join(palavraaslist)
                if "_" not in palavra_conclusao:
                    chutadas = True
        elif len(chute) == len(palavra) and chute.isalpha():
            if chute in chutadas_palavras:
                print("Tu ja chutou essa, carai.")
            elif chute!= palavra:
                print('ERRRRROU. NÃO É A PALAVRA!')
                tentativas -=1
                chutadas_palavras.append(chute)
            else:
                chutadas = True
                palavra_conclusao = palavra
        else:
            print('Esse chute tá errado, irmão. É invalido!')
        print(display_hangman(tentativas))
        print(palavra_conclusao)
        print('\n')
    if chutadas:
        print('Parabens. Venceu. Foda-se. Bjs')
    else:
        print('SE FUDEUUU KKKK tá enforcado. LOL A palavra era ' + palavra)

def display_hangman(tentativas):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tentativas]

def main():
    palavra = escolher_palavra()
    play(palavra)
    while input('Mais uma jogada, chefia? (s/n) ').lower() == 's':
        palavra = escolher_palavra()
        play(palavra)
if __name__ == "__main__":
    main()
