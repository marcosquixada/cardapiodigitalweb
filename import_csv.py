import csv
from cadastro.models import *
from decimal import Decimal

def import_csv_(path):
	print "Iniciou"
	arq = csv.reader(open(path,'rb'), delimiter=";")
	i = 0
	for linha in arq:
		if i> 0:
			Execucao.objects.get_or_create(id_unidade_orc  = linha[1],
										id_fonte_recurso = linha[2],
										id_programa_trabalho = linha[3],
										id_pi = linha[4][1:],
										elemento_despesa = linha[5][1:len(linha[5])-2],
										vl_inicial = Decimal(linha[6].replace(",",".")),
										vl_empenhado = Decimal(linha[7].replace(",",".")),
										vl_atualizado = Decimal(linha[8].replace(",",".")),
										data_registro = "20"+linha[0][6:8] + "-" + linha[0][3:5] + "-" + linha[0][:2])
		i = i + 1
	print "Terminou"


def import_csv_unidade_orc(path):
	print "Iniciou"
	arq = csv.reader(open(path,'rb'), delimiter=";")
	i = 0
	for linha in arq:
		UnidadeOrcamentaria.objects.get_or_create(id_unidade_orc  = linha[0],
										ds_unidade_orc = linha[1],
										id_orgao = linha[2],
										nm_mnemonico = linha[3])
		i = i + 1
	print "Terminou"


def import_csv_orgao(path):
	print "Iniciou"
	arq = csv.reader(open(path,'rb'), delimiter=";")
	i = 0
	for linha in arq:
		Orgao.objects.get_or_create(id_orgao = linha[0],
										ds_orgao = linha[1],
										nm_mnemonico = linha[2])
		i = i + 1
	print "Terminou"


def import_csv_programa_trabalho(path):
	print "Iniciou"
	arq = csv.reader(open(path,'rb'), delimiter=";")
	i = 0
	for linha in arq:
		ProgramaTrabalho.objects.get_or_create(id_programa_trabalho = linha[0],
										ds_programa_trabalho = linha[1])
		i = i + 1
	print "Terminou"

def import_csv_fonte_recurso(path):
	print "Iniciou"
	arq = csv.reader(open(path,'rb'), delimiter=";")
	i = 0
	for linha in arq:
		FonteRecurso.objects.get_or_create(id_fonte_recurso = linha[0],
										ds_fonte_recurso = linha[1])
		i = i + 1
	print "Terminou"

def import_csv_localizacao(path):
	print "Iniciou"
	arq = csv.reader(open(path,'rb'), delimiter=";")
	i = 0
	for linha in arq:
		Localizacao.objects.get_or_create(id_localizacao = linha[0],
										ds_localizacao = linha[1])
		i = i + 1
	print "Terminou"


def import_csv_pi(path):
	print "Iniciou"
	arq = csv.reader(open(path,'rb'), delimiter=";")
	i = 0
	for linha in arq:
		print linha[4]
		print linha[5]
		PI.objects.get_or_create(id_pi = linha[0],
										id_unidade_orc = linha[1],
										id_programa_trabalho = linha[2],
										id_localizacao = linha[3],
										dt_prazo_inicial = linha[4][6:10] + "-" + linha[4][3:5] + "-" + linha[4][:2],
										dt_prazo_final = linha[5][6:10] + "-" + linha[5][3:5] + "-" + linha[5][:2])
		i = i + 1
	print "Terminou"