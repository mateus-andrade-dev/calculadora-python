# menu
def calculadao():
    print('----------calculadao--------')
    print()
    print('area_do_circulo (1)')
    print('conversor_dolar (2)')
    print('area_do_triangulo (3)')
    print('salario_por_hora (4)')
    print('encerrar programa (5)')


# calculadoras
def area_do_circulo():
    pi = 3.14
    raio = float(input('digite o raio para saber o resultado    '))
    area = pi * (raio * raio)
    print(' a area e igual a:', area)


def conversor_dolar():
    real = float(input('digite o valor em real que sera convertido   '))
    dolar = 5.13
    valor = real / dolar
    print('a quantidade obtida em dolar apos a conversa e:', valor)


def area_do_triangulo():
    base = float(input('base do triangulo    '))
    altura = float(input('altura do triangulo    '))
    area = base * altura / 2
    print('a area do triangulo e igual a:', area)


def salario_por_hora():
    salario = float(input('valor recebido por mes   '))
    hora = int(input('horas trabalhadas    '))
    rh = salario / hora
    print('voce recebe por hora:', rh)


# loop
while True:
    calculadao()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        area_do_circulo()

    elif opcao == "2":
        conversor_dolar()

    elif opcao == "3":
        area_do_triangulo()

    elif opcao == "4":
        salario_por_hora()

    elif opcao == "5":
        print("Encerrando o programa...")
        break
