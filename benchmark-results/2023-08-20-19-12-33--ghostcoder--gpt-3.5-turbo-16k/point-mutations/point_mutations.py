import unittest

from point_mutations import hamming_distance

class PointMutationsTest(unittest.TestCase):
    def test_hamming_distance_in_off_by_one_strand(self):
        self.assertEqual(hamming_distance('GGACGGATTCTGACCTGGACTAATTTTGGGG',
                                          'GGTCGGATTCTGACCTGGACTAATTTTGGGG'), 1)

    def test_ignores_extra_length_on_original_strand_when_longer(self):
        self.assertEqual(hamming_distance('GACTACGGACAGGGTAGGGAAT',
                                          'GACATCGCACACC'), 5)

    def test_ignores_extra_length_on_other_strand_when_longer(self):
        self.assertEqual(hamming_distance('AAACTAGGGG',
                                          'AGGCTAGCGGTAGGAC'), 3)

if __name__ == '__main__':
    unittest.main()