from combinational.full_adder import FullAdder

class RippleCarryAdder4Bit:
    def __init__(self,name):
        self.name = name
        self.fulladders = [FullAdder(f"{name}_FA{i}") for i in range(4)]
        self.a = None #a tuple of 4 bits. first digit is least significant
        self.b = None
        self.cin = None
    
    def add_inputs(self,a,b,cin):
        '''
        a and b are tuples in form(A/B1,A/B2,A/B3,A/B4)
        cin is either 1 or 0
        '''
        assert isinstance(a,tuple) and len(a) == 4
        assert isinstance(b,tuple) and len(b) == 4
        assert cin in (0,1)
        self.a = a
        self.b = b
        self.cin = cin

    def compute_outputs(self):
        '''
        returns a tuple in form(Sum0,Sum1,Sum2,Sum3,C-Out)
        Sum0 is least significant bit but is first in the tuple
        '''
        carry = self.cin
        result = []
        for i in range(4):
            self.fulladders[i].add_inputs(self.a[i],self.b[i],carry)
            s, carry = self.fulladders[i].compute_outputs()
            result.append(s)
        result.append(carry)
        return tuple(result)