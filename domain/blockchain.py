import datetime as date
from .block import Block

class Blockchain:
    #constructor
    #ao iniciar a blockchain, é criado o bloco genesis
    def __init__(self):
        #self.chain é uma lista de blocos
        self.chain = [self.create_genesis_block()]
    
    #função para criar o bloco genesis, o primeiro bloco da blockchain (não possui hash anterior)
    def create_genesis_block(self):
        return Block(0, date.datetime.now(), "Genesis Block", "0")

    #função para adicionar um novo bloco à blockchain
    def add_block(self, new_block: Block):
        new_block.previous_hash = self.chain[-1].hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)
    
    #função para verificar se a blockchain é válida
    def is_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
            return True
        
    def print_blockchain(self):
        print()
        print(20*'------')
        print('------------------BLOCKCHAIN------------------')
        for block in self.chain:
            print('Index: ', block.index)
            print('Timestamp: ', block.timestamp)
            print('Data: ', block.data)
            print('Hash: ', block.hash)
            print('Previous Hash: ', block.previous_hash)
            print(20*'------')
            
    def save_blockchain_to_file(self, file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write('\n')
            file.write(20*'------' + '\n')
            file.write('------------------BLOCKCHAIN------------------\n')
            for block in self.chain:
                file.write(f'Index: {block.index}\n')
                file.write(f'Timestamp: {block.timestamp}\n')
                file.write(f'Data: {block.data}\n')
                file.write(f'Hash: {block.hash}\n')
                file.write(f'Previous Hash: {block.previous_hash}\n')
                file.write(20*'------' + '\n')