"""Print out all the melons in our inventory."""


from melons import *


def print_melon(name, price, seedless, flesh, rind, weight):
    """Print each melon with corresponding attribute information."""

    have_or_have_not = 'have'
    if seedless:
        have_or_have_not = 'do not have'

    print(f'{name}s {have_or_have_not} seeds and are ${price}.')
    print(f'The flesh is {flesh} and the rind is {rind}.')
    print(f'The average weight is {weight}.')


# for i in melon_names:
#     print_melon(melon_names[i], melon_prices[i], melon_seedlessness[i], melon_flesh_color[i], melon_rind_color[i], melon_average_weight[i])

def print_melon_two(name, price, seedless, flesh, rind, weight):
    """Print each melon with corresponding attribute information."""

    have_or_have_not = 'have'
    if seedless:
        have_or_have_not = 'do not have'

    print(f'{name}s {have_or_have_not} seeds and are ${price}.')
    print(f'The flesh is {flesh} and the rind is {rind}.')
    print(f'The average weight is {weight}.')


for i in all_melon_data:
    print_melon_two(all_melon_data[i][0], all_melon_data[i][1], all_melon_data[i][2], all_melon_data[i][3], all_melon_data[i][4], all_melon_data[i][5])