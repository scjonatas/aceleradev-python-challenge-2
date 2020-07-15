from main import Manager, Employee, Seller
import pytest


class TestChalange2:

    def test_employer_class(self):
        with pytest.raises(TypeError):
            Employee(123, 123, 123)

    def test_manager_class(self):
        manager = Manager(123, 123, 123)
        with pytest.raises(AttributeError):
            manager.departament.name

    def test_seller_class(self):
        seller = Seller(123, 123, 123)
        with pytest.raises(AttributeError):
            seller.departament.name = 'coders'

    def test_get_department_manager(self):
        manager = Manager(123, 123, 123)
        assert manager.get_department() == Manager.DEFAULT_DEPARTMENT_NAME

    def test_get_department_seller(self):
        seller = Seller(123, 123, 123)
        assert seller.get_department() == Seller.DEFAULT_DEPARTMENT_NAME

    def test_calc_bonus_manager(self):
        salary = 123
        manager = Manager(123, 123, 123)
        assert manager.calc_bonus() == salary * (Manager.PERCENT_BONUS / 100)

    def test_calc_bonus_seller(self):
        seller = Seller(123, 123, 123)
        seller.put_sales(5.65)
        assert seller.calc_bonus() == seller.get_sales() * (seller.PERCENT_BONUS / 100)

    def test_get_sales(self):
        seller = Seller(123, 123, 123)
        with pytest.raises(AttributeError):
            seller.sales == 0

        previous_sales_value = seller.get_sales()
        sales = 1.99
        seller.put_sales(sales)
        assert seller.get_sales() == previous_sales_value + sales
