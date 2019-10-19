# Contributing

> **Everyone is welcomed to contribute!**

To contribute, you may want to read the [README](./README.md) to find out what we are doing here.

## Dev info
Here are some other informations for developers:

This project mainly contains two seperate part : `Assembler` and `Simulator`

### `Assembler`
 - `class Assembler` : Encodes mips instructions to machine code.
 - `class DisAssembler` : Decodes machine code to mips instructions.
 - Depends on `class RegData`, `misc.static`.

### `Simulator`
 - `class Interpreter` : Parse and run mips instructions.
 - `class Simulator` : Run the mips instructions.
 - Depends on `class RegData`,`class Memory`,`class Registers`,`misc.static`.
 - Supported mips instructions:`lw`, `sw`, `add`, `addi`, `and`, `beq`, `j`, `or`, `sub`, `sll`, `slt`, `slti`, `srl`

### Dependency
 - `class RegData` : **[Key of this project]** Deals with all kinds of numbers and number_length stuffs.
 - `class Memory` : Simulates sparse memory (singleton mode).
 - `class Registers` : Simulates registers (singleton mode).
 - `misc.static` : Stores the static dictionaries.

### Unit test
See `./test/unit_test`
