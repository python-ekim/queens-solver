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
Make sure to install or upgrade via 
$ pip install --upgrade matplotlib

## Usage
The program prompts allowing you to have different experiences and do a simple comparisson of 3 algorithms:
A Human solving the Challenge
The Computer solving it using a fixed algorithm placing the Queens in order
The Computer solving it using random positions with recursive logic to solve the Challenge
The Computer performing N iterations to find as many different solutions as possible

## Features Version 2
-In Iterations Mode user chose to either use:
    Bit logic to represent the chessboard using 44 bytes or
    standar array [[0 for col in range(8)] for row in range(8)] using 120 bytes

-Each board position is encoded using 00 Empty, 01 Attacked, 10 Queen, 11 Not Used
-All the functions use Chess Standard Notation A,B,C,D,E,F,G,H for Columns 1,2,3,4,5,6,7,8 for Rows
-Using the Interation Mode you can compute different solutions, experiment increasing the number of iterations to see the progression of time vs. number of solutions found
-NEW in Version 2 you can Plot the results of the Iteration mode

## Contributing
DONE -Adapt the algoritm to use a standard array [[0 for col in range(8)] for row in range(8)] to benchmark performance
DONE -Use MathPlot to graph a curve on computing cycles vs. time comparing bit encoding vs. standard array
-Change from text in Command Line to a GUI
-Find out if implementing ML can provide faster solutions using less cycles

## License
This project is licensed under the BDMS Consulting NonCommercial License

### Terms and Conditions
1. **Non-Commercial Use**: This project is free to use for non-commercial purposes only. You may use, modify, and distribute the code for personal, educational, or research purposes.
2. **Attribution**: You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
3. **No Warranty**: The project is provided "as is", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages, or other liability, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the project or the use or other dealings in the project.

## Credits
-Very Thankful with the courses of https://edube.org/ Phython Essentials 1 & Phython Essentials 2

## Contact
Miguel Bernadez
mike@bdms-consulting.com
https://bdms-consulting.com

