from random import choice
from random import randint
import numpy as np
from time import sleep
import codecs


class Horst():
    code = 0x486f727374
    concepts = ["Algorithms", "Algebra", "Array", "Binary search", "Heap", "List", "Memory", "Overflow", "Sagmentation fault", "Stack", \
        "Dynamic programming", "Linear Programming", "Longest common subsequence", "Minimum spanning tree", "Object oriented", "Subset", \
        "Assembly", "Binary operations", "Constructor", "CNN", "Database", "Gradient descent", "Natural language processing", "Query", \
        "Approximation algorithm", "Bit", "Byte", "Computer", "Dictionary", "Greedy algorithm", "Linked list", "Loop", "Pointer", "String", \
        "3-D", "BUG", "Class", "CPU", "GPU", "Decorator", "Function", "Keyboard", "Matrix", "Max flow", "Screen", "Tensor", "Variable"]

    def __init__ (self):
        print(self.__repr__(), end = ' ')
        print("arrived.")

    def __eq__ (self, other):
        return other.lower() == "bug producer" or other.lower() == str(self).lower()

    def __ne__ (self, other):
        return not self.__eq__ (other)

    def __str__ (self):
        return self.code.to_bytes(5, 'big').decode("utf-8")

    def __repr__ (self):
        return self.__str__()

    def loop (self, buffer = []):
        buffer.append(np.random.randn(30, 30, 30))
        print(buffer)
        self.loop(buffer)

    def ask (self, keep = False):
        if keep:
            print("What is " + choice(self.concepts), end = "?"*20)
        else:
            print("What is " + choice(self.concepts), end = "?"*20+"\r")
        sleep(0.3)
        self.ask(keep)

    def bug_ignore(self, func, *args):
        try:
            func(*args)
        except Exception as e:
            print(e)

    def h_list(self, l):
        c = choice([1,2,3])
        if c == 1:
            return l[len(l)]
        else:
            c = choice([3.1415926, "string?", b'123'])
            return l[c]

    def h_dict(self, d, sHiT_lIke_vAriAblE_NAme = 1):
        while d.get(sHiT_lIke_vAriAblE_NAme) != None:
            sHiT_lIke_vAriAblE_NAme += 1
        return d[sHiT_lIke_vAriAblE_NAme]

    def h_import(self):
        import No_module_named

    def h_set(self, s):
        assert(type(s) == set)
        return s[0]

    def h_tuple(self, t):
        t[0] = 3
        return t

    def h_arithmetic(self, a, b, op):
        tensor = np.zeros([2,2,2,2])
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    for l in range(2):
                        operation = choice([lambda a,b:a+b, lambda a,b:a-b, lambda a,b:a*b, lambda a,b:a/b])
                        tensor[i, j, k, l] = operation(a, b)
        return tensor

    def h_sort(self, sequence, show = False):
        while sequence != sorted(sequence):
            sequence.append(sequence.pop(randint(0, len(sequence)-1)))
            if show:
                print(sequence)

    def h_depth(self):
        x = {}
        for i in range(1000000):
            x = {1:x}
        repr(x)
        



h = Horst()
h.h_crash()