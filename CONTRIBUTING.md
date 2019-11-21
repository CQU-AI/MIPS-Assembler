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
- Supported mips instructions:`add`,`addi`,`and`,`andi`,`beq`,`bgez`,`bgtz`,`blez`,`bltz`,`div`,`j`,`lui`,`lw`,`mfhi`,`mflo`,`mult`,`noop`,`or`,`ori`,`sll`,`sllv`,`slt`,`slti`,`srl`,`srlv`,`sub`,`sw`,`xor`,`xori`

### Dependency

- `class RegData` : **[Key of this project]** Deals with all kinds of numbers and number_length stuffs.
- `class Memory` : Simulates sparse memory (singleton mode).
- `class Registers` : Simulates registers (singleton mode).
- `misc.static` : Stores the static dictionaries.

## Unit test

This project use Tarvis-CI to run checks. PR can't be merge until it passes all the tests.

## To contribute

If you want to contribute to this project, you can work on the following stuffs (ordered from easy to hard):
- Use this tool and send us feedbacks
- Fix typo
- Add more instruction implementations
- Fix the issues
- Write the documentation
