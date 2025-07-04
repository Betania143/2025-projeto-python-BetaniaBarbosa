'''
Projeto: Jogo Da Forca
Python
2025/06/30
Betânia de Paula Maciel Barbosa
'''
# Objetivo: Desenvolver um jogo onde o jogador tenta adivinhar uma fruta completando a palavra com tentativas corretas, e a cada erro diminui 1 chance, se perder todas as chances, o jogador perde a partida
 
import random # Importando a biblioteca random para escolher uma palavra aleatória
frutas = ["abacaxi", "banana", "laranja", "uva", "morango","kiwi", "melancia"] # Lista de fruta para o jogador adivinhar
letrasUsuario = [] # Lista para armazenar as letras que o usuário já tentou
palavra = random.choice(frutas) # Escolhendo uma palavra aleatória da lista de frutas
chances = 7 # Número de chances que o usuário tem para adivinhar a palavra
ganhou = False # Variável para verificar se o usuário ganhou

def mostrarPalavra(palavra, letrasUsuario): # Função para exibir a palavra com as letras adivinhadas pelo usuário
    exibicao = "" # inicialização da string de exibição
    for letra in palavra: # Percorrendo cada letra da palavra
        if letra in letrasUsuario: # Se a letra já foi adivinhada pelo usuário
            exibicao += letra + " " # Adiciona a letra à exibição com um espaço
        else: # Se a etra não foi adivinhada
            exibicao += "_" # Adiciona um espaço em branco para a letra não adivinhada
        return exibicao.strip() # Retorna a string de exibição sem espaços extras no início ou no final

while True: # Loop de início do jogo
    print("\nPalavra:", mostrarPalavra(palavra, letrasUsuario)) # Exibe a palavra com as letras adivinhadas
    print("Cuidado, você tem essas chances restantes: {chances}") # Exibe o número de chances restantes

    tentativa = input("Digite uma letra: ") # Pede para o usuário digitar uma letra
    if tentativa.isalpha() and len(tentativa) == 1: # Vefirifica se a tentativa é uma letra válida
        if tentativa not in letrasUsuario: # verifica se a letra já foi tentada
            letrasUsuario.append(tentativa) # adicionar a letra à lista de letras tentadas
            if tentativa not in palavra: # Verifica se a letra está na palavra
                chances -= 1 # Se a letra não estiver na alavra perde uma chance
            else: # Se a letra estiver na palavra
                print(f"Boa! A letra '{tentativa}' está na palavra! Que bom, neh?") # Msg de sucesso

            ganhou = True # Inicializa a variável ganhou como True
            for letra in palavra: # Se todas as letras da palavra foram adivinhadas
                if letra not in letrasUsuario: # Se a letra não foi adivinhada
                    ganhou = False # A variável ganhou é definida como False
                    break # O loop é interrompido
            
            if chances == 0 or ganhou: # Se o usuário não tiver mais chances ou se ele ganhou
                break # O loop é interrompido

if ganhou: # Se o usuário ganhou
     print(f"\nIsso! Essa era a palavra! Parabéns, você ganhou. A palavra era: {palavra}") # Mg de vitória
else: # Se o usuário perdeu
     print(f"\nAh não... você perdeu! A palavra era: {palavra}") # Msg de derrota