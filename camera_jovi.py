
import funcoesDeCamera


# variaveis





def executar_sistema():
    while (True):
        op = int(input(funcoesDeCamera.menu()))  # Pronto

        #          TIRAR FOTO E GUARDAR NA GALERIA
        if op == 1:
            funcoesDeCamera.tirarFoto() # Pronto

        #           FILTROS
        elif op == 2:
            funcoesDeCamera.opcFiltro()

        #         VER FOTOS
        elif op == 3:
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
        elif op == 0:
            funcoesDeCamera.desligar()
            break

        #         ERRO
        else:
            print("Opção inválida")