from solutions.CHK import checkout_solution


# +------+-------+------------------------+
# | Item | Price | Special offers         |
# +------+-------+------------------------+
# | A    | 50    | 3A for 130, 5A for 200 |
# | B    | 30    | 2B for 45              |
# | C    | 20    |                        |
# | D    | 15    |                        |
# | E    | 40    | 2E get one B free      |
# +------+-------+------------------------+

class TestCHK1():

    def test_chk(self):
        assert checkout_solution.checkout(skus='CDAAABAB') == 20 + 15 + 130 + 50 + 45

    # def test_chk1(self):
    #     assert checkout_solution.checkout(skus='CDAAABABB') == 20 + 15 + 130 + 50 + 45 + 30
    #
    # def test_chk2(self):
    #     assert checkout_solution.checkout(skus='CDAAABABBE') == -1
    #
    # def test_chk3(self):
    #     assert checkout_solution.checkout(skus='') == -1
    #
    # def test_chk4(self):
    #     assert checkout_solution.checkout(skus=None) == -1
    #
    # def test_chk5(self):
    #     assert checkout_solution.checkout(skus='ABCDABCD') == 215 # 100 (Ax2) + 45 (Bx2) + 40 (Cx2) + 30 (Dx2)
    #
    # def test_chk6(self):
    #     assert checkout_solution.checkout(skus='BABDDCAC') == 215
    #
    # def test_chk7(self):
    #     assert checkout_solution.checkout(skus='CDAAABABA') == 20 + 15 + 200 + 45

    def test_chk_8(self):
        assert checkout_solution.checkout(skus='CDAAABABBEE') == 20 + 15 + 130 + 50 + 45 + 80
