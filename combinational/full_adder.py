from combinational.half_adder import HalfAdder
from logic.or_gate import OrGate

class FullAdder:
    def __init__(self,name):
        self.name = name
        self.half_adder1 = HalfAdder(name + "_HA1")
        self.half_adder2 = HalfAdder(name + "_HA2")
        self.or_gate = OrGate(name + "_OR")
        self.a = None
        self.b = None
        self.cin = None
    
    def add_inputs(self,a,b,cin):
        self.a = a
        self.b = b
        self.cin = cin

    def compute_outputs(self):
        '''
        returns a tuple in form: (sum, C-Out)
        '''
        
        # HalfAdder1: A,B
        self.half_adder1.add_inputs(self.a,self.b)
        s1,c1 = self.half_adder1.compute_outputs()

        # HalfAdder2: S1,Cin
        self.half_adder2.add_inputs(s1,self.cin)
        sum_,c2 = self.half_adder2.compute_outputs()

        #Carry Out (C-Out) C1 or C2
        self.or_gate.add_input(c1)
        self.or_gate.add_input(c2)
        cout = self.or_gate.compute_output()

        return sum_,cout