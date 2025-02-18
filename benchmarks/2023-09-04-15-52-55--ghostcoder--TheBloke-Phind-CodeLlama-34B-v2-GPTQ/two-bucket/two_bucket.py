class Buckets:
    def __init__(self, capacity1, capacity2):
        self.capacity1 = capacity1
        self.capacity2 = capacity2

    def measure(self, goal, start_bucket):
        # Initialize the buckets with 0 liters
        bucket1 = 0
        bucket2 = 0

        # Determine which bucket to fill first based on the 'start_bucket' parameter
        if start_bucket == 'bucket1':
            bucket1 = self.capacity1
        else:
            bucket2 = self.capacity2

        # Start the process of pouring
        while True:
            # If we have reached the goal, stop pouring
            if bucket1 == goal or bucket2 == goal:
                break

            # Otherwise, keep pouring
            else:
                if start_bucket == 'bucket1':
                    if bucket1 >= self.capacity1:
                        bucket1 -= self.capacity1
                        bucket2 += self.capacity1
                    elif bucket2 > 0 and bucket2 != self.capacity2:
                        bucket2 -= min(self.capacity2 - bucket2, bucket1)
                        bucket1 = self.capacity1
                    else:
                        bucket1 = self.capacity1
                else:
                    if bucket2 >= self.capacity2:
                        bucket2 -= self.capacity2
                        bucket1 += self.capacity2
                    elif bucket1 > 0 and bucket1 != self.capacity1:
                        bucket1 -= min(self.capacity1 - bucket1, bucket2)
                        bucket2 = self.capacity2
                    else:
                        bucket2 = self.capacity2

        # Return the final status of the buckets along with the number of steps taken
        return ((bucket1, bucket2), abs((goal - bucket1) + (goal - bucket2)))