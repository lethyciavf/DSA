#Exercicio do curso de Analise de dados 3.0 da DataScienceAcademy

import random

desenho = ['''
>>>>>>>>>>Forca<<<<<<<<<<
    +---+
    |   |
    |
    |
    |
    |
=========''', '''
    +---+
    |   |
    |   O
    |
    |
    |
=========''', '''
    +---+
    |   |
    |   O
    |   |
    |
    |
=========''', '''
    +---+
    |   |
    |   O
    |   |\ 
    |
    |
=========''', '''
    +---+
    |   |
    |   O
    |  /|\ 
    |
    |
=========''', '''
    +---+
    |   |
    |   O
    |  /|\ 
    |    \ 
    |
=========''',
'''    
    +---+
    |   |
    |   O
    |  /|\ 
    |  / \ 
    |
=========''']

class Forca: #Por convenção, as classes começam com letra maiuscula
    def __init__(self, palavra): #Ferramenta para a construção da classe
        self.palavra = palavra
        self.letra_errada = [] #Lista vazia que vai guardar as tentativas
        self.letras_corretas = []

    def tentativa(self, letra):
        if letra in self.palavra and letra not in self.letras_corretas: #Verifica se a entrada do usuario existe ou não na palavra
            self.letras_corretas.append(letra)
        elif letra not in self.palavra and letra not in self.letra_errada:
            self.letra_errada.append(letra)
        else:
            return False
        return True

    def fim_forca(self):
        return self.ganhou() or (len(self.letra_errada) == 6) #verifica se o jogo finalizou

    def ganhou(self):
        if '*' not in self.esconde_palavra():
            return True
        return False

    def esconde_palavra(self):
        saida = ''
        for letra in self.palavra:
            if letra not in self.letras_corretas:
                saida += '*'
            else:
                saida += letra
        return saida

    def saida_status(self):
        print(desenho[len(self.letra_errada)])
        print(f"\nPalavra: {self.esconde_palavra()}")
        print(f"\nLetras erradas: {self.letra_errada}")
        print(f"\nLetras corretas: {self.letras_corretas}")

def escolhe_palavra():
    with open('palavra.txt', 'rt') as palavra:
        dados = palavra.readlines()
    return dados[random.randint(0, len(dados))].strip()

def main():
    jogo = Forca(escolhe_palavra())

    while not jogo.fim_forca():
        jogo.saida_status()
        entrada = input(f"\nDigite uma letra: ")
        jogo.tentativa(entrada)

    jogo.saida_status()

    if jogo.ganhou():
        print(f"\nParabéns, você ganhou!")
    else:
        print(f"\nGame Over :( A palavra era: {jogo.palavra}")

if __name__ == '__main__':
    main()