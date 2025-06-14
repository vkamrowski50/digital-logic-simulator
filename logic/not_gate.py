from .base_gate import BaseGate
class NotGate(BaseGate):
    '''
    NOT GATE TRUTH TABLE:
    A | OUT
    1 |  0
    0 |  1
    '''
    def __init__(self,name):
        super().__init__(name)
    
    def compute_output(self):
        if len(self.inputs) != 1:
            raise ValueError("there MUST be 1 input value for not gate")
        return int(not self.inputs[0])