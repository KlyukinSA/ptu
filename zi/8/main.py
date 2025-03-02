import hashlib
import time

class Block:
    def __init__(self, timestamp, data, previous_hash=''):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.get_hash()

    def get_hash(self):
        block_string = f"{self.timestamp}{self.data}{self.previous_hash}{self.nonce}".encode('utf-8')
        return hashlib.sha256(block_string).hexdigest()

    def mine(self, difficulty):
        prefix_str = '0' * difficulty
        while not self.hash.startswith(prefix_str):
            self.nonce += 1
            self.hash = self.get_hash()

class Blockchain:
    def __init__(self, difficulty=4):
        self.chain = []
        self.difficulty = difficulty
        self.create_block(timestamp=time.time(), data="Genesis Block")

    def create_block(self, timestamp, data):
        previous_hash = self.chain[-1].hash if self.chain else '0'
        new_block = Block(timestamp, data, previous_hash)
        new_block.mine(self.difficulty)
        self.chain.append(new_block)
        return new_block

    def get_last_block(self):
        return self.chain[-1] if self.chain else None

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if the current block's hash is correct
            if current_block.hash != current_block.get_hash():
                return False

            # Check if the previous block's hash is correct
            if current_block.previous_hash != previous_block.hash:
                return False

        return True

# Пример использования
if __name__ == "__main__":
    blockchain = Blockchain(difficulty=4)

    # Добавление блоков в цепочку
    blockchain.create_block(timestamp=time.time(), data="занять 100р")
    blockchain.create_block(timestamp=time.time(), data="отдать 100р")

    # Проверка валидности цепочки
    print("Is blockchain valid?", blockchain.is_chain_valid())

    # Вывод информации о каждом блоке
    for index, block in enumerate(blockchain.chain):
        print(f"Block {index}:")
        print(f"Data: {block.data}")
        print(f"Timestamp: {block.timestamp}")
        print(f"Nonce: {block.nonce}")
        print(f"Hash: {block.hash}")
        print(f"PrevHash: {block.previous_hash}\n")
