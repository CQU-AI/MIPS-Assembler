from .RegData import RegData
from .static import *


class DisAssembler:
    def __init__(self):
        raise SyntaxError("DisAssembler can not instance, please use static method")

    @staticmethod
    def decode(codes):
        instructions = ""
        if isinstance(codes, RegData):
            codes = codes.bin
        else:
            codes = RegData(codes).bin

        while len(codes) >= 32:
            code = RegData("0b" + codes[:32], 32)
            codes = codes[32:]
            if code.bin[:6] == "000000":
                instructions += DisAssembler.r_decode(code) + "\n"
            elif RegData("0b" + code.bin[:6]).hash in I_index_to_inst.keys():
                instructions += DisAssembler.i_decode(code) + "\n"
            elif RegData("0b" + code.bin[:6]).hash in J_index_to_inst.keys():
                instructions += DisAssembler.j_decode(code) + "\n"
            else:
                raise ValueError("Unknown machiche code:{}".format(code.bin[:6]))
        return instructions

    @staticmethod
    def r_decode(code):
        op, rs, rt, rd, shamt, funct = code.split([6, 11, 16, 21, 26, 32])
        if rt == 0 and rd == 0:
            inst = "{} {}".format(R_index_to_inst[funct.hash], index_to_reg[rs.hash])
        else:
            inst = "{} {}, {}, {}".format(
                R_index_to_inst[funct.hash],
                index_to_reg[rd.hash],
                index_to_reg[rs.hash],
                index_to_reg[rt.hash],
            )
        return inst

    @staticmethod
    def i_decode(code):
        op, rs, rt, add = code.split([6, 11, 16, 32])
        if I_index_to_inst[op.hash] in ["lw", "sw"]:
            inst = "{} {}, {}({})".format(
                I_index_to_inst[op.hash],
                index_to_reg[rt.hash],
                add.value_base(10),
                index_to_reg[rs.hash],
            )
        else:
            inst = "{} {}, {}, {}".format(
                I_index_to_inst[op.hash],
                index_to_reg[rt.hash],
                index_to_reg[rs.hash],
                add.value_base(10),
            )
        return inst

    @staticmethod
    def j_decode(code):
        op, addr = code.split([6, 32])
        inst = "{} {}".format(J_index_to_inst[op.hash], addr.value_base(10))
        return inst


if __name__ == "__main__":
    print(DisAssembler.decode("0x0800271000af8020ae51000a"))
