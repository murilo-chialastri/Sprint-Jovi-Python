import time

# variaveis
foto = ""               #Adição de foto
fotosSalvas = []  #Lista de fotos salvas
fotosQualidade = []
filtro = "auto*"        #Filtro
opcFiltro = ['auto*', 'sem filtro', 'cinza']   #Opções de filtro

def menu():
    return """
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

def menuFotos():
    return """
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
    ║        ╭──────────────────╮        ║                        
    ║        │  FOTO PADRÃO (1) │        ║
    ║        ╰──────────────────╯        ║
    ║        ╭──────────────────╮        ║                        
    ║        │   MODO FOCO  (2) │        ║
    ║        ╰──────────────────╯        ║
    ║        ╭──────────────────╮        ║                        
    ║        │    VOLTAR    (3) │        
    ║        ╰──────────────────╯        ║
    ╠════════════════════════════════════╣
    ║         Selecione a opção          ║
    ╚════════════════════════════════════╝

    ➜ Opção: """
def desligar ():
    print("Desligando.")
    time.sleep(0.2)
    print("Desligando..")
    time.sleep(0.2)
    print("Desligando...")
    time.sleep(0.2)


def tirarFotos():       #Cria a foto e guarda na lista
    foto = input("nome da foto: ")
    print("tirando foto.")
    print("tirando foto..")
    print("tirando foto...")
    print("clique!")
    fotosSalvas.append(f'({filtro}){foto}')



def modoFoco():
    foto = input("nome da foto: ")
    print("focando.")
    time.sleep(0.3)
    print("focando..")
    time.sleep(0.3)
    print("focando...")
    time.sleep(0.3)
    print("clique!")
    fotosQualidade.append(f'({filtro}) {foto} (4k)')

def tirarFoto():
    while (True):
        op = input(menuFotos())
        if op == '1':
            tirarFotos()
        elif op == '2':
            modoFoco()
        elif op == '3':
            break
        else:
            print("Opção inválida")
            continue
        op2 = int(input("""
        ╔═══════════════════╗
        ║ Tirar outra foto? ║ 
        ║                   ║
        ║  Sim (1)  Não (2) ║
        ╚═══════════════════╝
        :
        """))
        if op2 == 2:
            break
        elif op2 == 1:
            continue
        else:
            print("Opção inválida")
            continue


def exibirFiltros():
     indf = 0
     for f in opcFiltro:  # percorre a lista de filtros para mostrar ao usuário
        indf = indf + 1
        print(f'{f} id ="{indf - 1}"')

def selecionarFiltro():
    indice = int(input("Qual o número do filtro? "))
    if indice < len(opcFiltro):  # Verifica se o índice existe
        filtro = opcFiltro[indice]
    else:
        print("Número inválido")

def addFiltro():
    add = input("Digite o nome do filtro: ")  # Cria e adiciona na lista de filtros
    opcFiltro.append(add)

def removeFiltro():
    remove = int(input("Número do filtro que deseja remover: "))  # Remove filtro pelo índice
    if len(opcFiltro) == 0:
        print("nenhum filtro encontrado")
    elif remove < len(opcFiltro):  # Verifica se o índice existe
        opcFiltro.pop(remove)
    else:
        print("Número inválido")

def opcFiltros():
    while (True):
        exibirFiltros()

        op2 = input("""
        ╔═══════════════════════╗
        ║ Selecionar Filtro (1) ║
        ║ Adicionar Filtro  (2) ║
        ║ Remover Filtro    (3) ║
        ║ Sair              (4) ║
        ╚═══════════════════════╝
        :
        """)  # Opções de interação
        if op2 == '1':
            selecionarFiltro()
        elif op2 == '2':
            addFiltro()
        elif op2 == '3':
           removeFiltro()
        elif op2 == '4':
            break
        else:
            print("Opção inválida")

def galeria():
    ind = 0
    for fotos in fotosSalvas:  # percorre a lista de fotos para mostrar ao usuário
        ind = ind + 1
        print(f'{fotos} id ="{ind - 1}"')

    #         APAGAR FOTOS
    while (True):
        op2 = int(
            input("Selecionar foto para apagar (1) Apagar última foto (2) sair (3)"))  # Opções de interação
        if op2 == 1:
            indice = int(input("Qual o número da foto?"))  # Apaga foto selecionada pelo índice
            if len(fotosSalvas) == 0:
                print("galeria vázia")
            elif indice < len(fotosSalvas):  # Verifica se o índice existe
                fotosSalvas.pop(indice)
            else:
                print("Número inválido")
        elif op2 == 2:
            if len(fotosSalvas) == 0:
                print("galeria vázia")
            else:
                fotosSalvas.pop()  # Apaga última foto
        elif op2 == 3:
            break
        else:
            print("Opção inválida")



