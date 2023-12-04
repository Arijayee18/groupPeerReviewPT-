# Name: Ciel Cochran
# Section: J
# References: Ari'jaye Derritt
# Final Project
# Time Taken: 30 minutes
import csv
import matplotlib.pyplot as plt

infile = open('./ps4_games.csv', 'r', newline='')


def parse_file_to_data(infile):
    data = []
    for line in infile:
        values = line.strip(',').split(',')
        data.append(values)
    data = data[1:]
    len(data)

    return data


data = parse_file_to_data(infile)
copies_sold = []
name_of_game = []
for lst in data:
    copies_sold.append(lst[1])
for lst in data:
    name_of_game.append(lst[0])
print(name_of_game)
print(copies_sold)

for million in range(len(copies_sold)):
    copies_sold[million] = float(copies_sold[million][0:2])
print(copies_sold)
print(type(copies_sold[0]))
max = max(copies_sold)
print(f'OUTPUT {max}') 

plt.bar(copies_sold, name_of_game, color='pink')
plt.title('Highest Selling PS4 Game')
plt.ylabel('Name of Game')
plt.xlabel('Copies Sold (In Millions)')
