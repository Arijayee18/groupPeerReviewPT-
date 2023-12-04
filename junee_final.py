import csv
import matplotlib.pyplot as plt

def parse_data(file_name):
    data = []
    with open(file_name, encoding='cp437') as file:
        next(file)
        contents = csv.reader(file)
        for row in contents:
            if row [3] == '' or row[5] == 'Unrated':    # Skip over lines with empty names or unrated ramen
                pass
            else:
                data.append(row)
        return data
    


def average_ratings(data):
    rating_dict = {}
    count_dict = {}
    for row in data:
        style = row[3]
        rating = float(row[5])
        if style not in rating_dict.keys():
            rating_dict[style] = rating         # If style is new, assign style to rating in dictionary
            count_dict[style] = 1               # Assign style to count in dictionary
        else:
            rating_dict[style] += rating        # If style is not new, add rating to previous ratings
            count_dict[style] += 1
    
    average_ratings = {}
    for key in rating_dict:
        average_ratings[key] = rating_dict[key] / count_dict[key]   # Calculate average of each style by dividing rating by total number of ramen in that style
    return average_ratings



# Create bar chart of average ratings
def create_graph(average_ratings):
    keys = list(average_ratings.keys())
    values = list(average_ratings.values())
    plt.bar(keys, values)
    plt.savefig('ramen_averages.png')



if __name__ == "__main__":
    ramen_data = parse_data('ramen-ratings.csv')    # Parse data 

    averages = average_ratings(ramen_data)          # Calculate average ratings of each style

    create_graph(averages)                          # Create bar chart of averages

    sorted_averages = sorted(averages.items(), key=lambda x:x[1])   # Create a sorted list of ratings and access max rating
    print(f'The highest rated style of ramen is {sorted_averages[-1][0].lower()} ramen with a rating of {sorted_averages[-1][1]}.')
    