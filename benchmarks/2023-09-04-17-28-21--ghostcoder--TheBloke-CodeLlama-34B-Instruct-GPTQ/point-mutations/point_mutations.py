def hamming_distance(dna_strand_1, dna_strand_2):
    # Check if the input strings are empty
    if not dna_strand_1 or not dna_strand_2:
        raise ValueError("Input strings cannot be empty")

    # Check if the input strings are of same length
    if len(dna_strand_1) != len(dna_strand_2):
        raise ValueError("Input strings must be of same length")

    # Initialize the counter variable
    count = 0

    # Iterate over each character in the input strings
    for i in range(len(dna_strand_1)):
        # If the characters at current position are unequal, increment the counter
        if dna_strand_1[i] != dna_strand_2[i]:
            count += 1

    # Return the final value of the counter
    return count
