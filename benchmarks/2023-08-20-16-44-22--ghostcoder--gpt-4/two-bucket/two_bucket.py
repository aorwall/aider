from collections import deque

def measure(bucket_one, bucket_two, goal, start_bucket):
    # Define the initial state
    if start_bucket == 'one':
        initial_state = (bucket_one, 0)
    else:
        initial_state = (0, bucket_two)

    # Use a queue to store the states to visit
    queue = deque([(initial_state, 1)])

    # Use a set to store the visited states
    visited = set([initial_state])

    while queue:
        # Get the current state and the number of actions
        (bucket_one_content, bucket_two_content), actions = queue.popleft()

        # Check if we have reached the goal
        if bucket_one_content == goal:
            return actions, 'one', bucket_two_content
        if bucket_two_content == goal:
            return actions, 'two', bucket_one_content

        # Generate the next states
        next_states = [
            (bucket_one, bucket_two_content),  # Fill bucket one
            (bucket_one_content, bucket_two),  # Fill bucket two
            (0, bucket_two_content),  # Empty bucket one
            (bucket_one_content, 0),  # Empty bucket two
            # Pour from bucket one to bucket two
            (max(bucket_one_content - (bucket_two - bucket_two_content), 0), min(bucket_two, bucket_two_content + bucket_one_content)),
            # Pour from bucket two to bucket one
            (min(bucket_one, bucket_one_content + bucket_two_content), max(bucket_two_content - (bucket_one - bucket_one_content), 0))
        ]

        for state in next_states:
            # Check if the next state violates the rule
            if start_bucket == 'one' and state == (0, bucket_two):
                continue
            if start_bucket == 'two' and state == (bucket_one, 0):
                continue

            if state not in visited:
                queue.append((state, actions + 1))
                visited.add(state)

    raise ValueError("It is not possible to reach the goal.")