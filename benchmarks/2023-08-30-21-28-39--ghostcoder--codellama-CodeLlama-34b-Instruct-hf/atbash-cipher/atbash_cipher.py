def test_encode_decode():
    plain_text = "test"
    cipher_text = encode(plain_text)
    assert cipher_text == "gvhg"
    assert decode(cipher_text) == plain_text

    plain_text = "x123 yes"
    cipher_text = encode(plain_text)
    assert cipher_text == "c123b vh"
    assert decode(cipher_text) == plain_text

    plain_text = "gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt"
    cipher_text = encode(plain_text)
    assert cipher_text == "thequickbrownfoxjumpsoverthelazydog"
    assert decode(cipher_text) == plain_text