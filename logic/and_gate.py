from .base_gate import BaseGate
class AndGate(BaseGate):
    '''
    AND GATE TRUTH TABLE:
    A B | OUT
    1 1 |  1
    1 0 |  0
    0 1 |  0
    0 0 |  0
    '''
    def __init__(self,name):
        super().__init__(name)
    
    def compute_output(self):
        if len(self.inputs) != 2:
            raise ValueError("there MUST be 2 input values for and gate")
        return int(self.inputs[0] and self.inputs[1])