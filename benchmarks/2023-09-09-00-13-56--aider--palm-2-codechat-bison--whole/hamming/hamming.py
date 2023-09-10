def distance(strand_a, strand_b):
  """
  Calculates the Hamming distance between two DNA strands.

  The Hamming distance is the number of differences between two DNA strands.
  For example, the Hamming distance between the strands "GAGCCTACTAACGGGAT" and "CATCGTAATGACGGCCT" is 7.

  Args:
    strand_a: The first DNA strand.
    strand_b: The second DNA strand.

  Returns:
    The Hamming distance between the two strands.
  """

  # Check that the strands are the same length.
  if len(strand_a) != len(strand_b):
    raise ValueError("Strands must be of equal length.")

  # Calculate the Hamming distance.
  hamming_distance = 0
  for i in range(len(strand_a)):
    if strand_a[i] != strand_b[i]:
      hamming_distance += 1

  return hamming_distance
