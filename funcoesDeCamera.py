import time

# variaveis
foto = ""               #Adição de foto
fotosSalvas = []  #Lista de fotos salvas
# fotosQualidade = []
filtro = "auto*"        #Filtro
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
    fotosSalvas.append(f'({filtro}) {foto} (4k)')

def tirarFoto():
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

def filtros():
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


def mostrarGaleria():
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
    #         APAGAR FOTOS
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



