from domain.block import Block
from domain.blockchain import Blockchain
import datetime as date

def bubble_sort_empresas(empresas):
    #ordena a lista de empresas usando o Bubble Sort
    n = len(empresas)
    for i in range(n):
        for j in range(0, n-i-1):
            if empresas[j]['consumo_kwh'] > empresas[j+1]['consumo_kwh']:
                temp = empresas[j]
                empresas[j] = empresas[j+1]
                empresas[j+1] = temp

def main():
    #instancia a blockchain
    my_blockchain = Blockchain()
    
    meta_kwh = float(input('Digite a meta de consumo máximo mensal de KWh necessária para ganhar um selo verde: '))
    empresas = []
    
    while True:
        print(20*'------')
        print('------------------CADASTRO DE EMPRESAS------------------')
        print('Bem-vindo(a) ao cadastro de empresas. Digite 0 para sair.')
        print(20*'------')
        
        empresa = input('Digite o nome da empresa: ')  
        if empresa == '0':
            break
        consumo_kwh = float(input(f'Digite o consumo mensal de KWh da empresa {empresa}: '))
        empresas.append({
            "empresa": empresa,
            "consumo_kwh": consumo_kwh
        })
    
    #ordena a lista de empresas usando o Bubble Sort
    bubble_sort_empresas(empresas)
    
    #adiciona o selo verde nas empresas que atingiram a meta de consumo
    for empresa in empresas:
        if empresa['consumo_kwh'] <= meta_kwh:
            empresa['selo'] = 'verde'
            my_blockchain.add_block(Block(len(my_blockchain.chain), date.datetime.now(), empresa, my_blockchain.chain[-1].hash))
    
    my_blockchain.print_blockchain()
    print('Blockchain válida? ', my_blockchain.is_valid())

if __name__ == '__main__':
    main()
