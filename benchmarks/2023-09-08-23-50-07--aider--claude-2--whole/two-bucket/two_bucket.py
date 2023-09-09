def measure(bucket_one, bucket_two, goal, start_bucket):
    
    if start_bucket not in ["one", "two"]:
        raise ValueError("start_bucket must be 'one' or 'two'")
        
    if bucket_one <= 0 or bucket_two <= 0 or goal <= 0:
        raise ValueError("Bucket sizes and goal must all be positive")

    bucket_one_max = bucket_one
    bucket_two_max = bucket_two

    if start_bucket == "one":
        current_bucket = bucket_one
        other_bucket = bucket_two
    else:
        current_bucket = bucket_two
        other_bucket = bucket_one

    actions = 0
    while current_bucket != goal:
        if current_bucket < bucket_two_max:
            diff = bucket_two_max - other_bucket
            to_pour = min(diff, current_bucket)
            current_bucket -= to_pour
            other_bucket += to_pour
        elif other_bucket > 0:
            other_bucket = 0
        else:
            current_bucket = bucket_one_max

        actions += 1

    return (actions, current_bucket, other_bucket)
