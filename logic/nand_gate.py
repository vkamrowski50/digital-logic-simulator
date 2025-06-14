from .base_gate import BaseGate
class NandGate(BaseGate):
    '''
    NAND GATE TRUTH TABLE:
    A B | OUT
    1 1 |  0
    1 0 |  1
    0 1 |  1
    0 0 |  1
    '''
    def __init__(self,name):
        super().__init__(name)
    
    def compute_output(self):
        if len(self.inputs) != 2:
            raise ValueError("there MUST be 2 input values for nand gate")
        return int(not(self.inputs[0] and self.inputs[1]))