def soma(x, y):
    """Soma 2 números """
    return x + y


x = int(input('Digite um número somavel : '))
y = int(input('Digite um número somavel : '))

print(f'Ola ! A soma é de {soma(x,y)} !')


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def setName(self):
        return self.nome

    def setIdade(self):
        return self.idade

    def getNome(self):
        return self.nome

    def getIdade(self):
        return self.idade


n1 = Pessoa('Roger', 32)
print(n1.getIdade())