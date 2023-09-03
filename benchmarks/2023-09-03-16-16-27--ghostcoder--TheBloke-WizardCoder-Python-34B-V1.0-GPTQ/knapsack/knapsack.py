def maximum_value(maximum_weight, items):
    prev_row = [0]*(maximum_weight+1)
    curr_row = [0]*(maximum_weight+1)

    for i in range(len(items)):
        wi, vi = items[i]['weight'], items[i]['value']
        for j in range(maximum_weight+1):
            if j >= wi:
                curr_row[j] = max(prev_row[j], prev_row[j-wi]+vi)

        prev_row, curr_row = curr_row, prev_row

    # Return the final answer
    return prev_row[-1]
