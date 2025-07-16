from combinational.full_adder import FullAdder

class RippleCarryAdder4Bit:
    def __init__(self,name):
        self.name = name
        self.FullAdder1 = FullAdder(name+"_FA1")
        self.FullAdder2 = FullAdder(name+"_FA2")
        self.FullAdder3 = FullAdder(name+"_FA3")
        self.FullAdder4 = FullAdder(name+"_FA4")
        self.a = None #a tuple of 4 0s/1s. first digit is least significant
        self.b = None
        self.cin = None
    
    def add_inputs(self,a,b,cin):
        '''
        a and b are tuples in form(A/B1,A/B2,A/B3,A/B4)
        cin is either 1 or 0
        '''
        self.a = a
        self.b = b
        self.cin = cin

    def compute_outputs(self):
        '''
        returns a tuple in form(Sum0,Sum1,Sum2,Sum3,Sum4,C-Out)
        Sum0 is least significant bit but is first in the tuple
        '''
        FullAdder1.add_inputs(self.a[0],self.b[0],cin)
        sum0, c1 = FullAdder1.compute_outputs()
        FullAdder2.add_inputs(self.a[1],self.b[1],c1)
        sum1, c2 = FullAdder2.compute_outputs()
        FullAdder3.add_inputs(self.a[2],self.b[2],c2)
        sum2, c3 = FullAdder3.compute_outputs()
        FullAdder4.add_inputs(self.a[3],self.b[3],c3)
        sum3, c4 = FullAdder4.compute_outputs()
        return sum0,sum1,sum2,sum3,c4