
class MenuRanking:
    def __init__(self,SistemaATP):
        self.sistema_atp = SistemaATP

    def exibir_menu(self):
        while True:
            print("\n===== MENU RANKING =====")
            print("1. Exibir ranking geral")
            print("2. Exibir ranking do jogador")
            print("3. Exibir ranking por superfície")
            print("4. Exibir estatísticas gerais")
            print("0. Voltar")
