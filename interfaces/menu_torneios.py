from models.Torneio import Torneio


class MenuTorneios:
    def __init__(self, sistemaATP):
        self.sistema_atp = sistemaATP

    def exibir_menu(self):
        while True:
            print("\n===== MENU TORNEIOS =====")
            print("1. Criar torneio")
            print("2. Listar torneios")
            print("3. Adicionar jogador a torneio")
            print("4. Iniciar torneio")
            print("0. Voltar")
            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                self.criar_torneio()
            elif opcao == "2":
                self.listar_torneios()
            elif opcao == "3":
                self.adicionar_jogador_torneio()
            elif opcao == "4":
                self.iniciar_torneio()
            elif opcao == "0":
                break
            else:
                print("Opção inválida. Tente novamente.")

    def criar_torneio(self):
        nome = input("Digite o nome do torneio: ")
        superficie = input("Digite a superfície do torneio (saibro, grama, hard): ")
        categoria = input("Digite a categoria do torneio: ")
        if superficie == "saibro":
            torneio = Torneio(nome, superficie, categoria)
            self.sistema_atp.torneios.append(torneio)
            print(f"Torneio {nome} criado com sucesso!")
        if superficie == "grama":
            torneio = Torneio(nome, superficie, categoria)
            self.sistema_atp.torneios.append(torneio)
            print(f"Torneio {nome} criado com sucesso!")
        if superficie == "hard":
            torneio = Torneio(nome, superficie, categoria)
            self.sistema_atp.torneios.append(torneio)
            print(f"Torneio {nome} criado com sucesso!")
        else:
            print("Superfície inválida. Tente novamente.")
        