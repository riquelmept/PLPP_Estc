from contas import Conta
from contapoupanca import ContaPoupanca


class ContaRemuneradaPoupanca(Conta, ContaPoupanca):
    def __init__(self, taxaremuneracao, clientes, numero, saldo):
        Conta.__init__(self,clientes,numero,saldo)
        Poupanca.__init__(self,taxaremuneracao)
        self.taxaremuneracao = taxaremuneracao
        
    def remuneraConta(Self):
        self.saldo += self.saldo * (self.taxaremuneracao/30)
        self.saldo -= self.taxaremuneracao