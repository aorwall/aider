def count(strand, nucleotide):
  """
  Counts the number of times the given nucleotide appears in the given strand.

  Args:
    strand: A string representing a DNA sequence.
    nucleotide: A single character representing a nucleotide.

  Returns:
    The number of times the given nucleotide appears in the given strand.

  Raises:
    ValueError: If the given strand contains an invalid nucleotide.
  """

  # Check if the given nucleotide is valid.
  if nucleotide not in ["A", "C", "G", "T"]:
    raise ValueError("Invalid nucleotide: {}".format(nucleotide))

  # Count the number of times the given nucleotide appears in the given strand.
  count = 0
  for character in strand:
    if character == nucleotide:
      count += 1

  return count


def nucleotide_counts(strand):
  """
  Counts the number of times each nucleotide appears in the given strand.

  Args:
    strand: A string representing a DNA sequence.

  Returns:
    A dictionary mapping each nucleotide to the number of times it appears in the
    given strand.

  Raises:
    ValueError: If the given strand contains an invalid nucleotide.
  """

  # Check if the given strand contains an invalid nucleotide.
  if not strand:
    raise ValueError("Empty strand")

  # Count the number of times each nucleotide appears in the given strand.
  counts = {}
  for nucleotide in ["A", "C", "G", "T"]:
    counts[nucleotide] = count(strand, nucleotide)

  return counts
