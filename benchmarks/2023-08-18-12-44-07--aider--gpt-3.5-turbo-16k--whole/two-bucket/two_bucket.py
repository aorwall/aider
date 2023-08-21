def measure(bucket_one, bucket_two, goal, start_bucket):
    # Initialize the buckets
    buckets = {
        'one': {'size': bucket_one, 'current': 0},
        'two': {'size': bucket_two, 'current': 0}
    }

    # Determine which bucket to fill first
    if start_bucket == 'one':
        fill_bucket = 'one'
        other_bucket = 'two'
    else:
        fill_bucket = 'two'
        other_bucket = 'one'

    # Perform the actions until the goal is reached
    actions = 0
    while True:
        # Fill the fill_bucket
        buckets[fill_bucket]['current'] = buckets[fill_bucket]['size']
        actions += 1

        # Check if the goal is reached
        if buckets[fill_bucket]['current'] == goal:
            return actions, fill_bucket, buckets[other_bucket]['current']

        # Pour from fill_bucket to other_bucket
        pour_amount = min(buckets[fill_bucket]['current'], buckets[other_bucket]['size'] - buckets[other_bucket]['current'])
        buckets[fill_bucket]['current'] -= pour_amount
        buckets[other_bucket]['current'] += pour_amount
        actions += 1

        # Check if the goal is reached
        if buckets[other_bucket]['current'] == goal:
            return actions, other_bucket, buckets[fill_bucket]['current']

        # Empty the fill_bucket if it becomes empty
        if buckets[fill_bucket]['current'] == 0:
            buckets[fill_bucket]['current'] = buckets[fill_bucket]['size']
            actions += 1

        # Empty the other_bucket if it becomes full
        if buckets[other_bucket]['current'] == buckets[other_bucket]['size']:
            buckets[other_bucket]['current'] = 0
            actions += 1
