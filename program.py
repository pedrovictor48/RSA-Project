from functions.uteis import *

def main():
    escolha = requisitarEscolha()

    if escolha == 1:
        gerarChavePublica()
    elif escolha == 2:
        pass
    else:
        pass
    print(bcolors.OKGREEN + "Feito!" + bcolors.ENDC)
    print("O que deseja fazer em seguida?")

if __name__ == "__main__":
    printHead()
    while True:
        main()
