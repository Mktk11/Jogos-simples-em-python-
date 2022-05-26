from random import randint
import turtle
cont_j1=0
cont_j2=0
lista=["Nada","Tesoura","Papel","Pedra"]
caneta=turtle.Turtle()
caneta.speed(0)
caneta.color("black")
caneta.penup()
caneta.hideturtle()
caneta.goto(0,260)
while(True):
    print("Escolha um número abaixo: ")
    print("----------------------------")
    print("1 - Tesoura")
    print("2 - Papel")
    print("3 - Pedra")
    print("0 - Sair do jogo")
    print("----------------------------")
    J1=int(input("Jogador 1 Digite um número: "))
    J2=randint(1,3)
    if(J1==J2):
        print("O jogador número 1 escolheu {} e O jogador número 2 também escolheu {} -> Empate!!!".format(lista[J1],lista[J2]))
    elif(J1==1 and J2==2):
        print("O jogador número 1 escolheu {} e O jogador número 2 escolheu {} -> Jogador número 1 é o vencedor!!!".format(lista[J1],lista[J2]))
        cont_j1+=1
    elif(J1==1 and J2==3):
        print("O jogador número 1 escolheu {} e O jogador número 2 escolheu {} -> Jogador número 2 é o vencedor!!!".format(lista[J1],lista[J2]))
        cont_j2+=1
    elif(J2==1 and J1==2):
        print("O jogador número 1 escolheu {} e O jogador número 2 escolheu {} -> Jogador número 2 é o vencedor!!!".format(lista[J1],lista[J2]))
        cont_j2+=1
    elif(J2==1 and J1==3):
        print("O jogador número 1 escolheu {} e O jogador número 2 escolheu {} -> Jogador número 1 é o vencedor!!!".format(lista[J1],lista[J2]))
        cont_j1+=1
    elif(J1==2 and J2==3):
        print("O jogador número 1 escolheu {} e O jogador número 2 escolheu {} -> Jogador número 1 é o vencedor!!!".format(lista[J1],lista[J2]))
        cont_j1+=1
    elif(J1==3 and J2==2):
        print("O jogador número 1 escolheu {} e O jogador número 2 escolheu {} -> Jogador número 2 é o vencedor!!!".format(lista[J1],lista[J2]))
        cont_j2+=1
    elif(J1==0):
        print("O placar foi de Jogador 1 {} x {} Jogador 2".format(cont_j1,cont_j2))
        break
    caneta.clear()
    caneta.write("Jogador 1 {} x {} Jogador 2".format(cont_j1,cont_j2),align="center",font=("Courier",20,"normal"))
