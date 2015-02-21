from __future__ import unicode_literals

from design_patterns.singleton import singleton


def test_singleton():

    created = []

    @singleton
    class MockObj(object):
        def __init__(self):
            created.append(self)

    # make sure the object was created correctly
    obj = MockObj()
    assert 1 == len(created)
    assert obj == created[0]

    # make sure only one object will be created
    new_obj = MockObj()
    assert id(obj) == id(new_obj)
    assert 1 == len(created)
