from selekta.student_pick import choose


def test_choose():
    actual = choose(0, 11)
    expected = list(range(11))
    assert sorted(actual) == expected

