# Blockscript

A typed language that compiles into Scratch files, providing young learners with a bridge between visual block programming and a typed coding environment.

- **NOTE: This project is still in a very early stage of development. It is currently unfinished and does not work. Please do not use until this message goes away.**

---

## Installation

1. Download or clone the repository via `git clone https://github.com/piano-miles/blockscript.git`.
2. Install the necessary dependencies by running `pip install -r requirements.txt` in your command line.

## Usage

1. Write your Blockscript code in the [`main.bs3`](main.bs3) file.
2. Compile the Blockscript code into Scratch code by running [`main.py`](main.py)
3. The compiled Scratch code will be saved as an `sb3` file.
4. Open Scratch and import the `sb3` file.

## Details

Blockscript files end in `.bs3` but can be raw text as well. The Blockscript compiler will compile the project to a `.sb3` Scratch file.

### Syntax

The syntax is detailed in the [`syntax files`](examples/syntax.md) in the examples folder.

### Examples

There are currently no examples. The examples will be made available in [`examples`](examples).

## License

Blockscript is licensed under the BSD 3-Clause “New” or “Revised” License. See the [LICENSE](LICENSE) file for more details.
