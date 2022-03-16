from solutions.SUM import sum_solution


# def test_sum()


class TestSum():
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3
    def test_sum_1(self):
        assert sum_solution.compute(2, 2) == 4

