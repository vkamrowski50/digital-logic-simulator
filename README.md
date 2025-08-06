# Digital Logic Simulator

Python-based simulator for digital logic circuits. Built entirely from the ground up by **Victor Kamrowski**. This simulator models logic gates and combinational circuits. Uses object-oriented design and unit tests.

## Features

- Logic gate simulations for:
  - AND, OR, NOT, NAND, NOR, XOR, XNOR
- Combinational Circuits:
  - Half Adder, Full Adder, 4-Bit Ripple Carry Adder (more to come)
- Object-oriented design / architecture
- Unit tests with 'unittest'

## How to Run

To run unit tests:

1. Open project root directory in terminal after cloning
2. Use '-m' flag to run tests as modules:
  ```bash
  python3 -m tests.test_combinational
  ```

## Motivation

This project was part of my effort to build a strong foundation in computer architecture and digital systems. Working up from logic gates to full circuits. In preperation for this project and my ECE path, I read **Code: The Hidden Language of Computer Hardware and Software** by **Charles Petzold**.


## Future Plans

- more combinationals (multiplexers, decoders, ALUs, ...)
- sequential logic (flip-flops, latches, counters and registers, ...)
- gui for circuit design
- debugging tools
- export to HDLs eventually

## Tech Stack

- Python 3.x
- unittest
- OOP
