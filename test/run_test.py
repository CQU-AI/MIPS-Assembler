import unittest
from fengyong import Assembler
from fengyong import DisAssembler
from fengyong import Simulator
from fengyong import Registers
from fengyong import Stack
import random


class MyTestCase(unittest.TestCase):
    def test_assemble(self):
        Registers.clear()
        instructions = "j 10000\nadd $s0, $a1, $t7\nsw $s1, 10($s2)\n"
        machine_code = Assembler.encode(instructions)

        self.assertEqual("0x0800271000af8020ae51000a", machine_code.value_base(16))
        self.assertEqual(instructions, DisAssembler.decode(machine_code))

    def test_simulate(self):
        Registers.clear()
        path = "./test/asm/sample1.asm"
        Simulator.run_file(path)
        self.assertEqual(468968, Registers.reg_get("$s0"))

        
    def test_stack(self):
        Registers.clear()
        path = "./test/asm/stack.asm"
        Simulator.run_file(path)
        self.assertEqual(3, Registers.reg_get("$t4"))
        self.assertEqual(2, Registers.reg_get("$t5"))
        self.assertEqual(1, Registers.reg_get("$t6"))
        
        
    def test_instructions1(self):
        instructions1 = {
            "add": lambda x, y: x + y,
            "and": lambda x, y: x & y,
            "or": lambda x, y: x | y,
            "sub": lambda x, y: x - y,
            "xor": lambda x, y: x ^ y,
            "sllv": lambda x, y: x << y,
            "srlv": lambda x, y: x >> y,
        }
        for inst in instructions1.keys():
            for i in range(100):
                a, b = random.randint(1, 2 ** 20), random.randint(1, 2 ** 20)
                Simulator.run_line("addi $t0, $0, {}".format(a), False)
                Simulator.run_line("addi $t1, $0, {}".format(hex(b)), False)
                Simulator.run_line("{} $s0, $t1, $t0".format(inst), False)
                self.assertEqual(instructions1[inst](a, b), Registers.reg_get("$s0"))

    def test_instructions2(self):
        instructions2 = {
            "sll": lambda x: x << 5,
            "srl": lambda x: x >> 5,
        }
        for inst in instructions2.keys():
            for i in range(100):
                a = random.randint(1, 2 ** 20)
                Simulator.run_line("addi $t1, $0, {}".format(hex(a)), False)
                Simulator.run_line("{} $s0, $t1, 5".format(inst), False)
                self.assertEqual(instructions2[inst](a), Registers.reg_get("$s0"))

    def test_muldiv(self):
        Registers.clear()
        path = "./test/asm/muldiv.asm"
        Simulator.run_file(path)
        self.assertEqual((0x7f7f7f7f * 0xacdb) >> 32, Registers.reg_get("$t1"))
        self.assertEqual((0x7f7f7f7f * 0xacdb) & 0xffffffff, Registers.reg_get("$t2"))
        self.assertEqual((0x7f7f7f7f % 0xacdb), Registers.reg_get("$t3"))
        self.assertEqual((0x7f7f7f7f // 0xacdb), Registers.reg_get("$t4"))


if __name__ == "__main__":
    unittest.main()
