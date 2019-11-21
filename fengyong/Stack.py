from .Registers import Registers


class Stack:
    __pointer = 1000000  # 栈顶指针
    __nsize = 0  # 栈的层数
    __lsize = 0  # 栈的开启长度
    __fsize = 0  # 使用长度
    __save = []  # 存储

    def __init__(self):
        raise SyntaxError("Register can not instance, please use class method")

    @classmethod
    def apply(cls, size):  # 申请堆栈空间
        if size >= 0:
            raise SyntaxError("Please use a minus")
        if -size % 4 != 0:
            raise SyntaxError("Please use an integral multiple of -4")
        cls.__pointer = cls.__pointer + size
        cls.__nsize = (1000000 - cls.__pointer) / 4
        cls.__lsize = 1000000 - cls.__pointer

    @classmethod
    def push(cls, inregname, point):  # 执行push操作
        if point % 4 != 0:
            raise SyntaxError("Please use an integral multiple of 4")
        if point > (cls.__lsize - cls.__fsize):
            raise SyntaxError("Index out of range, please ask for more stack space")
        cls.__save = cls.__save.append(Registers.reg_get(inregname))
        cls.__fsize = cls.__fsize + 4

    @classmethod
    def pop(cls, outregname, point):  # 执行pop操作
        if point % 4 != 0:
            raise SyntaxError("Please use an integral multiple of 4")
        if point > (cls.__lsize - cls.__fsize):
            raise SyntaxError("Index out of range")
        if point != cls.__fsize:
            raise SyntaxError("You can only pop subject on stack top")
        transporter = cls.__save[-1]
        return transporter

    @classmethod
    def Sreturn(cls, point):
        if point % 4 != 0:
            raise SyntaxError("Please use an integral multiple of 4")
        if point > cls.__fsize:
            raise SyntaxError(
                "Index out of range, stack doesn't have enough space to return"
            )
        for i in range(1, point / 4):
            cls.__save.pop()
        cls.__fsize = cls.__fsize - point
        cls.__lsize = cls.__lsize - point
        cls.__nsize = cls.__nsize - point / 4
        cls.__pointer = cls.__pointer + point

    @classmethod
    def clean(cls):  # 重置堆栈
        cls.__pointer = 1000000
        cls.__nsize = 0
        cls.__lsize = 0
        cls.__fsize = 0
        cls.__save = []
