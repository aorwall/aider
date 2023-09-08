def measure(bucket_one, bucket_two, goal, start_bucket):
    if start_bucket not in (1, 2):
        raise ValueError("Invalid start bucket, must be either 1 or 2.")

    if goal > bucket_one + bucket_two:
        raise ValueError("The goal cannot be greater than the combined capacity of both buckets.")

    current_bucket = start_bucket
    other_bucket = 1 if start_bucket == 2 else 2
    actions = 0
    liters_left = 0

    while goal != 0:
        if current_bucket == start_bucket:
            if goal <= bucket_one:
                actions += 1
                goal -= bucket_one
            else:
                actions += 2
                goal -= bucket_one
                current_bucket = other_bucket
        else:
            if goal <= bucket_two:
                actions += 1
                goal -= bucket_two
            else:
                actions += 2
                goal -= bucket_two
                current_bucket = other_bucket

    if current_bucket == start_bucket:
        liters_left = bucket_two
    else:
        liters_left = bucket_one

    return actions, current_bucket, liters_left
