def measure(bucket_one, bucket_two, goal, start_bucket):

    if start_bucket != "bucket_one" and start_bucket != "bucket_two":
        raise ValueError("start_bucket must be 'bucket_one' or 'bucket_two'")

    if bucket_one < 0 or bucket_two < 0 or goal < 0:
        raise ValueError("bucket sizes and goal must be positive numbers")

    num_actions = 0

    return num_actions, "", ""
