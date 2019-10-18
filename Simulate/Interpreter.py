# python3
# -*- coding: utf-8 -*-
# @File    : Interpreter.py
# @Desc    :
# @Project : MIPSAssembler
# @Time    : 10/17/19 8:41 PM
# @Author  : Loopy
# @Contact : peter@mail.loopy.tech
# @License : CC BY-NC-SA 4.0 (subject to project license)

from Simulate.instructions import *
from Assemble.Preprocessor import Preprocessor
from Assemble.Assembler import Assembler
from misc.RegData import RegData


class Interpreter:
    Inst = {
        "lw": lw_,
        "sw": sw_,
        "add": add_,
        "addi": addi_,
        "and": and_,
        "beq": beq_,
        "j": j_,
        "or": or_,
        "sub": sub_,
        "sll": sll_,
        "slt": slt_,
        "slti": slti_,
        "srl": srl_,
    }
    label = {}
    hist_inst = []
    curr_inst = 0

    def __init__(self):
        raise SyntaxError("Interpreter can not be instantiate. Please use static method.")

    @classmethod
    def clear(cls):
        cls.label = {}
        cls.hist_inst = []
        cls.curr_inst = 0
        Memory.clear()
        Registers.clear()

    @classmethod
    def run_line(cls, inst_line):
        code_list, label = Preprocessor.prep_line(inst_line)
        if label is not None:
            cls.add_label(label)
        elif code_list is not None:
            if code_list[0] not in cls.Inst:
                raise ModuleNotFoundError(
                    'Unknown instruction "{}".'.format(code_list[0])
                )
            res = cls.Inst[code_list[0]](*code_list[1:])
            if res is not None:
                cls.jump_label(res)
            cls.hist_inst.append(code_list)
            cls.curr_inst += 1
        else:
            raise ValueError("God knows what happened")

    @classmethod
    def add_label(cls, label):
        cls.label[label] = len(cls.hist_inst)

    @classmethod
    def jump_label(cls, label):
        if label in cls.label.keys():
            cls.curr_inst = cls.hist_inst[cls.label[label]]
            count = 0
            while cls.curr_inst < len(cls.hist_inst):
                if count > 10000:
                    raise RecursionError("Infinity Loop with label:{}".format(label))
                cls.run_line(cls.hist_inst[cls.curr_inst])
                cls.hist_inst += 1
                count += 1
        else:
            raise ValueError("Trying to jump to an unknown label:{}".format(label))


if __name__ == "__main__":
    # Registers.reg_set("$s1",RegData("123"))
    # Registers.reg_set("$s4", RegData("234"))
    #
    # Interpreter.run_line("sw $s1,8($s2)")
    Interpreter.run_line("slti $s3, $s2, 1")

    print(Registers.reg_get("$s3"), "haha")

    Interpreter.run_line("slti $s3, $s2, 0")

    print(Registers.reg_get("$s3"), "xixi")

    # Interpreter.run_line("slti $s3, $s2, -1")
    #
    # print(Registers.reg_get("$s3"))

    # Interpreter.run_line("add $s2,$s1,$s4")
    #
    # print(Registers.reg_get("$s2"))