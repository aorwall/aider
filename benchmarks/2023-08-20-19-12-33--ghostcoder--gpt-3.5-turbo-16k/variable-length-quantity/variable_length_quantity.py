def test_arbitrary_double_byte(self):
    self.assertEqual(encode([0x2000]), [0xC0, 0x00])

def test_arbitrary_quadruple_byte(self):
    self.assertEqual(encode([0x8000000]), [0xC0, 0x80, 0x80, 0x00])

def test_arbitrary_quintuple_byte(self):
    self.assertEqual(encode([0xFF000000]), [0x8F, 0xF8, 0x80, 0x80, 0x00])

def test_arbitrary_triple_byte(self):
    self.assertEqual(encode([0x4000]), [0x81, 0x80, 0x00])