class Tabuleiro:
    def __init__(self):
        self.tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]

    def mostrar(self):
        print("   A   B   C")
        for i in range(3):
            linha = " | ".join(self.tabuleiro[i])
            print(f"{i + 1}  {linha}")
            if i < 2:
                print("  ---+---+---")

    def marcar(self, linha, coluna, simbolo):
        if self.tabuleiro[linha][coluna] == " ":
            self.tabuleiro[linha][coluna] = simbolo
            return True
        else:
            print("Posição já marcada. Tente novamente.")
            return False

    def verificar_vitoria(self, simbolo):
        for i in range(3):
            if all(self.tabuleiro[i][j] == simbolo for j in range(3)):
                return True
            if all(self.tabuleiro[j][i] == simbolo for j in range(3)):
                return True
        if all(self.tabuleiro[i][i] == simbolo for i in range(3)):
            return True
        if all(self.tabuleiro[i][2 - i] == simbolo for i in range(3)):
            return True
        return False

    def cheio(self):
        return all(self.tabuleiro[i][j] != " " for i in range(3) for j in range(3))



class Jogador:
    def __init__(self, simbolo, nome=""):
        self.simbolo = simbolo
        self.nome = nome if nome else f"Jogador {simbolo}"
    
    def obter_jogada(self):
        while True:
            jogada_str = input(f"{self.nome} ({self.simbolo}), digite sua jogada (ex: 1A ou A1): ").upper()

            if len(jogada_str) == 2:
                char1, char2 = jogada_str[0], jogada_str[1]
                try:
                    if char1.isdigit() and char2.isalpha():
                        linha = int(char1) - 1
                        coluna = ord(char2) - ord('A')
                    elif char1.isalpha() and char2.isdigit():
                        linha = int(char2) - 1
                        coluna = ord(char1) - ord('A')
                    else:
                        print("👉 Entrada inválida. A jogada deve conter um número (1-3) e uma letra (A-C).")
                        continue 
                    if 0 <= linha < 3 and 0 <= coluna < 3:
                        return linha, coluna
                    else:
                        print("👉 Posição fora dos limites. A linha deve ser 1, 2 ou 3 e a coluna A, B ou C. Tente novamente.")
                except ValueError:
                        # Captura erro se a linha_char não for um número
                    print("👉 Entrada inválida. Por favor, use o formato '1A', '2B', etc. (ex: 1A para a primeira casa).")
            else:
                print("👉 Entrada inválida. Por favor, use o formato '1A', '2B', etc. (ex: 1A para a primeira casa).")


class JogoDaVelha:
    def __init__(self):
        self.tabuleiro = Tabuleiro()
        self.jogador_x = Jogador("X", "Jogador 1")
        self.jogador_o = Jogador("O", "Jogador 2")
        self.jogador_atual = self.jogador_x
        self.rodada = 0
        self.jogo_terminado = False

    def iniciar_jogo(self):

         print("🎮 Bem-vindo ao Jogo da Velha!")
         print("Digite a posição da sua jogada (ex: A1 para a primeira coluna da primeira linha).") 
         
         while not self.jogo_terminado:
            self.tabuleiro.mostrar()
            linha, coluna = self.jogador_atual.obter_jogada()

            if self.tabuleiro.marcar(linha , coluna, self.jogador_atual.simbolo):
                self.rodada += 1
                if self.tabuleiro.verificar_vitoria(self.jogador_atual.simbolo):
                    self.tabuleiro.mostrar()
                    print(f"🎉 Parabéns! O {self.jogador_atual.nome} ({self.jogador_atual.simbolo}) venceu!")
                    self.jogo_terminado = True
                # Verifica empate
                elif self.tabuleiro.cheio(): # Usando o nome do seu método atual
                    self.tabuleiro.mostrar()
                    print("🤝 O jogo empatou!")
                    self.jogo_terminado = True
                else:
                    # Troca o jogador
                    self.jogador_atual = self.jogador_o if self.jogador_atual == self.jogador_x else self.jogador_x
            # Se a jogada não for válida (marcar retornou False), o loop continua para o mesmo jogador.

# Finalmente, para rodar o jogo:
if __name__ == "__main__":
    jogo = JogoDaVelha()
    jogo.iniciar_jogo()





