# https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-queues
# should be faster with deque
class Fila():
    def __init__(self):
        self.regular = []
        self.priority = []
        self.counter = 0
    
    def insert(self, x, priority):
        if priority:
            self.priority.append(x)
        else:
            self.regular.append(x)
    
    def remove(self):
        self.counter += 1
        if self.counter % 2 == 0: 
            if len(self.priority) > 0:
                return self.priority.pop(0)
        else:
            if len(self.regular) > 0:
                return self.regular.pop(0)

    
    def top(self, priority):
        if len(self.data) > 0:
            if priority:
                return self.priority[0]
            else:
                return self.regular[0]
        
    def empty(self, priority):
        if priority:
            return not self.priority > 0
        else:
            return not self.regular > 0

    def __repr__(self):
        return f"Regular: {str(self.regular)}; Prioridade: {str(self.priority)}"


# Fila

f = Fila()
f.insert(1, True)
f.insert(2, False)
f.insert(3, False)
f.insert(4, False)
f.insert(5, False)
f.insert(1, True)
f