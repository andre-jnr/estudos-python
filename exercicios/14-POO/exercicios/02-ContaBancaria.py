class ContaBancaria:
  '''
    Cria uma conta bancária e permite fazer saques e depósitos
  '''
  def __init__(self, id, nome, saldo=0):
    self.id = id
    self.titular = nome
    self.saldo = saldo
    print(f'Conta criada com sucesso!')

  def depositar(self, valor):
    self.saldo += valor
    print(f'Deposito no valor de R${valor:,.2f}')

  def sacar(self, valor):
    if self.saldo >= valor:
      self.saldo -= valor
      print(f'Saque no valor de R${valor:,.2f} autorizado!')
    else:
      print(f'Saque no valor de R${valor:,.2f} não autorizado!')

  def __str__(self):
    return f'A conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo'
  

conta1 = ContaBancaria(112, 'Andre', 3000)
conta1.depositar(500)
conta1.sacar(2000)
conta1.sacar(2_000_000)
print(conta1)