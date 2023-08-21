def measure(bucket_one, bucket_two, goal, start_bucket):
    if start_bucket == 'one':
        bucket_one_current = bucket_one
        bucket_two_current = 0
    else:
        bucket_one_current = 0
        bucket_two_current = bucket_two

    actions = 1  # Initial fill
    previous_state = (bucket_one_current, bucket_two_current)

    while bucket_one_current != goal and bucket_two_current != goal:
        if bucket_one_current == 0:
            bucket_one_current = bucket_one
            actions += 1
        elif bucket_two_current == bucket_two:
            bucket_two_current = 0
            actions += 1
        else:
            transfer = min(bucket_one_current, bucket_two - bucket_two_current)
            bucket_one_current -= transfer
            bucket_two_current += transfer
            actions += 1

        current_state = (bucket_one_current, bucket_two_current)
        if current_state == previous_state:
            raise ValueError("The goal cannot be achieved with the given bucket sizes.")
        previous_state = current_state

    if bucket_one_current == goal:
        return actions, 'one', bucket_two_current
    else:
        return actions, 'two', bucket_one_current
