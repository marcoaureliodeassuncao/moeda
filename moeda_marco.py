import sys
import json


def valor_moedas(vlr):

	try:
		vlr = float(vlr)
		lista_moedas = [1, 0.5, 0.25, 0.10, 0.05, 0.01]
		lista_aux = []
		coins = {"R$1,00":0,"R$0,50":0,"R$0,25":0,"R$0,10":0,"R$0,05":0, "R$0,01":0}

		if vlr == 0:
			return 0

		for moeda in lista_moedas:
			if moeda > vlr:
				lista_aux.append(0)
				pass
			else:
				lista_aux.append(vlr//moeda)
				vlr = vlr % moeda

		coins["R$1,00"] = lista_aux[0]
		coins["R$0,50"] = lista_aux[1]
		coins["R$0,25"] = lista_aux[2]
		coins["R$0,10"] = lista_aux[3]
		coins["R$0,05"] = lista_aux[4]
		coins["R$0,01"] = lista_aux[5]

		return json.dumps(coins)

	except ValueError:
		return 'Invalid input'


if __name__ == '__main__':

	print(valor_moedas(sys.argv[1]))
