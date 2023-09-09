codon_table = {
  'AUG': 'Methionine',  
  'UUU': 'Phenylalanine',
  'UUC': 'Phenylalanine',
  'UUA': 'Leucine',
  'UUG': 'Leucine',
  'UCU': 'Serine',
  'UCC': 'Serine', 
  'UCA': 'Serine',
  'UCG': 'Serine',
  'UAU': 'Tyrosine',
  'UAC': 'Tyrosine',
  'UGU': 'Cysteine',
  'UGC': 'Cysteine',
  'UGG': 'Tryptophan',
  'UAA': 'STOP',
  'UAG': 'STOP',
  'UGA': 'STOP'
}

def proteins(rna):
  proteins = []
  i = 0
  while i < len(rna):
    codon = rna[i:i+3]
    if codon in codon_table:
      if codon_table[codon] == 'STOP':
        return proteins
      else:
        proteins.append(codon_table[codon])
      i += 3
    else:
      return "Invalid codon encountered"
  return proteins
