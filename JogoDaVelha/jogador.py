class JogoDaVelha:
    def __init__(self):
        self.tabuleiro = Tabuleiro()
        self.jogadores = []

    def adicionar_jogador(self, nome, simbolo):
        jogador = Jogador(nome, simbolo)
        self.jogadores.append(jogador)

    def jogar(self):
        turno = 0
        while True:
            self.tabuleiro.mostrar()
            jogador_atual = self.jogadores[turno % len(self.jogadores)]
            print(f"É a vez de {jogador_atual.nome} ({jogador_atual.simbolo})")
            linha = int(input("Escolha a linha (1, 2, 3): ")) - 1
            coluna = int(input("Escolha a coluna (1, 2, 3): ")) - 1
            
            if self.tabuleiro.marcar(linha, coluna, jogador_atual.simbolo):
                if self.tabuleiro.verificar_vitoria(jogador_atual.simbolo):
                    self.tabuleiro.mostrar()
                    print(f"{jogador_atual.nome} venceu!")
                    break
                if self.tabuleiro.cheio():
                    self.tabuleiro.mostrar()
                    print("Empate!")
                    break
                turno += 1
class Jogador:
    def __init__(self, nome, simbolo):
        self.nome = nome
        self.simbolo = simbolo  