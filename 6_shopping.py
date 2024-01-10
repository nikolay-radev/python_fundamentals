budget = int(input())
price_counter = 0

while True:
    command = input()
    if command == 'End':
        print('You bought everything needed.')
        break
    current_price = float(command)
    if price_counter + current_price > budget:
        print('You went in overdraft!')
        break
    price_counter += current_price
