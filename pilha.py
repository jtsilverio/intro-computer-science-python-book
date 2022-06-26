# https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-stacks
class Pilha():
    def __init__(self):
        self.data = []
        
    def push(self, x):
        self.data.append(x)
    
    def pop(self, x):
        if len(self.data) > 0:
            return self.data.pop(-1)
        
    def top(self):
        if len(self.data) > 0:
            return self.data[-1]
        
    def empty(self):
        return not len(self.data) > 0
    
    def __repr__(self):
        return str(self.data)
    
    def reverse(self):
        self.data.reverse()


# Conversao decima -> binário
def dec_to_bin(n):
    p = Pilha()
    while n > 0:
        resto = n % 2
        n = n // 2
        p.push(resto)
    
    p.reverse()
    return p

dec_to_bin(13)