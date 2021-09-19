import pytest

class NotInRange(Exception):
    def __init__(self, msg='value not in range'):
        self.msg = msg
        super().__init__(self.msg)

def test_generic():
    a, b = 2,2
    with pytest.raises(NotInRange):
        if a not in range(10,15):
            raise NotInRange
    assert a == b