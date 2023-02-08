class Item:
    def __init__(self, descricao, valor, quantidade):
        self.descricao = descricao
        self.valor = valor
        self.quantidade = quantidade

class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf


class Cupom:
    def __init__(self):
        self.itens = []
        self.valor_total = 0.0
        self.forma_pagamento = ""

    def adicionar_item(self, item):
        self.itens.append(item)
        self.valor_total += item.valor * item.quantidade

    def imprimir(self):
        print("CUPOM NÃO FISCAL")
        if hasattr(self, "cliente"):
            print("Cliente: {}".format(self.cliente.nome))
        else:
            print("Cliente: Consumidor")
        print("\nDescrição\tQuantidade\tValor\t\tSubtotal")
        for item in self.itens:
            subtotal = item.valor * item.quantidade
            print("{}\t\t{}\t\t{:.2f}\t\t{:.2f}".format(item.descricao, item.quantidade, item.valor, subtotal))
        print("\nValor Total\t\t\t\t\t\t{:.2f}".format(self.valor_total))
        print("\nForma de Pagamento: {}".format(self.forma_pagamento))

if input("Deseja realizar o cadastro de cliente (s/n)? ").lower() == 's':
    nome = input("Nome: ")
    cpf = input("CPF: ")
    cliente = Cliente(nome, cpf)
    cupom = Cupom()
    cupom.cliente = cliente
else:
    cupom = Cupom()

while True:
    descricao = input("Descrição do item (ou enter para encerrar): ")
    if descricao == '':
        break
    quantidade = int(input("Quantidade: "))
    valor = float(input("Valor: "))
    tem_desconto = input("Possui desconto (s/n)? ").lower() == 's'
    if tem_desconto:
        desconto = float(input("Desconto: "))
        valor -= desconto
    item = Item(descricao, valor, quantidade)
    cupom.adicionar_item(item)

cupom.forma_pagamento = input("Informe a forma de pagamento: ")
cupom.imprimir()
