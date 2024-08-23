Gerador de Nomes Fictícios
Este repositório contém um script Python que gera 200 nomes fictícios em português do Brasil usando a biblioteca Faker. É uma ferramenta útil para criar dados fictícios para testes, desenvolvimento de software, ou qualquer outra aplicação que necessite de nomes aleatórios.

Funcionalidades
Geração de Nomes: Gera 200 nomes fictícios em português do Brasil.
Uso da Biblioteca Faker: Utiliza a biblioteca Faker para garantir a diversidade e realismo dos nomes gerados.
Simples e Eficiente: Código simples e fácil de entender, ideal para iniciantes e desenvolvedores experientes.
Como Usar
Instale a biblioteca Faker:
pip install faker

Clone este repositório:
git clone https://github.com/seu-usuario/gerador-nomes-ficticios.git
cd gerador-nomes-ficticios

Execute o script:
python gerar_nomes.py

Veja os nomes gerados:
O script imprimirá uma lista de 200 nomes fictícios no console.
Exemplo de Código
Python

import random
from faker import Faker  # Biblioteca para gerar nomes fictícios
from time import sleep
import time

fake = Faker("pt_BR")  # Configuração para nomes em português do Brasil
nomes_clientes = [fake.name() for _ in range(200)]

print(nomes_clientes)
Código gerado por IA. Examine e use com cuidado. Mais informações em perguntas frequentes.
Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests para melhorias e correções.
