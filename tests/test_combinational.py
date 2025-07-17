import unittest
from combinational.half_adder import HalfAdder
from combinational.full_adder import FullAdder
from combinational.ripple_carry_adder_4bit import RippleCarryAdder4Bit

class TestCombinationals(unittest.TestCase):
    def test_half_adder(self):
        g = HalfAdder("HA1")
        g.add_inputs(0,0)
        self.assertEqual(g.compute_outputs(),(0,0))
        g = HalfAdder("HA2")
        g.add_inputs(0,1)
        self.assertEqual(g.compute_outputs(),(1,0))
        g = HalfAdder("HA3")
        g.add_inputs(1,0)
        self.assertEqual(g.compute_outputs(),(1,0))
        g = HalfAdder("HA4")
        g.add_inputs(1,1)
        self.assertEqual(g.compute_outputs(),(0,1))
    
    def test_full_adder(self):
        test_cases = [
            ((0,0,0), (0,0)),
            ((0,0,1), (1,0)),
            ((0,1,0), (1,0)),
            ((0,1,1), (0,1)),
            ((1,0,0), (1,0)),
            ((1,0,1), (0,1)),
            ((1,1,0), (0,1)),
            ((1,1,1), (1,1))
        ]

        for i, (inputs,expected) in enumerate(test_cases):
            with self.subTest(case=i, input_values=inputs):
                g = FullAdder(f"FA{i}")
                g.add_inputs(*inputs)
                self.assertEqual(g.compute_outputs(),expected)
        
    def test_ripple_carry_adder_4bit(self):
        test_cases = [
            (((0,0,0,0),(0,0,0,0),0),(0,0,0,0,0)),
            (((1,0,0,0),(1,0,0,0),0),(0,1,0,0,0)), #1+1=2
            (((1,1,1,1),(1,1,1,1),0),(0,1,1,1,1)), #15+15=30
            (((1,1,1,1),(1,1,1,1),1),(1,1,1,1,1)), #15+15+1=31
            (((0,1,0,1),(1,0,1,0),0),(1,1,1,1,0)), #10+5=15
        ]

        for i, ((a,b,cin),expected) in enumerate(test_cases):
            with self.subTest(case=i, a=a, b=b, cin=cin):
                rca = RippleCarryAdder4Bit(f"RCA{i}")
                rca.add_inputs(a,b,cin)
                self.assertEqual(rca.compute_outputs(),expected)

if __name__ == '__main__':
    unittest.main()