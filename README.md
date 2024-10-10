# Project Title
8 Queens Challenge - Place 8 Queens in the chessboard without any one of them attacking each other

## Description
Provide a fun way to experiment human vs. computer solutions

## Table of Contents
- Installation
- Usage
- Features
- Contributing
- License
- Credits
- Contact

## Installation
This program uses regular Python libraries. You should not need to install anything additional.

## Usage
The program prompts allowing you to have different experiences and do a simple comparisson of 3 algorithms:
Your mind solving the Challenge
The Computer solving it using a fixed algorithm placing the Queens in order
The Computer solving it using random positions with recursive logic to solve the Challenge

## Features
-Bit logic to represent the chessboard using 44 bytes vs. 120 bytes for a simplier array [[0 for col in range(8)] for row in range(8)]
-Each board position is encoded using two bits to represent: 00 Empty, 01 Attacked, 10 Queen, 11 Not Used
-All the functions use Chess Standard Notation A,B,C,D,E,F,G,H for Columns 1,2,3,4,5,6,7,8 for Rows
-Using the Interation Mode you can compute different solutions, experiment increasing the number of iterations to see the progression of time vs. number of solutions found

## Contributing
-Change from text in Command Line to a GUI
-Adapt the algoritm to use a standard array [[0 for col in range(8)] for row in range(8)] to benchmark performance
-Find out if implementing ML can provide the same number of solutions using less cycles
-Use MathPlot to graph a curve on computing cycles vs. time comparing bit encoding vs. standard array

## License
This project is licensed under the BDMS Consulting NonCommercial License

## Credits
-Very Thankful with the courses of https://edube.org/ Phython Essentials 1 & Phython Essentials 2

### Terms and Conditions
1. **Non-Commercial Use**: This project is free to use for non-commercial purposes only. You may use, modify, and distribute the code for personal, educational, or research purposes.
2. **Attribution**: You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
3. **No Warranty**: The project is provided "as is", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages, or other liability, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the project or the use or other dealings in the project.

## Contact
Miguel Bernadez
mike@bdms-consulting.com
https://bdms-consulting.com

