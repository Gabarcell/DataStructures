class Fila:
    def __init__(self):
        self.fila = []  #cria lista da fila
    def insert(self, n):
        self.fila.append(n) #adiciona elemento na fila
    def excluir(self):
        if not self.vazia(): #verifica se fila esta vazia
            return self.fila.pop(0) #retorna lista excluindo primeiro elemento
    def tamanho(self):
        return len(self.fila) #retorna tamanho da fila
    def vazia(self):
        return self.tamanho() == 0 #varifica quantos elementos na fila

fila = Fila()

fila.insert(1)
fila.insert(2)
fila.insert(3)
print(fila.excluir())
print(fila.excluir())
print(fila.excluir())
print(fila.vazia())