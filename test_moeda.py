import unittest
from moeda_marco import valor_moedas
import json


valor_json = json.dumps({"R$1,00":200.0,"R$0,50":1.0,"R$0,25":1.0,"R$0,10":2.0,"R$0,05":0, "R$0,01":4.0})
valor_invalido = 'Invalid input'


class Tester(unittest.TestCase):

	def teste_valor_moeda(self):
		self.assertEqual(valor_moedas('200.99'), valor_json)
		pass

	def teste_valor_alfabeto(self):
		self.assertEqual(valor_moedas('oi'), valor_invalido)
		pass

	def teste_valor_caracter_especial(self):
		self.assertEqual(valor_moedas('@'), valor_invalido)
		pass

	def teste_valor_alfanumerico(self):
		self.assertEqual(valor_moedas('2a3fe'), valor_invalido)
		pass

	def teste_valor_alfanumerico_caracter_especial(self):
		self.assertEqual(valor_moedas('s@3fs'), valor_invalido)
		pass


if __name__ == '__main__':

	unittest.main()
