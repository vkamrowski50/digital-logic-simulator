import unittest
from combinational.half_adder import HalfAdder

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
