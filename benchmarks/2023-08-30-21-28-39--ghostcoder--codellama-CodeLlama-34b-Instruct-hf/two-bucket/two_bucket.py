def measure(bucket_one, bucket_two, goal, start_bucket):
    # Initialize variables
    actions = 0
    current_bucket = start_bucket
    other_bucket = 1 if start_bucket == 2 else 2
    current_bucket_size = bucket_one if start_bucket == 1 else bucket_two
    other_bucket_size = bucket_two if start_bucket == 1 else bucket_one

    # Perform actions until the goal is reached or it's impossible to reach
    while current_bucket_size != goal and current_bucket_size + other_bucket_size >= goal:
        # If the current bucket is full, pour it into the other bucket
        if current_bucket_size == current_bucket:
            pour_amount = min(current_bucket_size, other_bucket_size - current_bucket_size)
            current_bucket_size -= pour_amount
            other_bucket_size += pour_amount
            actions += 1
        # If the other bucket is full, pour it into the current bucket
        elif other_bucket_size == other_bucket:
            pour_amount = min(other_bucket_size, current_bucket_size - other_bucket_size)
            other_bucket_size -= pour_amount
            current_bucket_size += pour_amount
            actions += 1
        # If the current bucket is empty, fill it
        elif current_bucket_size == 0:
            current_bucket_size = current_bucket
            actions += 1
        # If the other bucket is empty, fill it
        elif other_bucket_size == 0:
            other_bucket_size = other_bucket
            actions += 1

    # Return the number of actions and the final bucket with the goal amount
    return actions, current_bucket if current_bucket_size == goal else other_bucket
