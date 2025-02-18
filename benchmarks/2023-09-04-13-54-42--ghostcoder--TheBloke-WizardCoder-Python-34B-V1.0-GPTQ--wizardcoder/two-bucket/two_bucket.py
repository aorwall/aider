class Buckets:
    def __init__(self, size_one, size_two):
        self.size_one = size_one
        self.size_two = size_two
        self.buckets = {
            'one': {'volume': 0, 'capacity': size_one},
            'two': {'volume': 0, 'capacity': size_two}
        }

    def pour(self, from_bucket, to_bucket):
        free_space = self.buckets[to_bucket]['capacity'] - self.buckets[to_bucket]['volume']
        transferred_liquid = min(free_space, self.buckets[from_bucket]['volume'])
        self.buckets[from_bucket]['volume'] -= transferred_liquid
        self.buckets[to_bucket]['volume'] += transferred_liquid

    def fill(self, bucket):
        self.buckets[bucket]['volume'] = self.buckets[bucket]['capacity']

    def empty(self, bucket):
        self.buckets[bucket]['volume'] = 0

    def get_goal_status(self, goal, start_bucket):
        current_bucket = start_bucket
        while True:
            if self.buckets[current_bucket]['volume'] == goal:
                return current_bucket

            # Check if we need to switch buckets
            if self.buckets[current_bucket]['volume'] == 0:
                current_bucket = 'one' if current_bucket == 'two' else 'two'

            # Perform actions based on the current volume levels
            if self.buckets['one']['volume'] == 0:
                self.fill('one')
            elif self.buckets['two']['volume'] == 0:
                self.fill('two')
            else:
                self.pour(current_bucket, 'one' if current_bucket == 'two' else 'two')

def measure(bucket_one, bucket_two, goal, start_bucket='one'):
    if start_bucket not in ['one', 'two']:
        raise ValueError("Invalid value for start_bucket. Must be either 'one' or 'two'.")

    buckets = Buckets(bucket_one, bucket_two)
    final_bucket = buckets.get_goal_status(goal, start_bucket)
    remaining_liters = buckets.buckets[start_bucket]['capacity'] - buckets.buckets[start_bucket]['volume']

    return {
        'total_actions': buckets.buckets['one']['volume'] + buckets.buckets['two']['volume'],
        'final_bucket': final_bucket,
        'remaining_liters': remaining_liters
    }

def measure(bucket_one, bucket_two, goal, start_bucket):
    if start_bucket != 'one' and start_bucket != 'two':
        raise ValueError("Invalid value for start_bucket. Must be either 'one' or 'two'.")

    buckets = Buckets(bucket_one, bucket_two)
    final_bucket = buckets.get_goal_status(goal, start_bucket)
    remaining_liters = buckets.buckets[start_bucket]['capacity'] - buckets.buckets[start_bucket]['volume']

    return {
        'total_actions': buckets.buckets['one']['volume'] + buckets.buckets['two']['volume'],
        'final_bucket': final_bucket,
        'remaining_liters': remaining_liters
    }
