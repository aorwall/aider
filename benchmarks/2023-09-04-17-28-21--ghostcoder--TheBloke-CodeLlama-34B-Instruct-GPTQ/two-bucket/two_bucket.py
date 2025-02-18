def measure(bucket_one, bucket_two, goal, start_bucket):
    # Initialize variables to keep track of current contents and moves
    cur_bucket_one = bucket_one
    cur_bucket_two = 0
    moves = 0

    # Perform moves until we achieve or exceed the desired amount
    while cur_bucket_one != goal and cur_bucket_two != goal and cur_bucket_one <= bucket_one and cur_bucket_two <= bucket_two:
        # Determine which bucket to fill based on the provided start bucket
        if start_bucket == 'one':
            # If bucket one starts off as empty, fill it
            if cur_bucket_one == 0:
                cur_bucket_one = bucket_one
            else:
                # Otherwise, pour it into bucket two
                cur_bucket_two += cur_bucket_one
                cur_bucket_one = 0
        elif start_bucket == 'two':
            # If bucket two starts off as empty, fill it
            if cur_bucket_two == 0:
                cur_bucket_two = bucket_two
            else:
                # Otherwise, pour it into bucket one
                cur_bucket_one += cur_bucket_two
                cur_bucket_two = 0

        # Increment move counter
        moves += 1

    # Check whether we successfully reached the desired amount
    if cur_bucket_one == goal or cur_bucket_two == goal:
        return moves
    else:
        return -1
