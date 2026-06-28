import random
from models.Torneio import Torneio
from models.Jogador import Jogador
from models.Ranking import Ranking
from utils.enums import CategoriaTorneio, Superficie
from database.banco import Banco

class SistemaAtp:
    def __init__(self):
        self.jogadores = []
        self.ranking = Ranking()
        self.banco = Banco()
        self.banco.criar_tabelas()
        self.torneios = []
        self.carregar_jogadores()

    def cadastrar_jogador(self, nome, idade, nacionalidade, habilidade_saibro, habilidade_grama, habilidade_hard):
        if self.buscar_jogador(nome):
            print("Jogador já cadastrado.")
            return
        jogador = Jogador(nome, idade, nacionalidade, habilidade_saibro, habilidade_grama, habilidade_hard)
        self.jogadores.append(jogador)
        self.banco.salvar_jogador(jogador)
        self.ranking.adicionar_jogador(jogador)

    def buscar_jogador(self, nome):
        for jogador in self.jogadores:
            if jogador.nome == nome:
                return jogador
        return None
    
    def get_ranking_geral(self):
        self.ranking.atualizar_ranking()
        return self.ranking.mostrar_ranking()
    
    def gerar_jogadores_teste(self):
        nomes = [
            "Djokovic", "Alcaraz", "Sinner", "Medvedev",
            "Zverev", "Rune", "Rublev", "Tsitsipas"
        ]

        for nome in nomes:
            self.cadastrar_jogador(
                nome,
                random.randint(18, 38),
                "Teste",
                random.randint(70, 100),
                random.randint(70, 100),
                random.randint(70, 100)
            )
    
    def gerar_torneios_teste(self):
        torneios = [
            ("Australian Open", CategoriaTorneio.GRAND_SLAM, Superficie.HARD),
            ("Roland Garros", CategoriaTorneio.GRAND_SLAM, Superficie.SAIBRO),
            ("Wimbledon", CategoriaTorneio.GRAND_SLAM, Superficie.GRAMA),
            ("US Open", CategoriaTorneio.GRAND_SLAM, Superficie.HARD),
            ("Indian Wells", CategoriaTorneio.MASTERS_1000, Superficie.HARD),
            ("Monte Carlo", CategoriaTorneio.MASTERS_1000, Superficie.SAIBRO),
            ("Queen's", CategoriaTorneio.ATP_500, Superficie.GRAMA),
            ("Doha", CategoriaTorneio.ATP_250, Superficie.HARD)
        ]

        for nome, categoria, superficie in torneios:
            self.torneios.append(
                Torneio(nome, categoria, superficie)
            )

    def gerar_temporada_teste(self):
        self.gerar_jogadores_teste()
        self.gerar_torneios_teste()

        for torneio in self.torneios:
            for jogador in self.jogadores:
                torneio.adicionar_jogador(jogador)

    def iniciar_torneio(self, torneio):
        torneio.iniciar_torneio()
        self.atualizar_banco()
        self.ranking.atualizar_ranking()
        self.atualizar_banco()

    def criar_torneio(self, nome, categoria, superficie):
        torneio = Torneio(nome, categoria, superficie)
        self.torneios.append(torneio)
        return torneio
    
    def carregar_jogadores(self):
        jogadores_carregados = self.banco.carregar_jogadores()
        for linha in jogadores_carregados:
            jogador = Jogador(
                linha[1],  # nome
                linha[2],  # idade
                linha[3],  # nacionalidade
                linha[4],  # saibro
                linha[5],  # grama
                linha[6]   # hard
            )
            
            jogador.id = linha[0]  # id
            jogador.pontos = linha[7]  # pontos
            jogador.ranking = linha[8]  # ranking
            jogador.vitorias = linha[9]  # vitorias
            jogador.derrotas = linha[10]  # derrotas
            jogador.stamina = linha[11]  # stamina
            jogador.fisico = linha[12]  # fisico
            self.jogadores.append(jogador)
            self.ranking.adicionar_jogador(jogador)

    def atualizar_banco(self):
        for jogador in self.jogadores:
            self.banco.atualizar_jogador(jogador)