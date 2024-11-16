# EcoWatt


Bem-vindo(a) ao repositório oficial do backend do projeto EcoWatt, solicitado para a **Global Solution: Green Energy**, como forma avaliativa na [FIAP](https://www.fiap.com.br/)!

Este repositório contém o código-fonte responsável pela gestão e atribuição de Selos Verdes, um reconhecimento destinado a empresas que alcançam metas de consumo sustentável de energia. A atribuição dos selos é realizada utilizando a tecnologia Blockchain, garantindo transparência, segurança e confiabilidade no processo.

## Tecnologias utilizadas

- Python
- Blockchain (simulação do funcionamento)

## Funcionalidades

- Cadastro de empresas e consumo mensal
- Cadastro da meta de consumo mensal em KwH
- Atribuição de selos verdes para empresas que atingirem a meta

## Instruções

Para rodar o projeto, siga os passos a seguir:

1. Faça um clone desse repositório em sua máquina
    ```
    git clone https://github.com/yasmingcv/blockchain-python
    ```

2. Entre na pasta do projeto
    ```
    cd blockchain-python
    ```

3. Instale o Python (caso não tenha)
    https://www.python.org/downloads/

3. Rode o projeto:
   ```
   py main.py
   ```

## Estrutura do projeto

```
├── blockchain.txt -> Guarda os blocos da Blockchain
├── main.py -> Arquivo principal
├── README.md -> Documentação
│
└───domain -> Pasta contendo as classes 
    ├── block.py -> Classe Block
    └── blockchain.py -> Classe Blockchain

```

## Exemplo de execução

```
----------------------------------------------------------------------
                         CADASTRO DE EMPRESAS
      Bem-vindo(a) ao cadastro de empresas. Digite 0 para sair.
----------------------------------------------------------------------
Digite o nome da empresa: FIAP
Digite o consumo mensal de KWh da empresa FIAP: 10000
----------------------------------------------------------------------
Digite o nome da empresa: IBM
Digite o consumo mensal de KWh da empresa IBM: 11000
----------------------------------------------------------------------
Digite o nome da empresa: Alura
Digite o consumo mensal de KWh da empresa Alura: 13000
----------------------------------------------------------------------
Digite o nome da empresa: 0


----------------------------------------------------------------------
                              BLOCKCHAIN
Index:  0
Timestamp:  2024-11-16 18:19:20.871710
Data:  Genesis Block
Hash:  34a2993a6e36859901714a2bff6fc500c8ed834ea34fbeac9fb9113c8292c3c4
Previous Hash:  0
----------------------------------------------------------------------
Index:  1
Timestamp:  2024-11-16 18:19:40.610276
Data:  {'empresa': 'FIAP', 'consumo_kwh': 10000.0, 'selo': 'verde'}
Hash:  7c3a3bbc0e55d6ad6f091c2fe2fabddbb2b54770a11e44b19e4d5240c9cc5d6f
Previous Hash:  34a2993a6e36859901714a2bff6fc500c8ed834ea34fbeac9fb9113c8292c3c4
----------------------------------------------------------------------
Index:  2
Timestamp:  2024-11-16 18:19:40.610276
Data:  {'empresa': 'IBM', 'consumo_kwh': 11000.0, 'selo': 'verde'}
Hash:  a72353bc300e11562b258653cc2c8c42caf47643d459dd980fc49bbf1cee5698
Previous Hash:  7c3a3bbc0e55d6ad6f091c2fe2fabddbb2b54770a11e44b19e4d5240c9cc5d6f
----------------------------------------------------------------------
```

## Integrantes

- David Murillo de Oliveira Soares (RM 559078)
- Yasmin Gonçalves Coelho (RM 559147)