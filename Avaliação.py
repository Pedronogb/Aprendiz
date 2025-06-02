# Criar classe Cliente

class Cliente:
    def __init__(self, nome, cpf, renda_mensal, score_credito):
        self.nome = nome
        self.cpf = cpf
        self.renda_mensal = renda_mensal
        self.score_credito = score_credito

# Método verificar_credito()

    def verificar_credito(self):
        if self.renda_mensal >= 2000 and self.score_credito >= 600:
            print(f"Cliente {self.nome}: Crédito aprovado para concessão de compras.")
        else:
            print(f"Cliente {self.nome}: Crédito negado.")

# 3 Objetos em que: 1 seja aprovado, 1 reprovado por renda e 1 reprovado por score

cliente1 = Cliente("Gabriela", "197.755.897-13", 3000.00, 1000)
cliente2 = Cliente("João", "075.396.947-50", 1550.00, 850)
cliente3 = Cliente("Jubiscreuza", "285.714.967-38", 2600.00, 599)

cliente1.verificar_credito()
cliente2.verificar_credito()
cliente3.verificar_credito()

# Após a prova subir para o git e mandar o link do repositório no final para a professora