def count(strand, nucleotide):
  if nucleotide not in ['A', 'C', 'G', 'T']:
    raise ValueError('Invalid nucleotide: ' + nucleotide)
  return strand.count(nucleotide)


def nucleotide_counts(strand):
  if any(nucleotide not in ['A', 'C', 'G', 'T'] for nucleotide in strand):
    raise ValueError('Invalid nucleotides in strand')
  
  counts = {}
  for nucleotide in ['A', 'C', 'G', 'T']:
    counts[nucleotide] = count(strand, nucleotide)
  return counts
