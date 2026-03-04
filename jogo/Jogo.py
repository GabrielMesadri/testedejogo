from sys import exit

def gold_room():
    print("Esta sala está cheia de ouro. Quanto você pega?")
    choice = input("> ")
    if choice.isdigit():  #para verificar se a entrada é um número
        how_much = int(choice)
    else:
        dead("Cara, aprenda a digitar um número.")
    if how_much < 50:
        print("Legal, você não é ganancioso, você ganhou!")
        exit(0)
    else:
        dead("Você é um bastardo ganancioso!")

def bear_room():
    print("Há um urso aqui.")
    print("O urso tem um monte de mel.")
    print("O urso gordo está na frente de outra porta.")
    print("Como você vai mover o urso?")
    bear_moved = False
    while True:
        choice = input("> ")
        if choice == "take honey":
            dead("O urso olha para você e então dá um tapa na sua cara.")
        elif choice == "taunt bear" and not bear_moved:
            print("O urso se moveu da porta.")
            print("Agora você pode passar por ela.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("O urso fica irritado e morde sua perna.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("Não entendi o que isso significa.")

def cthulhu_room():
    print("Aqui você vê o grande mal Cthulhu.")
    print("Ele, ou o que seja, te observa e você fica insano.")
    print("Você foge pela sua vida ou ele come sua cabeça?")
    choice = input("> ")
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Bem, isso estava saboroso!")
    else:
        cthulhu_room()  #para chamar a função novamente se a entrada não for válida

def dead(why):
    print(why, "Bom trabalho!") 
    exit(0)


def front_rom2():
    print( "voce entra em outra sala e tem duas portas")
    choice = input(">")
    if "right" in choice:
        leon_rom()
    else:
        cobra_rom()

def leon_rom():
  print("parabens, todos o leoes estão mortos, você pode sair")
  choice = input("> ")
  if choice == "Sair":
    liberdade()

def liberdade():
  print("Você conseguiu escapar com sucesso!")
    

def cobra_rom():
    print("todas as cobras sao najas e voce toma uma picada(la ele) e morre ")
    choice = input("> ")
    if choice == "morrer":
        cthulhu_room()




def start(): 
  print("Você esta em uma sala escura.")
  print("Há uma porta à sua direita, esquerda e na sua frente.") 
  print("Qual você escolheria?")
  choice = input("> ")
  if choice == "left": 
    bear_room()
  elif choice == "right": 
    cthulhu_room()
  elif choice == "front":
    front_rom2()
  else: 
    dead("You stumble around the room until you starve.")

start()
