from __future__ import unicode_literals

import pytest

from design_patterns.observer import Subject


@pytest.fixture
def subject():
    return Subject()


def test_subscribe(subject):

    result = []

    def func(*args, **kwargs):
        result.append((args, kwargs))

    subject.subscribe(func)
    subject(1, 2, 3, k1='a', k2='b')
    assert result == [((1, 2, 3), dict(k1='a', k2='b'))]

    del result[:]
    subject.subscribe(func)
    subject('test2')
    assert result == [(('test2', ), {})] * 2


def test_unsubscribe(subject):

    result_a = []

    def func_a(data):
        result_a.append(data)

    result_b = []

    def func_b(data):
        result_b.append(data)

    sid_a = subject.subscribe(func_a)
    sid_b = subject.subscribe(func_b)

    subject('data1')
    assert result_a == ['data1']
    assert result_b == ['data1']

    del result_a[:]
    del result_b[:]
    sid_a.unsubscribe()
    subject('data2')
    assert result_a == []
    assert result_b == ['data2']

    del result_a[:]
    del result_b[:]
    sid_b.unsubscribe()
    subject('data3')
    assert result_a == []
    assert result_b == []

    with pytest.raises(KeyError):
        sid_b.unsubscribe()
