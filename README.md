# 2D-Materials-Processor

This python script converts set of molecular formulas into the One Hot Vector.

It reads a CSV file that contains a column named "Formula" . (Example file: 2d-materials-list.csv )

Then it converts it into a One Hot Vector (actually it is a count vector: it contains number of elements).

Writes the result in to a CSV file (OneHotVector.csv).

This information can be used as a descriptors for machine learning processes.

Code also plots the occurence counts of each element:

![alt text](https://raw.githubusercontent.com/mcsorkun/2D-Materials-Processor/master/elements.png)
