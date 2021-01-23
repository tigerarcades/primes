from tigerarcades.primes import lib


def test_is_prime():
    assert lib.is_prime(2)
    assert lib.is_prime(3)
    assert not lib.is_prime(4)
    assert lib.is_prime(5)
    assert not lib.is_prime(6)
    assert lib.is_prime(7)
    assert not lib.is_prime(8)
    assert not lib.is_prime(9)
