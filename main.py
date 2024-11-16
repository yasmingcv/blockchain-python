from domain.block import Block
from domain.blockchain import Blockchain
import datetime as date

def main():
    #instancia a blockchain
    my_blockchain = Blockchain()
    
    selo = {
        "nome": "Selo verde",
        "descricao": "Selo verde para produtos sustentáveis",
        "empresa": "Empresa X",
    }
    
    selo2 = {
        "nome": "Selo verde",
        "descricao": "Selo verde para produtos sustentáveis",
        "empresa": "Empresa Y",
    }
    my_blockchain.add_block(Block(1, date.datetime.now(), selo, my_blockchain.chain[-1].hash))
    my_blockchain.add_block(Block(2, date.datetime.now(), selo2, my_blockchain.chain[-1].hash))
    print('Blockchain válida? ', my_blockchain.is_valid())
    chain = my_blockchain.chain
    my_blockchain.print_blockchain()
    
if __name__ == '__main__':
    main()