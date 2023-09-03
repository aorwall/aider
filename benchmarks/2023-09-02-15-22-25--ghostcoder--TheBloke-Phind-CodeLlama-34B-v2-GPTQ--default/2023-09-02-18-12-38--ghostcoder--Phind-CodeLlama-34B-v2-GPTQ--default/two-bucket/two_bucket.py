def measure(bucket_one, bucket_two, goal, start_bucket):
    # Check for invalid inputs
    if (goal < 0 or bucket_one <= 0 or bucket_two <= 0 or
            (start_bucket != 'one' and start_bucket != 'two')):
        raise ValueError('Invalid input values')

    # Initialize variables
    actions = 0
    b1 = bucket_one
    b2 = bucket_two
    state = start_bucket

    while True:
        # Case 1: Pour one bucket into another
        if state == 'one':
            b1 -= min(b1, b2 - b1)
            b2 += min(b1, b2 - b1)
            b1 = bucket_one - ((bucket_one + b1) % bucket_one)
        else:
            b2 -= min(b2, b1 - b2)
            b1 += min(b2, b1 - b2)
            b2 = bucket_two - ((bucket_two + b2) % bucket_two)

        # Count action
        actions += 1

        # Check for end conditions
        if b1 == goal or b2 == goal:
            break
        elif b1 == 0 or b2 == 0:
            return None

        # Switch active bucket
        state = 'one' if state == 'two' else 'two'

    # Calculate remaining liters in the other bucket
    remaining = abs(goal - b1) if state == 'one' else abs(goal - b2)

    return (actions, state, remaining)
