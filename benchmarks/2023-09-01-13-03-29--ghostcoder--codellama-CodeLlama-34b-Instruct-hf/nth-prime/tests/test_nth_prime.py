def test_prime():
    assert prime(1) == 2
    assert prime(2) == 3
    assert prime(3) == 5
    assert prime(4) == 7
    assert prime(5) == 11
    assert prime(6) == 13
    with pytest.raises(ValueError):
        prime(0)