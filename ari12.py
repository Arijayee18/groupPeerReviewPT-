import csv


def parse_price_file(filename):
    price_data = []
    infile = open(filename, 'r')
    remaining_seats = int(next(infile))
    for line in infile:
        values = line.split()
        price_data.append(values)
    print([remaining_seats, price_data])
    return [price_data, remaining_seats]


def ticket_pricing(price_data, week, num_seats):
    rev = 0
    if week == 0:
        return 0
    elif week != 0:
        for weeks in price_data[-week]:
            weeks = weeks.split(',')
            prices = int(weeks[0])
            current_seats = int(weeks[1])
            seats_used = min(num_seats, current_seats)
            max_rev = seats_used * prices
            seats_left = num_seats - seats_used
            if seats_left > 0:
                max_rev += ticket_pricing(price_data, week-1, seats_left)
            if max_rev > rev:
                rev = max_rev
        return rev


if __name__ == '__main__':
    filename = input()
    data = parse_price_file(filename)
    price_data = data[0]
    week = len(price_data)
    num_seats = data[1]
    pricing = ticket_pricing(price_data, week, num_seats)
    print(f'OUTPUT {pricing}')
