from collections import deque

def measure(bucket_one, bucket_two, goal, start_bucket):
    # Initialize the queue and the set of visited states
    queue = deque()
    visited = set()

    # Determine the initial state
    if start_bucket == 'one':
        initial_state = (bucket_one, 0, 1)
    else:
        initial_state = (0, bucket_two, 1)

    # Add the initial state to the queue and the set of visited states
    queue.append(initial_state)
    visited.add(initial_state[:2])

    while queue:
        # Take a state from the queue
        bucket_one_content, bucket_two_content, steps = queue.popleft()

        # Check if we have reached the goal
        if bucket_one_content == goal:
            return (steps, 'one', bucket_two_content)
        if bucket_two_content == goal:
            return (steps, 'two', bucket_one_content)

        # Generate all possible next states
        next_states = [
            # Fill bucket one
            (bucket_one, bucket_two_content, steps + 1),
            # Fill bucket two
            (bucket_one_content, bucket_two, steps + 1),
            # Empty bucket one
            (0, bucket_two_content, steps + 1),
            # Empty bucket two
            (bucket_one_content, 0, steps + 1),
            # Pour from bucket one to bucket two
            (bucket_one_content - min(bucket_one_content, bucket_two - bucket_two_content),
             bucket_two_content + min(bucket_one_content, bucket_two - bucket_two_content), steps + 1),
            # Pour from bucket two to bucket one
            (bucket_one_content + min(bucket_two_content, bucket_one - bucket_one_content),
             bucket_two_content - min(bucket_two_content, bucket_one - bucket_one_content), steps + 1)
        ]

        # Add the next states to the queue and the set of visited states
        for next_state in next_states:
            if next_state[:2] not in visited:
                queue.append(next_state)
                visited.add(next_state[:2])
