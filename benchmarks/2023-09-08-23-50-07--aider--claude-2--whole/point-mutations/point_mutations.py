def hamming_distance(dna_strand_1, dna_strand_2):
  if len(dna_strand_1) != len(dna_strand_2):
    raise ValueError("DNA strands must be of equal length.")

  shorter_strand_length = min(len(dna_strand_1), len(dna_strand_2))
    
  distance = 0
  for i in range(shorter_strand_length):
    if dna_strand_1[i] != dna_strand_2[i]:
      distance += 1

  return distance
