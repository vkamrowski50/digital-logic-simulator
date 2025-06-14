class BaseGate:
    '''
    Base Gate for all gates.
    1 is equivalent to True, 0 is equivalent to False.
    '''
    def __init__(self,name):
        self.name = name
        self.inputs = []
    
    def compute_output(self):
        raise NotImplementedError("method compute_output() not implemented by gate subclasses")

    def add_input(self,input):
        if input not in (0,1):
            raise ValueError("input MUST be a 0 (false) or 1 (true)")
        self.inputs.append(input)