# Discrete-Time-Signal-Convolution
This is a Python code for discrete time signal convolution. The code defines a function conv() that takes four arguments: x_value, x_start, h_value, and h_start.

The function first calculates the multiplication of the two input signals and stores the result in a list called keeper. It then inserts zeros in the empty places to align the signals properly.

Next, it calculates the sum of each column in the keeper list and stores the result in a list called conv_res. It also calculates the value of n for the first value in conv_res.

Then it adds some zeros to the start and end of each signal and conv_res list to properly align them for plotting. Finally, it plots the three signals using the stem() function from the matplotlib library.

There are five examples provided, each with its own input signals and start values. However, only the last example is uncommented, which means it will be executed when the code is run. The other examples are commented out and can be run by uncommenting them.
