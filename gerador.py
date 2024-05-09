import csv
from faker import Faker

fake = Faker('pt_BR')
nome_arquivo = 'dados.csv'
cabecalho = ['nome', 'email, 'endereco', 'telefone']

with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as csvfile:
	escritor = csv.witer(csvfile)
	escritor.writerow(cabecalho)
	
	for _ in range:
		nome = fake.name()
		email = fake.email()
		endereco = fake.address().replace('\n', ',')
		telefone = fake.phone_number()

		escritor.writerow(nome, email, endereco, telefone)
