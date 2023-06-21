import math
class Calculadora:
    def __init__(self, num1, num2, menu):
        self.num1 = num1
        self.num2 = num2
        self.menu = menu

    @staticmethod
    def opcoes_do_menu():
        print("*"*10 +"Menu" + "*"*10)
        print("~"*24)
        print("[1] Adicao")
        print("[2] Subtracao")
        print("[3] Multiplicacao")
        print("[4] Divisao")
        print("[5] Exponenciacao")
        print("[6] Radiciacao")
        print("[7] Moludo")
        print("[0] SAIR")

    @staticmethod
    def escolher_opcao():
        while True:
                opcao_escolhida = input("Escolha uma opcao: ")
                try:
                    opcao_escolhida = int(opcao_escolhida)
                    if 0 < opcao_escolhida <= 7:
                        return opcao_escolhida
                    elif opcao_escolhida == 0:
                         print("Saindo do programa...")
                         exit()
                    else:
                         print("Opcao invalida. Digite um numero entre 0 e 7.")
                except ValueError:
                    print("Opcao invalida. Digite um numero valido.")

    @staticmethod
    def calcular(opcao_escolhida, num1, num2):
         while True:
          if opcao_escolhida == 1:
               return num1 + num2
          elif opcao_escolhida == 2:
               return num1 - num2
          elif opcao_escolhida == 3:
               return num1 * num2
          elif opcao_escolhida == 4:
               return num1 / num2
          elif opcao_escolhida == 5:
               return num1 ** num2
          elif opcao_escolhida == 6:
               return math.sqrt(num1 + num2)
          elif opcao_escolhida == 7:
               return num1 % num2
          elif opcao_escolhida == 0:
               exit()
          else:
               print("Opcao invalida.Tente novamente!!.")



while True:
    Calculadora.opcoes_do_menu()
    escolha = Calculadora.escolher_opcao()
    ru1 = int(input("Digite o PENULTIMO No do seu RU: "))
    ru2 = int(input("Digite o ULTIMO No do seu RU: "))
    resultado = Calculadora.calcular(escolha, ru1, ru2)
    print(f"Resultado:{resultado} ")
    print()
    pergunta = input("deseja continuar? [s]sim ou[n]nao: ").lower().strip()
    if pergunta == "s":
         pass
    else:
         print("Programa encerrado!!")
         exit()