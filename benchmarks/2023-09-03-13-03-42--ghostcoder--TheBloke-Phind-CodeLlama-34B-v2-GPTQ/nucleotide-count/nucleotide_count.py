def validate(strand):
    valid_nucleotides = ['A', 'C', 'G', 'T']
    for nucleotide in strand:
        if nucleotide not in valid_nucleotides:
            raise ValueError('Invalid nucleotide')
def count(strand, nucleotide):
    return strand.upper().count(nucleotide)


def nucleotide_counts(strand):
    validate(strand)
    counts = {'A': count(strand, 'A'),
              'C': count(strand, 'C'),
              'G': count(strand, 'G'),
              'T': count(strand, 'T')}

    return counts
