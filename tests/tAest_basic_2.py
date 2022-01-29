
from src.NOW.CodeSignal.c001add import add

class TestOur2():
    
    def test_2(self):
        a = 5
        b = 3
        assert a + b == add.solution(a,b)