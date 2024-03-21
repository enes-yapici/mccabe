# McCabe-Thiele Method for Binary Distillation

This repository contains a Python script that implements the McCabe-Thiele method to determine the number of theoretical stages required for a binary distillation process. The script also generates a plot that visualizes the McCabe-Thiele diagram, including the equilibrium line, operating lines for the enriching and stripping sections, and the step-by-step construction used to determine the number of stages.

## Overview

The McCabe-Thiele method is a graphical technique used in chemical engineering to design and analyze the performance of distillation columns. It simplifies the complex calculations involved in distillation into a straightforward graphical method, allowing engineers to quickly estimate the number of theoretical stages needed to achieve a desired separation.

## Features

- Calculation of the number of theoretical stages using the McCabe-Thiele method.
- Visualization of the equilibrium line, enriching and stripping section operating lines, and the feed line.
- Dynamic adjustment to different operating conditions and feed compositions.

## Requirements

To run this script, you'll need:

- Python 3.x
- NumPy
- Matplotlib
- Pandas

Ensure you have these packages installed, which can be done using pip:
pip install numpy matplotlib pandas

## Usage

1. Clone this repository to your local machine.
2. Prepare an Excel file named `xy_data.xlsx` containing the binary mixture data with columns labeled `x` and `y`, representing the mole fraction of the more volatile component in the liquid and vapor phases, respectively.
3. Run the script with Python:
mccabe.py

4. The output will be a plot displayed on your screen showing the McCabe-Thiele diagram for the binary distillation process. Additionally, the script will print the number of theoretical stages required.

## Contributing

Feel free to fork this repository and submit pull requests to contribute to the development of this script. If you encounter any issues or have suggestions for improvements, please open an issue.
