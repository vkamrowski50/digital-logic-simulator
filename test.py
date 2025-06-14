import unittest
from logic.and_gate import AndGate
from logic.or_gate import OrGate
from logic.not_gate import NotGate
from logic.nand_gate import NandGate
from logic.xor_gate import XorGate

class TestLogicGates(unittest.TestCase):
    def test_and_gate(self):
        g = AndGate("AND1")
        g.add_input(1)
        g.add_input(1)
        self.assertEqual(g.compute_output(),1)
        g = AndGate("AND2")
        g.add_input(1)
        g.add_input(0)
        self.assertEqual(g.compute_output(),0)
        g = AndGate("AND3")
        g.add_input(0)
        g.add_input(1)
        self.assertEqual(g.compute_output(),0)
        g = AndGate("AND4")
        g.add_input(0)
        g.add_input(0)
        self.assertEqual(g.compute_output(),0)
    
    def test_or_gate(self):
        g = OrGate("OR1")
        g.add_input(1)
        g.add_input(1)
        self.assertEqual(g.compute_output(),1)
        g = OrGate("OR2")
        g.add_input(1)
        g.add_input(0)
        self.assertEqual(g.compute_output(),1)
        g = OrGate("OR3")
        g.add_input(0)
        g.add_input(1)
        self.assertEqual(g.compute_output(),1)
        g = OrGate("OR4")
        g.add_input(0)
        g.add_input(0)
        self.assertEqual(g.compute_output(),0)

    def test_not_gate(self):
        g = NotGate("NOT1")
        g.add_input(1)
        self.assertEqual(g.compute_output(),0)
        g = NotGate("NOT2")
        g.add_input(0)
        self.assertEqual(g.compute_output(),1)

    def test_nand_gate(self):
        g = NandGate("NAND1")
        g.add_input(1)
        g.add_input(1)
        self.assertEqual(g.compute_output(),0)
        g = NandGate("NAND2")
        g.add_input(1)
        g.add_input(0)
        self.assertEqual(g.compute_output(),1)
        g = NandGate("NAND3")
        g.add_input(0)
        g.add_input(1)
        self.assertEqual(g.compute_output(),1)
        g = NandGate("NAND4")
        g.add_input(0)
        g.add_input(0)
        self.assertEqual(g.compute_output(),1)

    def test_xor_gate(self):
        g = XorGate("XOR1")
        g.add_input(1)
        g.add_input(1)
        self.assertEqual(g.compute_output(),0)
        g = XorGate("XOR2")
        g.add_input(1)
        g.add_input(0)
        self.assertEqual(g.compute_output(),1)
        g = XorGate("XOR3")
        g.add_input(0)
        g.add_input(1)
        self.assertEqual(g.compute_output(),1)
        g = XorGate("XOR4")
        g.add_input(0)
        g.add_input(0)
        self.assertEqual(g.compute_output(),0)

if __name__ == "__main__":
    unittest.main()