import unittest
from fengyong import Assembler
from fengyong import DisAssembler
from fengyong import Simulator
from fengyong import Registers
import random



class MyTestCase(unittest.TestCase):
    def test_assemble(self):
        instructions = "j 10000\nadd $s0, $a1, $t7\nsw $s1, 10($s2)\n"
        machine_code = Assembler.encode(instructions)

        self.assertEqual("0x0800271000af8020ae51000a", machine_code.value_base(16))
        self.assertEqual(instructions, DisAssembler.decode(machine_code))

    def test_simulate(self):
        path = "../../sample/sample1/sample1.asm"
        Simulator.run_file(path)
        self.assertEqual(468968,Registers.reg_get("$s0"))

    def test_instructions(self):

        instructions = {
            "add":lambda x,y: x+y,
            "and":lambda x,y: x&y,
            "or" :lambda x,y: x|y,
            "sub":lambda x,y: x-y,
            "xor":lambda x,y: x^y,
            }
        for inst in instructions .keys():
            for i in range(100):
                a, b = random.randint(1, 2 ** 20), random.randint(1, 2 ** 20)
                Simulator.run_line("addi $t0, $0, {}".format(a), False)
                Simulator.run_line("addi $t1, $0, {}".format(hex(b)), False)

                Simulator.run_line("{} $s0, $t1, $t0".format(inst), False)
                self.assertEqual(instructions[inst](a, b), Registers.reg_get("$s0"))


    def test_muldiv(self):
        path = "./muldiv.asm"
        Simulator.run_file(path)
        self.assertEqual((0x7f7f7f7f * 0xacdb) >> 32,Registers.reg_get("$t1"))
        self.assertEqual((0x7f7f7f7f * 0xacdb) & 0xffffffff,Registers.reg_get("$t2"))
        self.assertEqual((0x7f7f7f7f % 0xacdb),Registers.reg_get("$t3"))
        self.assertEqual((0x7f7f7f7f // 0xacdb),Registers.reg_get("$t4"))


if __name__ == "__main__":
    unittest.main()
