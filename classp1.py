class Pessoa:

    def __init__(self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso =  peso
    def apresentar(self):
        print(f'Muito prazer!Eu me chamo {self.nome} e tenho {self.idade} anos de idade.')
    def eh_maior(self,idade):
        if idade >= 18:
            print('Eu sou maior de idade!')
        elif idade <= 17:
            print('Eu sou menor de idade!')
    def imc(self):
        print(f'Você pesa {self.peso}')
    def imc_longo(self,peso):
        if peso<= 25.0:
            print('saldavel')
        elif peso<= 29.9:
            print('Você é acima so peso')
        elif peso<= 34.9:
            print('Tem obesidade 1')
        elif peso<= 39.9:
            print('Tem obesidade 2,severa')
        elif peso>= 40:
            print('Tem obesidade 3,mórbida')
    def comparar_idade(self,idade):
        if idade< 17:
            print('Você é mais novo(a) que eu!')
        elif idade== 17:
            print('Você tem a mesma idade que eu!')
        elif idade> 17:
            print('Você é mais velho(a) que eu!')

pessoa1=Pessoa('Gallye', '21', '1.78', '33.6')
pessoa1.apresentar()
pessoa1.eh_maior(idade=21)
pessoa1.imc()
pessoa1.imc_longo(peso=33.6)
pessoa1.comparar_idade(idade=21)

Herina=Pessoa('Herina', '17', '1.63', '27.9')
Herina.apresentar()
Herina.eh_maior(idade=17)
Herina.comparar_idade(idade=17)
Herina.imc_longo(peso=27.9)