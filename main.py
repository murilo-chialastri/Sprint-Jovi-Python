import time


# variaveis
menu = """
╔════════════════════════════════════╗
║                 ●            📶 🔋 ║
╠════════════════════════════════════╣
║                                    ║║
║             ╭──────╮               ║║
║             │  ◉◉  │               ║
║             │  ──  │               ║
║             ╰──────╯               ║║
║           SMART CAMERA             ║║
║                                    ║
║      ╭────────╮  ╭────────╮        ║
║      │   1    │  │   2    │        ║
║      │  FOTO  │  │FILTROS │        ║
║      ╰────────╯  ╰────────╯        ║
║                                    ║
║      ╭────────╮  ╭────────╮        ║
║      │   3    │  │   0    │        ║
║      │SALVOS  │  │  SAIR  │        ║
║      ╰────────╯  ╰────────╯        ║
║                                    ║
╠════════════════════════════════════╣
║         Selecione a opção          ║
╚════════════════════════════════════╝

➜ Opção: """
foto = ""               #Adição de foto
fotosSalvas = []        #Lista de fotos salvas
filtro = "auto*"        #Filtro
opcFiltro = ['auto*', 'sem filtro', 'cinza']   #Opções de filtro

# Funções
def tirarFotos():       #Cria a foto e guarda na lista
    foto = input("nome da foto: ")
    fotosSalvas.append(f'({filtro}){foto}')

def msgFotos():          #Mensagem da foto
    print("tirando foto.")
    time.sleep(0.3)
    print("tirando foto..")
    time.sleep(0.3)
    print("tirando foto...")
    time.sleep(0.3)


#              INÍCIO
while(True):
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
            for f in opcFiltro:     #percorre a lista de filtros para mostrar ao usuário
                indf = indf + 1
                print(f'{f} id ="{indf - 1}"')

            op2 = int(input("Selecionar Filtro (1) adicionar filtro (2) apagar filtro (3) sair (4):  "))  #Opções de interação
            if op2 == 1:
                indice = int(input("Qual o número do filtro? "))
                if indice < len(opcFiltro):    #Verifica se o índice existe
                    filtro = opcFiltro[indice]
                else:
                    print("Número inválido")
            elif op2 == 2:
                add = input("Digite o nome do filtro: ")   #Cria e adiciona na lista de filtros
                opcFiltro.append(add)
            elif op2 == 3:
                remove = int(input("Número do filtro que deseja remover: "))    #Remove filtro pelo índice
                if len(opcFiltro) == 0:
                    print("nenhum filtro encontrado")
                elif remove < len(opcFiltro) :     #Verifica se o índice existe
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
        for fotos in fotosSalvas:  #percorre a lista de fotos para mostrar ao usuário
             ind = ind +1
             print(f'{fotos} id ="{ind- 1}"')

    #         APAGAR FOTOS
        while(True):
            op2 = int(input("Selecionar foto para apagar (1) Apagar última foto (2) sair (3)")) #Opções de interação
            if op2 == 1:
                indice = int(input("Qual o número da foto?"))  #Apaga foto selecionada pelo índice
                if len(fotosSalvas) == 0:
                    print("galeria vázia")
                elif indice < len(fotosSalvas):   #Verifica se o índice existe
                    fotosSalvas.pop(indice)
                else:
                    print("Número inválido")
            elif op2 == 2:
                if len(fotosSalvas) == 0:
                    print("galeria vázia")
                else:
                 fotosSalvas.pop()  #Apaga última foto
            elif op2 == 3:
                break
            else:
                print("Opção inválida")
    elif op == 0:
        print("Desligando.")
        time.sleep(0.2)
        print("Desligando..")
        time.sleep(0.2)
        print("Desligando...")
        time.sleep(0.2)
        break

    #         ERRO
    else:
        print("Opção inválida")






