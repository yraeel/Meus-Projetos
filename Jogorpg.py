#jogo rpg

from random import randint

lista = []
opcoes = {1: "Guerreiro(a)", 2: "Mago(a)", 3: "Elfo(a)", 4: "Dwarf", 5: "Hobbit"}

class Jogador():
    def __init__(self,classe, trocacl, nome, forca, inteligencia):
        self.classe = classe
        self.trocacl = trocacl
        self.nome = nome
        self.forca = forca
        self.inteligencia = inteligencia
        

#função que escolhe classe

    def escolhaClasse(self):
        print("""Suas opções são:
        [1] - Guerreiro(a)
        [2] - Mago(a)
        [3] - Elfo(a)
        [4] - Dwarf
        [5] - Hobbit
        """)
        
        escolha = int(input("Escolha sua opção: "))
        if escolha in opcoes:
            self.classe = opcoes[escolha]
            lista.append(self.classe)
            print("Você escolheu a classe:", self.classe)
        else:
            print("Opção inválida.")


            
        
#função que troca de classe

    def trocarClasse(self):
        while True:

            troca = input("Deseja trocar de classe? [s/n]")
            if troca == "s":
                lista.pop()
                self.escolhaClasse()
                
                            
            elif troca == "n":
                print("Sua classe atual é ", self.classe)
                break

            else:
                print("Opção inválida.")

    
    

        

    
    def inserirNome(self):
        nome = input("Digite seu nome: ")
        lista.append(nome)
        self.nome = nome
        
    #todos os jogadores começam com apenas 1 ponto de forca
    
    def inserirForca(self):
        forca = 1
        lista.append(forca)
        

    def inserirInteligencia(self):
        inteligencia = 1
        lista.append(inteligencia)
        print(lista)



    def monstro(self):
        print("""Monstro nivel 1. 
        HP = 100
        Ataque = 1
        Defesa = 1
        """)
        user = Jogador('','','','','')
        monstro_hp = 100
        acertos = 0

        for rodada in range(3):
            print("Você possui um dado de 6 lados para jogar.")
            jogada = input("Deseja jogar o dado? [s/n]")
            if jogada == "s":
                dado = randint(1,6)
                print("Sua jogada foi: {}".format(dado))

                if dado >= 4:
                    print("Você acertou o monstro e causou 10 pontos de dano.")
                    monstro_hp -= 10
                    acertos += 1
                    if acertos == 3 or monstro_hp <= 10:
                    
                        print("Você derrotou o monstro. Pode prosseguir!")
                        break
                else:
                    print("Você perdeu essa rodada")

            elif jogada == "n":
                break
        
        if monstro_hp > 0:
            print("Você foi derrotado. Tente novamente.")
        else:
            print("Parabéns, você venceu!")














user = Jogador('', '','','','')
print("""Introdução, esse é um jogo RPG.
Você começara com apenas 1 ponto em todos os atributos.
Ao decorrer da partida, você lutará contra monstros, cada um possuindo determinado nivel.
Você precisará vencer as batalhas contra esses monstros se quiser prosseguir.
As rodadas serão decididas em 3 rodadas jogadas por um dado de 6 lados, você precisa tirar maior que 4 em pelo menos 2 vezes para vencer.
Boa sorte!""")

user.escolhaClasse()
user.trocarClasse()
user.inserirNome()
user.monstro()


while True:
    jogar = input("Deseja jogar novamente?")
    if jogar == "s":
        user.escolhaClasse()
        user.trocarClasse()
        user.inserirNome()
        user.inserirForca()
        user.inserirInteligencia()
        user.monstro()
        

    elif jogar == "n":
        print("Até logo!")
        break
