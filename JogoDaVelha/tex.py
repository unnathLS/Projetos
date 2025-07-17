class Jogador:
    def __init__(self, simbolo, nome=""):
        self.simbolo = simbolo
        self.nome = nome if nome else f"Jogador {simbolo}"
    
    def obter_jogada(self):
        while True:
            # Pede a jogada e converte para maiúsculas imediatamente
            jogada_str = input(f"{self.nome} ({self.simbolo}), digite sua jogada (ex: 1A ou A1): ").upper()

            if len(jogada_str) == 2:
                char1, char2 = jogada_str[0], jogada_str[1]
                
                linha_indice = -1 # Inicializa com valor inválido
                coluna_indice = -1 # Inicializa com valor inválido

                try:
                    # Tenta converter o primeiro caractere para número (formato 1A)
                    if char1.isdigit() and char2.isalpha():
                        linha_indice = int(char1) - 1
                        coluna_indice = ord(char2) - ord('A')
                    # Tenta converter o segundo caractere para número (formato A1)
                    elif char1.isalpha() and char2.isdigit():
                        linha_indice = int(char2) - 1
                        coluna_indice = ord(char1) - ord('A')
                    else:
                        # Se não for nenhum dos formatos esperados (ex: 'AA' ou '11')
                        print("👉 Entrada inválida. A jogada deve conter um número (1-3) e uma letra (A-C).")
                        continue # Volta para o início do loop

                    # Valida se os índices estão dentro dos limites do tabuleiro (0 a 2)
                    if 0 <= linha_indice <= 2 and 0 <= coluna_indice <= 2:
                        return linha_indice, coluna_indice # Retorna e sai do loop
                    else:
                        print("👉 Posição fora dos limites. A linha deve ser 1, 2 ou 3 e a coluna A, B ou C. Tente novamente.")
                except (ValueError, TypeError):
                    # Captura erros se a conversão de tipo falhar
                    print("👉 Entrada inválida. Por favor, use o formato '1A', '2B', etc. (ex: 1A ou A1).")
            else:
                print("👉 Entrada inválida. Por favor, use o formato '1A', '2B', etc. (ex: 1A ou A1).")