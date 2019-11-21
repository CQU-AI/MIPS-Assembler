from .RegData import RegData
from .static import reg_to_index, R_inst_to_index, I_inst_to_index, J_inst_to_index
from .Preprocessor import Preprocessor


class Assembler:
    def __init__(self):
        raise SyntaxError("Assembler can not instance, please use static method")

    @staticmethod
    def encode(instrcutions):
        """

        :param instrcutions: string
        :return:
        """
        instrcutions = Preprocessor.prep(instrcutions, return_label=False)
        machine_code = RegData(None)
        for inst in instrcutions:
            inst = list(
                filter(
                    lambda x: x != "",
                    inst.replace(",", " ")
                    .replace("(", " ")
                    .replace(")", "")
                    .split(" "),
                )
            )
            if inst[0] in R_inst_to_index.keys():
                machine_code = machine_code.concat(Assembler.r_encode(inst))
            elif inst[0] in I_inst_to_index.keys():
                machine_code = machine_code.concat(Assembler.i_encode(inst))
            elif inst[0] in J_inst_to_index.keys():
                machine_code = machine_code.concat(Assembler.j_encode(inst))
            else:
                raise ValueError("Unknown mips instruction:{}".format(inst[0]))
        return machine_code

    @staticmethod
    def r_encode(instruction_list):
        """
        R-type instruction encoder
        :param instruction_list: one inst
        :return: RegData
        """
        try:
            if len(instruction_list) == 4:
                op = RegData("0b000000")
                rs = reg_to_index[instruction_list[2]]
                rt = reg_to_index[instruction_list[3]]
                rd = reg_to_index[instruction_list[1]]
                shamt = RegData("0b00000")
                funct = R_inst_to_index[instruction_list[0]]

                return RegData.concat_list([op, rs, rt, rd, shamt, funct])
            else:
                op = RegData("0b000000")
                rs = reg_to_index[instruction_list[1]]
                rt = RegData("0b00000")
                rd = RegData("0b00000")
                shamt = RegData("0b00000")
                funct = R_inst_to_index[instruction_list[0]]

                return RegData.concat_list([op, rs, rt, rd, shamt, funct])
        except Exception as e:
            raise ValueError(
                'Unable to encode r_instruction:"{}",{}'.format(instruction_list, e)
            )

    @staticmethod
    def i_encode(instruction_list):
        """
        R-type instruction encoder
        :param instruction_list: one inst
        :return: RegData
        """

        try:
            # TODO: jump to inst unsupported
            if instruction_list[-1][0] == "$":
                op = I_inst_to_index[instruction_list[0]]
                rs = reg_to_index[instruction_list[3]]
                rt = reg_to_index[instruction_list[1]]
                add = RegData(instruction_list[2], 16)

                return RegData.concat_list([op, rs, rt, add])
            else:
                op = I_inst_to_index[instruction_list[0]]
                rs = reg_to_index[instruction_list[2]]
                rt = reg_to_index[instruction_list[1]]
                add = RegData(instruction_list[3], 16)

                return RegData.concat_list([op, rs, rt, add])
        except Exception as e:
            raise ValueError(
                'Unable to encode i_instruction:"{}",{}'.format(instruction_list, e)
            )

    @staticmethod
    def j_encode(instruction_list):
        """
        R-type instruction encoder
        :param instruction_list: one inst
        :return: RegData
        """
        # TODO: jump to label unsupported
        try:
            op = J_inst_to_index[instruction_list[0]]
            address = RegData(instruction_list[1], 26)
            return RegData.concat_list([op, address])

        except Exception as e:
            raise ValueError(
                'Unable to encode j_instruction:"{}",{}'.format(instruction_list, e)
            )


if __name__ == "__main__":
    inst = "j 10000\nadd $s0,$a1,$t7\nsw $s1,10($s2)"
    print(Assembler.encode(inst).bin, Assembler.encode(inst).value_base(16))
