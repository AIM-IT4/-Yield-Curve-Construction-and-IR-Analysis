
# Yield Curve Construction and Analysis Using QuantLib Python

This repository contains a Python script for constructing and analyzing yield curves using various methods provided by QuantLib Python. The script demonstrates how to build a yield curve from market data and compare different construction methods.

## Description

The project focuses on three methods for constructing yield curves:

1. **Piecewise Linear Zero Rates (`PiecewiseLinearZero`)**: Constructs the curve by linearly interpolating the zero rates.
2. **Piecewise Log Cubic Discount (`PiecewiseLogCubicDiscount`)**: Uses log cubic interpolation of the discount factors.
3. **Piecewise Cubic Zero Rates (`PiecewiseCubicZero`)**: Applies cubic interpolation to the zero rates.

Each method is applied to the same set of market data for comparison. The script plots the yield curves and calculates the forward rate after one year for each method.

## Requirements

- Python 3
- QuantLib Python
- Matplotlib
- NumPy

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install QuantLib Python, Matplotlib, and NumPy.

```bash
pip install QuantLib-Python matplotlib numpy
```

## Usage

Run the script `yield_curve_construction.py` to generate the plots and analysis. The script will display subplots for each yield curve construction method and print out the forward rates.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
