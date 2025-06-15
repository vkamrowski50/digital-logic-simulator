from logic.xor_gate import XorGate
from logic.and_gate import AndGate

class HalfAdder:
    def __init__(self,name):
        self.name = name
        self.xor_gate = XorGate(name + "_XOR")
        self.and_gate = AndGate(name + "_AND")
    
    def add_inputs(self,a,b):
        self.xor_gate.add_input(a)
        self.xor_gate.add_input(b)
        self.and_gate.add_input(a)
        self.and_gate.add_input(b)

    def compute_outputs(self):
        sum_output = self.xor_gate.compute_output()
        carry_output = self.and_gate.compute_output()
        return sum_output, carry_output
