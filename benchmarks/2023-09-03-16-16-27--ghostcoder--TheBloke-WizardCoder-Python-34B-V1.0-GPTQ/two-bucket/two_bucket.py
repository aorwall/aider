from math import ceil

def measure(bucket_one, bucket_two, goal, start_bucket):
    if start_bucket == "one":
        current_bucket = bucket_one
        other_bucket = bucket_two
    else:
        current_bucket = bucket_two
        other_bucket = bucket_one

    steps = 0
    while True:
        if current_bucket == goal:
            return (steps, start_bucket, other_bucket)
        elif current_bucket > goal:
            diff = current_bucket - goal
            other_bucket += diff
            current_bucket -= diff
            steps += 1
        elif other_bucket + current_bucket < goal:
            other_bucket += current_bucket
            current_bucket = 0
            steps += 1
        else:
            diff = goal - other_bucket
            current_bucket += diff
            other_bucket -= diff
            steps += 1
        if start_bucket == "one":
            start_bucket, other_bucket = other_bucket, current_bucket
        else:
            start_bucket, other_bucket = current_bucket, other_bucket
