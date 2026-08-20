
import funcoesDeCamera


# variaveis





def executar_sistema():
    while (True):
        op = input(funcoesDeCamera.menu)  # Pronto

        #          TIRAR FOTO E GUARDAR NA GALERIA
        if op == '1':
            funcoesDeCamera.tirarFoto() # Pronto

        #           FILTROS
        elif op == '2':
            funcoesDeCamera.filtros()

        #         VER FOTOS
        elif op == '3':
            funcoesDeCamera.galeria()
        elif op == '0':
            funcoesDeCamera.desligar()
            break

        #         ERRO
        else:
            print("Opção inválida")