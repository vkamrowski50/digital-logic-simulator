from combinational.ripple_carry_adder_4bit import RippleCarryAdder4Bit

class RippleCarryAdder8Bit:
    def __init__(self,name):
        self.name = name
        self.rca4bits = [RippleCarryAdder4Bit(f"{name}+_RCA4B{i}") for i in range(2)]
        self.a = None
        self.b = None
        self.cin = None
    
    def add_input(self,a,b,cin):
        '''
        a and b are tuples in form(A/B1,A/B2,A/B3,A/B4,...)
        cin is either 1 or 0
        '''
        assert isinstance(a,tuple) and len(a) == 8
        assert isinstance(b,tuple) and len(b) == 8
        assert cin in (0,1)
        self.a = a
        self.b = b
        self.cin = cin
    
    def compute_outputs(self):
        '''
        returns a tuple in form(Sum0,Sum1,Sum2,...,Sum7,C-Out)
        Sum0 is least significant bit but is first in the tuple
        '''
        carry = self.cin
        result = []
        self.rca4bits[0].add_inputs(self.a[:4],self.b[:4],self.cin)
        
        