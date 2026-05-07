import time
from os import remove

# variaveis
menu = """
        interface
+-------------------------+
|                  ______ |
|               2 |filtro||
|                  ------ |
|                         |
|  ______          ______ |
|1| foto |       3|salvos||
|  ------          ------ |
|            0            |
|        finalizar        |
+-------------------------+
Opção: """
foto = ""
op = -1
fotosSalvas = []
filtro = "auto*"
opcFiltro = ['auto*', 'sem filtro', 'cinza']

# Funções
def tirarFotos():
    foto = input("nome da foto: ")
    fotosSalvas.append(f'({filtro}){foto}')

def msgFotos():
    print("tirando foto.")
    time.sleep(0.3)
    print("tirando foto..")
    time.sleep(0.3)
    print("tirando foto...")
    time.sleep(0.3)

while(op != 0):
    op = int(input(menu))


    #          TIRAR FOTO E GUARDAR NA GALERIA
    if op == 1:
        while(True):
            msgFotos()
            tirarFotos()
            op2 = int(input("tirar outra foto? Sim (1) Não (2)"))
            if op2 == 2:
                break
            elif op2 == 1:
                continue
            else:
                print("Opção inválida")

    #           FILTROS
    elif op == 2:
        while(True):
            indf = 0
            for f in opcFiltro: #err
                indf = indf + 1
                print(f, indf- 1)
            op2 = int(input(f"Selecionar Filtro (1) adicionar filtro (2) apagar filtro (3) sair (4):  "))
            if op2 == 1:
                indice = int(input("Qual o número do filtro? "))
                if indice < len(opcFiltro):
                    filtro = opcFiltro[indice]
                else:
                    print("Número inválido")
            elif op2 == 2:
                add = input("Digite o nome do filtro: ")
                opcFiltro.append(add)
            elif op2 == 3:
                remove = int(input("Número do filtro que deseja remover: "))
                if remove < len(opcFiltro):
                    opcFiltro.pop(remove)
                else:
                    print("Número inválido")
            elif op2 == 4:
                break
            else:
                print("Opção inválida")
    #         VER FOTOS
    elif op == 3:
        ind = 0
        for fotos in fotosSalvas:
             ind = ind +1
             print(fotos, ind- 1)

    #         APAGAR FOTOS
        while(True):
            op2 = int(input("Selecionar foto para apagar (1) Apagar última foto (2) sair (3)"))
            if op2 == 1:
                indice = int(input("Qual o número da foto?"))
                if indice < len(fotosSalvas):
                    fotosSalvas.pop(indice)
                else:
                    print("Número inválido")
            elif op2 == 2:
                 fotosSalvas.pop()
            elif op2 == 3:
                break
            else:
                print("Opção inválida")

    #         ERRO
    else:
        print("Opção inválida")






# Adicionar lista que guarda nome das fotos e quantidade de fotos (1)
# opção mudar filtro para auto, sem , salvos (2)
# mostar lista de fotos com nome e quantidade (3)