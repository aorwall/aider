def measure(bucket_one, bucket_two, goal, start_bucket):
    if start_bucket not in ["one", "two"]:
        raise ValueError("Invalid start bucket")

    if goal % gcd(bucket_one, bucket_two) != 0:
        raise ValueError("Goal cannot be reached")

    if start_bucket == "one":
        small_bucket, big_bucket = bucket_one, bucket_two
    else:
        small_bucket, big_bucket = bucket_two, bucket_one

    actions = 1
    small_bucket_level = small_bucket
    big_bucket_level = 0

    while small_bucket_level != goal and big_bucket_level != goal:
        if small_bucket_level == 0:
            small_bucket_level = small_bucket
            actions += 1
        elif big_bucket_level == big_bucket:
            big_bucket_level = 0
            actions += 1
        else:
            transfer = min(small_bucket_level, big_bucket - big_bucket_level)
            small_bucket_level -= transfer
            big_bucket_level += transfer
            actions += 1

    if small_bucket_level == goal:
        return actions, "one", big_bucket_level
    else:
        return actions, "two", small_bucket_level

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a