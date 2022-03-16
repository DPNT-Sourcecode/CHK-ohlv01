from solutions.CHK import checkout_solution


# +------+-------+----------------+
# | Item | Price | Special offers |
# +------+-------+----------------+
# | A    | 50    | 3A for 130     |
# | B    | 30    | 2B for 45      |
# | C    | 20    |                |
# | D    | 15    |                |
# +------+-------+----------------+


class TestCHK1():

    def test_chk(self):
        assert checkout_solution.checkout(skus='CDAAABAB') == 20 + 15 + 130 + 50 + 45

    def test_chk1(self):
        assert checkout_solution.checkout(skus='CDAAABABB') == 20 + 15 + 130 + 50 + 45 + 30

    def test_chk2(self):
        assert checkout_solution.checkout(skus='CDAAABABBE') == -1

    def test_chk2(self):
        assert checkout_solution.checkout(skus='') == -1

    def test_chk2(self):
        assert checkout_solution.checkout(skus=None) == -1

