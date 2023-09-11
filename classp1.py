class Pessoa:

    def __init__(self, nome, idade, altura, peso, nascimento):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso =  peso
        self.nascimento = nascimento

    @property
    def nome(self):
        return self.nome
    
    @property
    def idade(self):
        return self.idade
    
    @property
    def altura(self):
        return self.altura

    @property
    def peso(self):
        return self.peso

    @property
    def nascimento(self):
        data = f'{self.nascimento[3:5]}/{self.nascimento[0:2]}/{self.nascimento[6:10]}'
        return data
