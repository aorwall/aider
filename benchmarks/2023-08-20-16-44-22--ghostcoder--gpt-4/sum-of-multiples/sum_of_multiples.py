def sum_of_multiples(limit, multiples):
    # Generate the multiples of each base value that are less than the level number
    multiples_list = [i for multiple in multiples if multiple != 0 for i in range(multiple, limit, multiple)]
    # Combine these lists into a single list, convert it to a set to remove duplicates
    unique_multiples = set(multiples_list)
    # Sum the unique multiples
    return sum(unique_multiples)