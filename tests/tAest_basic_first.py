
from src.NOW.CodeSignal.c001add import add

class TestOurFirstOne():
    
    def test_firstThing(self):
        a = 5
        b = 3
        assert a + b == add.solution(a,b)