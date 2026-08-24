import time

# variaveis
foto = ""               #Adição de foto
fotosSalvas = []  #Lista de fotos salvas
filtro = ["auto*"]        #Filtro
opcFiltro = ['auto*', 'sem filtro', 'cinza']   #Opções de filtro

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

menuFotos ="""
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
    """
    Função para exibir uma mensagem ao desligar o programa
    """
    print("Desligando.")
    time.sleep(0.2)
    print("Desligando..")
    time.sleep(0.2)
    print("Desligando...")
    time.sleep(0.2)



def tirarFotos():
    """
    Cria uma foto e guarda na lista de fotos
    """
    foto = input("nome da foto: ")
    print("tirando foto.")
    print("tirando foto..")
    print("tirando foto...")
    print("clique!")
    fotosSalvas.append(f'({filtro}){foto}')



def modoFoco():
    """
    Cria uma foto e guarda na lista de fotos, porém adiciona '(4k) para simular uma foto com mais qualidade'

    """
    foto = input("nome da foto: ")
    print("focando.")
    time.sleep(0.3)
    print("focando..")
    time.sleep(0.3)
    print("focando...")
    time.sleep(0.3)
    print("clique!")
    fotosSalvas.append(f'({filtro[0]}) {foto} (4k)')

def tirarFoto():
    """
    Exibir um menu interativo com as opções de tirar foto, utilizando 3 outras funções dentro do while
    """
    while (True):
        op = input(menuFotos)
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
    """
    Função para exibir a lista de filtros
    :return print com os dados do filtro e o índice na lista
    """
    contador = 0
    for f in opcFiltro:  # percorre a lista de filtros para mostrar ao usuário
        contador = contador + 1
        print(f'{f} id ="{contador - 1}"')

def selecionarFiltro():
    """
    Seleciona um filtro que aparece nos dados da foto
    :return: modifica o nome do filtro
    """
    indice = int(input("Qual o número do filtro? "))
    if indice < len(opcFiltro):  # Verifica se o índice existe
        filtro[0] = opcFiltro[indice]

    else:
        print("Número inválido")

def addFiltro():
    """
    Pede um nome para o filtro novo e o adiciona na lista de filtros
    :return: adiciona o filtro na lista
    """
    add = input("Digite o nome do filtro: ")  # Cria e adiciona na lista de filtros
    opcFiltro.append(add)

def removeFiltro():
    """
    Remove um filtro da lista pelo índice

    """
    remove = int(input("Número do filtro que deseja remover: "))  # Remove filtro pelo índice
    if len(opcFiltro) == 0:
        print("nenhum filtro encontrado")
    elif remove < len(opcFiltro):  # Verifica se o índice existe
        opcFiltro.pop(remove)
    else:
        print("Número inválido")

def filtros():
    """
    Menu interativo da sessão Filtros.
    Utiliza 4 funções dentro do while
    """
    while (True):

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
            exibirFiltros()
            selecionarFiltro()
        elif op2 == '2':
            addFiltro()
        elif op2 == '3':
            exibirFiltros()
            removeFiltro()
        elif op2 == '4':
            break
        else:
            print("Opção inválida")


def mostrarGaleria():
    """
    Função para exibir a lista de fotos
    :return print com os dados das fotos e o índice na lista
    """
    ind = 0
    print("""
        ═══════════════════════
                GALERIA
        ═══════════════════════
        """)
    for fotos in fotosSalvas:  # percorre a lista de fotos para mostrar ao usuário
        ind = ind + 1

        print(f"""
        ║ {fotos} | ID ({ind - 1}) |║""")


verificaVazia = lambda: True if len(fotosSalvas) == 0 else False
verificaIndice = lambda i:  True if i < len(fotosSalvas) else False

def apagarFotos():
    """
    Remove uma foto da lista pelo índice

    """
    vazia = verificaVazia()
    if vazia == True:
        print("Galeria vazia")
    else:
        while True:
            arg = input("""
        ╔═════════════════════════════╗
        ║ Apagar Foto Selecionada (1) ║
        ║ Apagar Última Foto      (2) ║
        ║ Sair                    (3) ║                     
        ╚═════════════════════════════╝
            """)
            if arg == '1':
                mostrarGaleria()
                i = int(input("Informe o id da foto"))  # Apaga foto selecionada pelo índice
                indice = verificaIndice
                if indice == True:  # Verifica se o índice existe
                    fotosSalvas.pop(i)
                else:
                    print("Número inválido")
            elif arg == '2':(
                fotosSalvas.pop())  # Apaga última foto
            else:
                print("Opção inválida")


def galeria():
    """
    Menu interativo da sessão Galeria
    Utiliza 2 funções dentro do while
    """
    while (True):
        op2 = input("""
        ╔══════════════════════╗
        ║ Exibir Galeria   (1) ║
        ║ Apagar Fotos     (2) ║
        ║ Sair             (3) ║                     
        ╚══════════════════════╝
        """)  # Opções de interação
        if op2 == '1':
            mostrarGaleria()
        elif op2 == '2':
            apagarFotos()
        elif op2 == '3':
            break
        else:
            print("Opção inválida")



