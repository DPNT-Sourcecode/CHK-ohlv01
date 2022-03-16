from solutions.HLO import hello_solution



class TestSum():

    def test_hlo(self):
        assert hello_solution.hello(None) == "Hello, World!"

