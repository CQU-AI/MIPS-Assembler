from .Memory import Memory
from .Registers import Registers
from .RegData import RegData
from .Stack import Stack

# Currently unsupported instructions
# Unsigned problem: 			addiu addu sltiu sltu subu multu divu
# Link problem: 				bgezal bltzal jal
# Jump problem: 				jr
# Byte problem: 				lb sb
# Arithmetic shift problem: 	sra
# Other: 						syscall
# Oct 20, 2019


# Add (with overflow)
def add_(rd, rs, rt):
    Registers.reg_set(rd, Registers.reg_get(rt) + Registers.reg_get(rs))


# Add immediate (with overf low)
def addi_(rt, rs, imm):
    if(rt == "$sp" and rs == "$sp"):      #实现堆栈申请和归还
        if(imm <= 0):
            Stack.apply(imm)
        else:
            Stack.Sreturn(imm)
    Registers.reg_set(rt, Registers.reg_get(rs) + RegData(imm))


# Add immediate unsigned(no overflow)
# def addiu_(rt, rs, imm):
#     Registers.reg_set(rt, Registers.reg_get(rs) + RegData(imm))

# Add unsigned (no overflow)
# def addu_(rd, rs, rt):
#     Registers.reg_set(rd, Registers.reg_get(rt) + Registers.reg_get(rs))

# Bitwise and
def and_(rd, rs, rt):
    Registers.reg_set(rd, Registers.reg_get(rt) & Registers.reg_get(rs))


# Bitwise and immediate
def andi_(rt, rs, imm):
    Registers.reg_set(rt, Registers.reg_get(rs) & RegData(imm))


# Branch on equal
def beq_(rt, rs, LABEL):
    return LABEL if Registers.reg_get(rt) == Registers.reg_get(rs) else None


# Branch on greater than or equal to zero
def bgez_(rs, LABEL):
    return LABEL if Registers.reg_get(rs) >= 0 else None


# Branch on greater than or equal to zero and link
# def bgezal_(rs, LABEL):

# Branch on greater than zero
def bgtz_(rs, LABEL):
    return LABEL if Registers.reg_get(rs) > 0 else None


# Branch on less than or equal to zero
def blez_(rs, LABEL):
    return LABEL if Registers.reg_get(rs) <= 0 else None


# Branch on less than zero
def bltz_(rs, LABEL):
    return LABEL if Registers.reg_get(rs) < 0 else None


# Branch on less tan zero and link
# def bltzal_(rs, LABEL):

# Divide
def div_(rs, rt):
    Registers.reg_set(
        "$LO", Registers.reg_get(rs) // Registers.reg_get(rt), is_private=True
    )
    Registers.reg_set(
        "$HI", Registers.reg_get(rs) % Registers.reg_get(rt), is_private=True
    )


# Divide unsigned
# def divu_(rs, rt):

# Jump
def j_(LABEL):
    return LABEL


# Jump and link
# def jal_(LABEL):

# Jump register
# def jr_(rd):

# Load Byte
# def lb_(rt, offset, rs)

# Load upper immediate
def lui_(rt, imm):
    Registers.reg_set(rt, RegData(RegData(imm) < 16))


def lw_(rt, add, rs):
    if(rs == "$sp"):
        dw = Stack.pop(rt, add)
    else:
        dw = Memory.get_dw(Registers.reg_get(rs) + add)
    Registers.reg_set(rt, dw)


# Move from HI
def mfhi_(rd):
    Registers.reg_set(rd, Registers.reg_get("$HI", is_private=True))


# Move from LO
def mflo_(rd):
    Registers.reg_set(rd, Registers.reg_get("$LO", is_private=True))


# Multiply
def mult_(rs, rt):
    high, low = (Registers.reg_get(rs) * Registers.reg_get(rt)).split([32, 64])
    Registers.reg_set("$HI", high, is_private=True)
    Registers.reg_set("$LO", low, is_private=True)


# Multiply unsigned
# def multu_(rs, rt):

# No operation
def noop_():
    pass


# Bitwise or
def or_(rd, rs, rt):
    Registers.reg_set(rd, Registers.reg_get(rt) | Registers.reg_get(rs))


# Bitwise or immediate
def ori_(rt, rs, imm):
    Registers.reg_set(rt, Registers.reg_get(rs) | RegData(imm))


# Store byte
# def sb_(rt, offset, rs):

# Shift left logical
def sll_(rt, rs, imm):
    Registers.reg_set(rt, Registers.reg_get(rs) << RegData(imm))


# Shift left logical variable
def sllv_(rd, rt, rs):
    Registers.reg_set(rd, Registers.reg_get(rt) << Registers.reg_get(rs))


# Set on less than (signed)
def slt_(rd, rs, rt):
    Registers.reg_set(rd, RegData(Registers.reg_get(rs) < Registers.reg_get(rt)))


# Set on less than immediate (signed)
def slti_(rt, rs, imm):
    Registers.reg_set(rt, RegData(Registers.reg_get(rs) < RegData(imm)))


# Set on less than immediate unsigned
# def sltiu_(rt, rs, imm):
#    Registers.reg_set(rt, RegData(Registers.reg_get(rs) < RegData(imm)))


# Set on less than unsigned
# def sltu_(rt, rs, imm):
#    Registers.reg_set(rt, RegData(Registers.reg_get(rs) < RegData(imm)))

# Shift right arithmetic
# def sra_(rd, rt, shamt)f

# Shift right logical
def srl_(rd, rt, shamt):
    Registers.reg_set(rd, Registers.reg_get(rt) >> RegData(shamt))


# Shift right logical variable
def srlv_(rd, rt, rs):
    Registers.reg_set(rd, Registers.reg_get(rt) >> Registers.reg_get(rs))


# Subtract
def sub_(rd, rs, rt):
    Registers.reg_set(rd, Registers.reg_get(rt) - Registers.reg_get(rs))


# Subtracted unsigned
# def subu_(rd, rs, rt):

# Store word
def sw_(rt, add, rs):
    if(rs == "$sp"):         #实现push
        Stack.push(rt, add)
    else:
        dw = Registers.reg_get(rt)
        Memory.set_dw(Registers.reg_get(rs) + add, dw)


# System call
# def syscall_():

# Bitwise exclusive or
def xor_(rd, rs, rt):
    Registers.reg_set(rd, Registers.reg_get(rt) ^ Registers.reg_get(rs))


# Bitwise exclusive or immediate
def xori_(rt, rs, imm):
    Registers.reg_set(rt, Registers.reg_get(rs) ^ RegData(imm))
