from abc import abstractmethod

class Nucleic_Acid(): 
    @abstractmethod
    def __add__ (self, other):
        pass

class DNA(Nucleic_Acid):
    def __init__(self, sequence):
        
        l = len(sequence)
        a = sequence.count('A', 0, l)
        t = sequence.count('T', 0, l)
        g = sequence.count('G', 0, l)
        c = sequence.count('C', 0, l)
        if l > (a+t+g+c): 
            raise Exception
        antisequence = ''
        for i in range(l): 
            if sequence[i] == 'A':
                antisequence += 'T'
            elif sequence[i] == 'T': 
                antisequence += 'A'
            elif sequence[i] == 'G': 
                antisequence += 'C'
            elif sequence[i] == 'C':
                antisequence += 'G'
        self.seq = [sequence, antisequence]
    def __str__ (self):
        return(str(self.seq))
    def __add__(self, other): 
        return(DNA(self.seq[0]+other.seq[0]))
    
class RNA(Nucleic_Acid): 
    def __init__(self, sequence): 
        l = len(sequence)
        a = sequence.count('A', 0, l)
        u = sequence.count('U', 0, l)
        g = sequence.count('G', 0, l)
        c = sequence.count('C', 0, l)
        if l > (a+u+g+c): 
            raise Exception
        self.seq = sequence
    def __str__ (self):
        return(self.seq)
    def __add__(self, other): 
        return(RNA(self.seq+other.seq))
    
kon = RNA('AAAAUUUUUGCGCGC')
onk = RNA('AUAUGA')
oo = DNA('TACTAC')
o = DNA('CACA')

print(kon+onk)
print(oo+o)


    