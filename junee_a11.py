# Junee Omana
# CSCI 128 - Section J
# Assessment 11
# References: no one
# Time: 30 minutes

import csv
import matplotlib.pyplot as plt

datafile = input('INPUT_PATH> ')
horizontal = input('OUTPUT_HS> ')
vertical = input('OUTPUT_VS> ')

coord_data = []
with open(datafile) as file:
    next(file)
    contents = csv.reader(file)
    for row in contents:
        coord_data.append(row)

x = []
y = []
z = []
for row in coord_data:
    x.append(float(row[0]))
    y.append(float(row[1]))
    z.append(abs(float(row[2])))

plt.plot(x, y)
plt.title(f'{datafile[:-4]} Horizontal Section')
plt.xlabel('Easting, EW (ft)')
plt.ylabel('Northing, NS (ft)')
plt.savefig(horizontal)
plt.clf()

plt.plot(x, z)
plt.title(f'{datafile[:-4]} Vertical Section')
plt.xlabel('East-West Crossection (ft)')
plt.ylabel('True Vertical Depth (ft)')
plt.savefig(vertical)