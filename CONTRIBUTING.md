# Contributing

> **Everyone is welcomed to contribute!**

To contribute, firstly you may have to read the [README](./README.md) to know what we exactly doing here.

## Dev info
Here are some other informations for developer:

This project mainly contains two seperate part : `Assemble` and `Simlator`

### `Assemble`
 - `class Assembler` : Encode mips instructions to machine code.
 - `class DisAssembler` : Decode machine code to mips instructions.
 - depends on `class RegData`,`misc.static`.

### `Simlator`
 - `class Interpreter` : Interpret mips instructions to python and run it.
 - `class Simulator` : Run the mips instructions.
 - depends on `class RegData`,`class Memory`,`class Registers`,`misc.static`.
 
### Depends
 - `class RegData` : **[key of this project]** Deal with all the numbers and number_length stuffs.
 - `class Memory` : Sparse memory simlulation (singleton mode).
 - `class Registers` : Registers simlulation (singleton mode).
 - `misc.static` : store the static dics.
