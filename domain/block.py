import hashlib

class Block: 
        #constructor
        def __init__(self, index, timestamp, data, previous_hash):
                self.index = index
                self.timestamp = timestamp
                self.data = data
                self.previous_hash = previous_hash
                self.hash = self.calculate_hash
                
        #função para calcular o hash
        def calculate_hash (self):
                sha = hashlib.sha256()
                #concatena as strings criptografadas para criar o hash
                sha.update(
                        str(self.index).encode('utf-8') +
                        str(self.timestamp).encode('utf-8') +
                        str(self.data).encode('utf-8') +
                        str(self.previous_hash).encode('utf-8'))
                return sha.hexdigest()