from math import ceil


class RegData:
    def __init__(self, value, length=-1):
        """
        init the data
        :param value: string,int in any base
        :param length: max bin length
        """
        self.bin_length = length
        self.value = value

    def __repr__(self):
        return str(self.value)

    @staticmethod
    def op(a, b, func, return_regdata=True, res_bin_len=None):
        if isinstance(b, int):
            return (
                RegData(
                    func(a.value, b),
                    a.bin_length if res_bin_len is None else res_bin_len,
                )
                if return_regdata
                else func(a.value, b)
            )
        elif isinstance(b, str):
            b = RegData(b)
            return (
                RegData(
                    func(a.value, b.value),
                    max(a.bin_length, b.bin_length)
                    if res_bin_len is None
                    else res_bin_len,
                )
                if return_regdata
                else func(a.value, b.value)
            )
        elif isinstance(b, RegData):
            return (
                RegData(
                    func(a.value, b.value),
                    max(a.bin_length, b.bin_length)
                    if res_bin_len is None
                    else res_bin_len,
                )
                if return_regdata
                else func(a.value, b.value)
            )
        else:
            raise ValueError("Unable to handle data:{} in type {}".format(b, type(b)))

    def __add__(self, other_data):
        return self.op(self, other_data, int.__add__)

    def __mul__(self, other_data):
        return self.op(self, other_data, int.__mul__, res_bin_len=64)

    def __floordiv__(self, other_data):
        return self.op(self, other_data, int.__floordiv__)

    def __mod__(self, other_data):
        return self.op(self, other_data, int.__mod__)

    def __sub__(self, other_data):
        return self.op(self, other_data, int.__sub__)

    def __lt__(self, other_data):
        return self.op(self, other_data, int.__lt__, return_regdata=False)

    def __gt__(self, other_data):
        return self.op(self, other_data, int.__gt__, return_regdata=False)

    def __le__(self, other_data):
        return self.op(self, other_data, int.__le__, return_regdata=False)

    def __ge__(self, other_data):
        return self.op(self, other_data, int.__ge__, return_regdata=False)

    def __eq__(self, other_data):
        return self.op(self, other_data, int.__eq__, return_regdata=False)

    def __ne__(self, other_data):
        return self.op(self, other_data, int.__ne__, return_regdata=False)

    def __or__(self, other_data):
        return self.op(self, other_data, int.__or__)

    def __and__(self, other_data):
        return self.op(self, other_data, int.__and__)

    def __rshift__(self, n):
        return RegData(self.value >> n, self.bin_length)

    def __lshift__(self, n):
        return RegData(self.value << n, self.bin_length)

    def __hash__(self):
        return self._value.__hash__()

    @property
    def hash(self):
        return self.__hash__()

    def split(self, split_index):
        """
        split the RegData
        :param split_index: where to split (when you want to split 6 data in 3 groups, split_index should be [2,4,6])
        :return: list
        """
        res = []
        prew_i = 0
        for i in split_index:
            res.append(RegData("0b" + self.bin[prew_i:i]))
            prew_i = i
        return res

    def concat(self, other_data):
        """
        concat two RegData(not concat in place)
        :param other_data:
        :return: the concat two RegData
        """
        if self._value is None:
            return other_data
        if isinstance(other_data, int) or isinstance(other_data, str):
            return RegData("0b" + self.bin + RegData(other_data).bin)
        elif isinstance(other_data, RegData):
            return RegData("0b" + self.bin + other_data.bin)
        else:
            raise ValueError(
                "Unable to handle data:{} in type {}".format(
                    other_data, type(other_data)
                )
            )

    @staticmethod
    def concat_list(data_list):
        """
        concat a list of RegData together
        :param data_list:
        :return: the concat result
        """
        res = data_list[0]
        for i in data_list[1:]:
            res = res.concat(i)
        return res

    def resize(self, size):
        """
        set the max_bin_size
        :param size: max_bin_size
        :return: self
        """
        if size < self.bin_length:
            self._value = self._value % (2 ** size)
            raise Warning("Trying to reduce the RegData size")
        self.bin_length = size
        return self

    @property
    def value(self):
        """
        :return: RegData value in 10-base
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        value setter
        :param value: str,int in any base (0b,0o,0x,10)
        :return: None
        """
        if value is None:
            self._value = None
            return
        elif isinstance(value, int):
            self._value = int(value)
            self.check_overflow()
        elif isinstance(value, str):
            try:
                if value[:2] == "0x":
                    self._value = int(value[2:], 16)
                    self.bin_length = (
                        ceil((len(value) - 2) * 4)
                        if self.bin_length == -1
                        else self.bin_length
                    )
                elif value[:2] == "0b":
                    self._value = int(value[2:], 2)
                    self.bin_length = (
                        ceil((len(value) - 2) * 1)
                        if self.bin_length == -1
                        else self.bin_length
                    )
                elif value[:2] == "0o":
                    self._value = int(value[2:], 8)
                    self.bin_length = (
                        ceil((len(value) - 2) * 3)
                        if self.bin_length == -1
                        else self.bin_length
                    )
                else:
                    self._value = int(value)
                self.check_overflow()
            except Exception as e:
                raise ValueError("Unknown data value: {},{}".format(value, e))
        elif isinstance(value, bool):
            if value:
                self.bin_length = 32
                self._value = 1
            else:
                self.bin_length = 32
                self._value = 0
        else:
            raise ValueError("Unknown data value: {}".format(value))

    def check_overflow(self):
        if self._value >= (2 ** self.bin_length) and self.bin_length != -1:
            print("Warning: RegData Overflow")
            self._value = self._value % (2 ** (self.bin_length))

    @property
    def bin(self):
        """
        :return: Bin_code of RegData
        """
        if self._value is None:
            return None
        return self.value_base(2)[2:]

    def value_base(self, base=10):
        """
        get value in any base
        """
        if self._value is None:
            return None
        if base == 2:
            return "0b" + bin(self._value)[2:].zfill(self.bin_length)
        elif base == 8:
            res = "0o" + oct(self._value)[2:].zfill(ceil(self.bin_length // 3))
        elif base == 16:
            res = "0x" + hex(self._value)[2:].zfill(ceil(self.bin_length // 4))
        elif base == 10:
            return self._value
        else:
            raise ValueError("Unsupported data base: {}".format(base))
        return str(res)
