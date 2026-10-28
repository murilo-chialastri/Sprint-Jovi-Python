import time
import random

# variaveis
foto = ""               #Adição de foto
fotosSalvas = []  #Lista de fotos salvas
filtro = "Normal"        #Filtro
filtrosApi = {
        "Normal": "",
        "Preto e Branco": "grayscale",
        "Desfocado": "blur=4",
        "Preto e Branco + Desfocado": "grayscale&blur=4"
    }   #Opções de filtro

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

def salvarGaleriaTxt(galeria):

    arq = open('galeria.txt', 'w', encoding='UTF-8')
    for foto in galeria:

        linha = f"{foto[0]};{foto[1]};{foto[2]}\n"
        arq.write(linha)
    arq.close()

def carregarGaleriaTxt():
    galeria = []


    arq = open('galeria.txt', 'r', encoding='UTF-8')
    for linha in arq:
        linha_limpa = linha.strip()
        if linha_limpa != "":

            dados_foto = linha_limpa.split(';')
            galeria.append(dados_foto)
    arq.close()

    return galeria


def excluirFotoTxt(indiceApagar):
    arq = open('galeria.txt', 'r', encoding='UTF-8')
    linhas = arq.readlines()
    arq.close()


    if -1 <= indiceApagar < len(linhas):

        linhas.pop(indiceApagar)

        arq = open('galeria.txt', 'w', encoding='UTF-8')
        for linha in linhas:
            arq.write(linha)
        arq.close()


    else:
        print("\n Índice inválido!")

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



def tirarFotos(filtroAtivo):
    idFoto = random.randint(1, 1000)
    foto = input("nome da foto: ")
    if " " in foto:
        foto = foto.replace(" ","")


    idFiltro = filtrosApi[filtroAtivo]

    if filtroAtivo != "Normal":
        url = f"https://picsum.photos/id/{idFoto}/800/600?{idFiltro}"
    else:
        url = f"https://picsum.photos/id/{idFoto}/800/600"

    print("tirando foto.")
    print("tirando foto..")
    print("tirando foto...")
    print("clique!")
    fotosSalvas.append([foto,filtroAtivo,url])
    print(f"URL da foto gerada: {url}")
    salvarGaleriaTxt(fotosSalvas)


def modoFoco(filtroAtivo):
    """
    Cria uma foto e guarda na lista de fotos, porém adiciona '(4k) para simular uma foto com mais qualidade'

    """
    idFoto = random.randint(1, 1000)
    foto = input("nome da foto: ")
    if " " in foto:
        foto = foto.replace(" ", "")

    idFiltro = filtrosApi[filtroAtivo]

    if filtroAtivo != "Normal":
        url = f"https://picsum.photos/id/{idFoto}/800/600?{idFiltro}"
    else:
        url = f"https://picsum.photos/id/{idFoto}/800/600"

    print("focando.")
    time.sleep(0.3)
    print("focando..")
    time.sleep(0.3)
    print("focando...")
    time.sleep(0.3)
    print("clique!")
    fotosSalvas.append([foto, filtroAtivo, '(4k)', url])
    print(f"URL da foto gerada: {url}")
    salvarGaleriaTxt(fotosSalvas)


def camera(filtro):
    """
    Exibir um menu interativo com as opções de tirar foto, utilizando 3 outras funções dentro do while
    """

    while (True):
        op = input(menuFotos)
        if op == '1':
            tirarFotos(filtro)
        elif op == '2':
            modoFoco(filtro)
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
    for f in filtrosApi:  # percorre a lista de filtros para mostrar ao usuário
        print(f'({contador}) - {f}')
        contador += 1

def selecionarFiltro():
    """
    Seleciona um filtro que aparece nos dados da foto
    :return: modifica o nome do filtro
    """
    fil = "Normal"
    filtroNome = {
        "0": "Normal",
        "1": "Preto e Branco",
        "2": "Desfocado",
        "3": "Preto e Branco + Desfocado"
    }
    indice = int(input("Qual o número do filtro? "))
    if indice < len(filtrosApi):  # Verifica se o índice existe
        fil = filtroNome[str(indice)]

    else:
        print("Número inválido")
    filtro = fil
    return filtro


def filtros(filtro):
    """
    Menu interativo da sessão Filtros.
    Utiliza 4 funções dentro do while
    """

    while (True):

        op2 = input("""
        ╔═══════════════════════╗
        ║ Selecionar Filtro (1) ║
        ║ Sair              (2) ║
        ╚═══════════════════════╝
        :
        """)  # Opções de interação
        if op2 == '1':
            exibirFiltros()
            filtro = selecionarFiltro()

        elif op2 == '2':

            return filtro
        else:
            print("Opção inválida")


def mostrarGaleria(fotosSalvas):
    """
    Função para exibir a lista de fotos
    :return print com os dados das fotos e o índice na lista
    """
    if len(fotosSalvas) == 0:
        print("Galeria vazia!")
    else:
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





def apagarFotos(fotosSalvas):
    """
    Remove uma foto da lista pelo índice

    """
    verificaVazia = lambda: True if len(fotosSalvas) == 0 else False
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
                mostrarGaleria(fotosSalvas)
                i = int(input("Informe o id da foto"))  # Apaga foto selecionada pelo índice

                if i < len(fotosSalvas):  # Verifica se o índice existe
                    fotosSalvas.pop(i)
                    excluirFotoTxt(i)

                else:
                    print("Número inválido")
            elif arg == '2':
                if len(fotosSalvas) > 0:
                    fotosSalvas.pop()  # Apaga última foto
                    excluirFotoTxt(-1)
                else:
                    print("Opção inválida")
            elif arg == '3':
                break
            else:
                print("Opção inválida")


def galeria(fotosSalvas):
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
            mostrarGaleria(fotosSalvas)
        elif op2 == '2':
            apagarFotos(fotosSalvas)
        elif op2 == '3':
            break
        else:
            print("Opção inválida")



def executar_sistema():
    filtroC = filtro
    while (True):
        fotosSalvas = carregarGaleriaTxt()
        print(fotosSalvas)
        op = input(menu)  # Pronto

        #          TIRAR FOTO E GUARDAR NA GALERIA
        if op == '1':
            camera(filtroC) # Pronto

        #           FILTROS
        elif op == '2':
            filtroC = filtros(filtro)

        #         VER FOTOS
        elif op == '3':
            galeria(fotosSalvas)
        elif op == '0':
            desligar()
            break

        #         ERRO
        else:
            print("Opção inválida")