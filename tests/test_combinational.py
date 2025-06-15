import unittest
from combinational.half_adder import HalfAdder
from combinational.full_adder import FullAdder

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

if __name__ == '__main__':
    unittest.main()