import random

class Palavra:
    def __init__(self, lista_palavras):
        self.lista_palavras = lista_palavras
        self.palavra = random.choice(self.lista_palavras).upper()

    def get_palavra(self):
        return self.palavra

class Forca:
    def __init__(self, palavra):
        self.palavra = palavra
        self.letras_corretas = set()
        self.letras_erradas = set()
        self.tentativas_max = 6

    def mostrar_palavra(self):
        # Mostra o progresso (_ _ T _ _)
        return " ".join([letra if letra in self.letras_corretas else "_" for letra in self.palavra])

    def tentar_letra(self, letra):
        letra = letra.upper()
        if letra in self.palavra:
            self.letras_corretas.add(letra)
            return True
        else:
            self.letras_erradas.add(letra)
            return False

    def tentativas_restantes(self):
        return self.tentativas_max - len(self.letras_erradas)

    def venceu(self):
        return all(letra in self.letras_corretas for letra in self.palavra)

    def perdeu(self):
        return self.tentativas_restantes() <= 0

class JogoDaForca:
    def __init__(self, lista_palavras):
        self.palavra_obj = Palavra(lista_palavras)
        self.forca = Forca(self.palavra_obj.get_palavra())

    def jogar(self):
        print("Bem-vindo ao Jogo da Forca!")
        while not self.forca.venceu() and not self.forca.perdeu():
            print(f"Palavra: {self.forca.mostrar_palavra()}")
            print(f"Tentativas restantes: {self.forca.tentativas_restantes()}")
            print(f"Letras erradas: {', '.join(self.forca.letras_erradas)}")
            letra = input("Digite uma letra: ").strip().upper()

            if len(letra) != 1 or not letra.isalpha():
                print("Digite apenas uma letra.")
                continue
            if letra in self.forca.letras_corretas or letra in self.forca.letras_erradas:
                print("Você já tentou essa letra.")
                continue
            acertou = self.forca.tentar_letra(letra)
            print("Você acertou!" if acertou else "Letra errada.")
        if self.forca.venceu():
            print(f"Parabéns! Você venceu! A palavra era: {self.forca.palavra}")
        else:
            print(f"Você perdeu! A palavra era: {self.forca.palavra}")

if __name__ == "__main__":
    palavras = ["python", "computador", "programacao", "desenvolvimento", "algoritmo"]
    jogo = JogoDaForca(palavras)
    jogo.jogar()