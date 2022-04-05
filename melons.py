melon_names = {
    1: 'Honeydew',
    2: 'Crenshaw',
    3: 'Crane',
    4: 'Casaba',
    5: 'Cantaloupe',
}

melon_prices = {
    1: 0.99,
    2: 2.00,
    3: 2.50,
    4: 2.50,
    5: 0.99,
}

melon_seedlessness = {
    1: True,
    2: False,
    3: False,
    4: False,
    5: False,
}

melon_flesh_color = {
    1: 'Green',
    2: 'Orange',
    3: 'Orange',
    4: 'White',
    5: 'Orange',
}

melon_rind_color = {
    1: 'Green',
    2: 'Orange',
    3: 'Green and White',
    4: 'Orange',
    5: 'Beige',
}

melon_average_weight = {
    1: 5,
    2: 9,
    3: 10,
    4: 5,
    5: 3,
}

# Create a master dictionary to store aggregate key, value melon data
all_melon_data = {}

def refactor_melons(melon_data, melon_attribute):
    """
    Update/reassign key, value data in master melon dictionary based on melon attribute.

    :param melon_data: a dictionary to store melon attribute key, value data
    :param melon_attribute: a dictionary containing melon attribute key, value data
    :return melon-data: an updated melon dictionary 
    """

    for key in melon_attribute:
        if key not in melon_data:
            melon_data[key] = [melon_attribute[key]]
        else:
            melon_data[key] += [melon_attribute[key]]

    return melon_data

refactor_melons(all_melon_data, melon_names)
refactor_melons(all_melon_data, melon_prices)
refactor_melons(all_melon_data, melon_seedlessness)
refactor_melons(all_melon_data, melon_flesh_color)
refactor_melons(all_melon_data, melon_rind_color)
refactor_melons(all_melon_data, melon_average_weight)

print(all_melon_data)