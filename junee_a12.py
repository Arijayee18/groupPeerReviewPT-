# Junee Omana
# Section J
# Assessment 12
# References: no one
# Time: 2 hours

import csv

def parse_price_file(datafile):
    pricing_options = []
    with open(datafile, 'r') as file:
        seats_remaining = int(file.readline())
        for row in file:
            price = row.split()
            pricing_options.append(price)

    return [pricing_options, seats_remaining]



def ticket_pricing(price_data, week, num_seats_left):
    if week == 0 or num_seats_left == 0:
        return 0
    max_rev = 0
    for i in price_data[-week]:
        option = i.split(',')
        price = int(option[0])
        available_tickets = int(option[1])
        tickets_bought = min(num_seats_left, available_tickets)
        rev = tickets_bought * price
        new_num_seats_left = num_seats_left - tickets_bought

        if new_num_seats_left > 0 and week > 0:
            rev += ticket_pricing(price_data, week - 1, new_num_seats_left)
        
        max_rev = max(max_rev, rev)

    return max_rev



if __name__ == "__main__":
    datafile = input("DATA_FILE> ")
    data = parse_price_file(datafile)
    max_rev = ticket_pricing(data[0], len(data[0]), data[1])
    print(f'OUTPUT {max_rev}')









