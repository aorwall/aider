def measure(bucket_one_capacity, bucket_two_capacity, goal, start_bucket):
    def fill_bucket(size, target):
        return size - target

    def empty_bucket(size, target):
        return 0

    def pour_buckets(size1, size2, target1, target2):
        amount = min(size1, size2 - target2)
        target1 += amount
        target2 += amount
        size1 -= amount
        size2 -= amount

        if target1 == target2:
            return (target1, target2), 'equal', None
        elif target1 > target2:
            return (target1, target2), 'pour_to_two', (size1, size2 + amount)
        else:
            return (target1, target2), 'pour_to_one', (size1 + amount, size2)

    def backtrack(history, current_state, steps):
        action, previous_state = history[-1]
        del history[-1]
        if previous_state[0] < bucket_one_capacity and previous_state[1] < bucket_two_capacity:
            if action == 'fill_one':
                new_state = (previous_state[0], bucket_two_capacity)
            elif action == 'fill_two':
                new_state = (bucket_one_capacity, previous_state[1])
            elif action == 'empty_one':
                new_state = (0, previous_state[1])
            else:
                new_state = (previous_state[0], 0)

            if new_state not in history:
                history.append((action, new_state))
                return backtrack(history, new_state, steps+1)
            else:
                raise ValueError("Invalid state transition")
        else:
            return steps, history

    start_bucket_capacity = bucket_one_capacity if start_bucket == "one" else bucket_two_capacity
    start_state = (0, 0)
    if start_bucket == "one":
        start_state = (start_bucket_capacity, 0)
    else:
        start_state = (0, start_bucket_capacity)

    states = [(start_state, [])]
    visited = set()
    while states:
        current_state, history = states.pop(0)
        target1, target2 = current_state
        if target1 == goal or target2 == goal:
            return backtrack(history, current_state, len(history))

        if current_state not in visited:
            visited.add(current_state)
            actions = []
            if target1 < bucket_one_capacity:
                actions.append('fill_one')
            if target2 < bucket_two_capacity:
                actions.append('fill_two')
            if target1 > 0:
                actions.append('pour_to_two')
            if target2 > 0:
                actions.append('pour_to_one')

            for action in actions:
                if action == 'fill_one':
                    new_state = fill_bucket(*current_state)
                elif action == 'fill_two':
                    new_state = fill_bucket(*current_state[::-1])
                else:
                    new_state, next_action, _ = pour_buckets(*current_state, *current_state)

                if new_state is None:
                    continue

                new_history = history + [(action, new_state)]
                states.insert(0, (new_state, new_history))

    raise ValueError("No solution found")