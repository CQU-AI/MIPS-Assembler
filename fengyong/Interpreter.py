from .instructions import *
from .Preprocessor import Preprocessor
from .RegData import RegData


class Interpreter:
    Inst = {
        "add": add_,
        "addi": addi_,
        "and": and_,
        "andi": andi_,
        "beq": beq_,
        "bgez": bgez_,
        "bgtz": bgtz_,
        "blez": blez_,
        "bltz": bltz_,
        "div": div_,
        "j": j_,
        "lui": lui_,
        "lw": lw_,
        "mfhi": mfhi_,
        "mflo": mflo_,
        "mult": mult_,
        "noop": noop_,
        "or": or_,
        "ori": ori_,
        "sll": sll_,
        "sllv": sllv_,
        "slt": slt_,
        "slti": slti_,
        "srl": srl_,
        "srlv": srlv_,
        "sub": sub_,
        "sw": sw_,
        "xor": xor_,
        "xori": xori_,
    }
    label = {}
    hist_inst = []
    curr_inst = 0

    def __init__(self):
        raise SyntaxError(
            "Interpreter can not be instantiate. Please use class method."
        )

    @classmethod
    def clear(cls):
        cls.label = {}
        cls.hist_inst = []
        cls.curr_inst = 0
        Memory.clear()
        Registers.clear()

    @classmethod
    def run_line(cls, inst_line, save_hist=True):
        code_list, label = Preprocessor.prep_line(inst_line)
        if label is not None:
            cls.add_label(label)
        if code_list is not None:
            if code_list[0] not in cls.Inst:
                raise ModuleNotFoundError(
                    'Unknown instruction "{}".'.format(code_list[0])
                )
            res = cls.Inst[code_list[0]](*code_list[1:])
            if res is not None:
                cls.jump_label(res)
            if save_hist:
                cls.hist_inst.append(inst_line)
            cls.curr_inst += 1

    @classmethod
    def add_label(cls, label):
        cls.label[label] = len(cls.hist_inst)

    @classmethod
    def jump_label(cls, label):
        if label in cls.label.keys():
            cls.curr_inst = int(cls.label[label]) - 1
        else:
            raise ValueError("Trying to jump to an unknown label:{}".format(label))


if __name__ == "__main__":
    # Registers.reg_set("$s1",RegData("123"))
    # Registers.reg_set("$s4", RegData("234"))
    #
    # Interpreter.run_line("sw $s1,8($s2)")
    Registers.reg_set("$s3", RegData(2024, 32))
    Interpreter.run_line("add $t0, $s3,$0")

    print(Registers.reg_get("$t0"), "haha")

    print(Registers.reg_get("$s3"), "xixi")

    # Interpreter.run_line("slti $s3, $s2, -1")
    #
    # print(Registers.reg_get("$s3"))

    # Interpreter.run_line("add $s2,$s1,$s4")
    #
    # print(Registers.reg_get("$s2"))
