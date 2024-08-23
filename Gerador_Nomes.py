# Gerar 200 nomes fictícios
import random
from faker import Faker  # Biblioteca para gerar nomes fictícios
from time import sleep
import time

fake = Faker("pt_BR")  # Configuração para nomes em português do Brasil
nomes_clientes = [fake.name() for _ in range(200)]

print(nomes_clientes)
