#  Ciel Cochran
#  Section J
#  Assessment 11
#  Time:
#  References: none

import matplotlib.pyplot as plt
import csv

# Function to read survey data from a CSV file and create horizontal and vertical section plots


def create_section_plots(input_csv, output_horizontal, output_vertical):
    # Initialize lists to store x, y, and z coordinates
    x = []
    y = []
    z = []

    # Read the survey data from the CSV file
    with open(input_csv, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header row
        for line in csv_reader:
            x.append(float(line[0]))
            y.append(float(line[1]))
            z.append(float(line[2]) * -1)
    filename = input_csv.split('.')[0]
    # Create horizontal section plot
    plt.plot(x, y)
    plt.title(f'{filename} Horizontal Section')
    plt.xlabel("Easting, EW (ft)")
    plt.ylabel("Northing, NS (ft)")

    # Save the horizontal plot with a specified DPI (dots per inch)
    plt.savefig(output_horizontal)
    plt.clf()  # Clear the plot for the next one

    # Create vertical section plot
    plt.plot(x, z)
    plt.title(f"{filename} Vertical Section")
    plt.ylabel("True Vertical Depth (ft)")
    plt.xlabel("East-West Crossection (ft)")

    # Save the vertical plot with a specified DPI (dots per inch)
    plt.savefig(output_vertical)

# Input from the user


input_csv = input("INPUT_PATH> ")
output_horizontal = input("OUTPUT_HS> ")
output_vertical = input("OUTPUT_VS> ")

# Create the section plots and save them to the specified paths
create_section_plots(input_csv, output_horizontal, output_vertical)
