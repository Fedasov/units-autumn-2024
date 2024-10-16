import unittest
from src.calculator import Calculator
import math


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add_integers(self):
        # Тесты с целыми числами
        self.assertEqual(self.calculator.addition(1, 2), 3)
        self.assertEqual(self.calculator.addition(2, 2), 4)
        self.assertEqual(self.calculator.addition(1, 0), 1)
        self.assertEqual(self.calculator.addition(0, 0), 0)

    def test_add_fractional(self):
        # Тесты с числами с плавающей точкой
        self.assertEqual(self.calculator.addition(1.2, 2.3), 3.5)
        self.assertEqual(self.calculator.addition(1.2, 2), 3.2)
        self.assertEqual(self.calculator.addition(1.2, 0), 1.2)

    def test_add_negative(self):
        # Тесты с отрицательными числами
        self.assertEqual(self.calculator.addition(-1, -2), -3)
        self.assertEqual(self.calculator.addition(-1, -1.2), -2.2)
        self.assertEqual(self.calculator.addition(-1, 0), -1)
        self.assertEqual(self.calculator.addition(-1, 1), 0)

    def test_add_infinity(self):
        # Тесты с бесконечностью
        self.assertTrue(math.isnan(self.calculator.addition(math.inf, -math.inf)))
        self.assertEqual(self.calculator.addition(math.inf, math.inf), math.inf)
        self.assertEqual(self.calculator.addition(math.inf, 2), math.inf)
        self.assertEqual(self.calculator.addition(math.inf, -1), math.inf)

    def test_add_string(self):
        # Тесты со строками
        self.assertEqual(self.calculator.addition("a", "a"), "aa")
        self.assertEqual(self.calculator.addition("a", ""),"a")
        
    def test_add_list(self):
        # Тесты с массивами
        self.assertEqual(self.calculator.addition(['a'], ['a']), ['a', 'a'])
        self.assertEqual(self.calculator.addition(['a'], []), ['a'])

    def test_add_exception(self):
        # Тесты на исключения при неправильных типах данных
        with self.assertRaises(TypeError):
            self.calculator.addition(2, [1, 2])
            self.calculator.addition("a", [1, 2])
            self.calculator.addition("hello", 1)

    def test_multiply_integers(self):
        # Тесты с целыми числами
        self.assertEqual(self.calculator.multiplication(1, 2), 2)
        self.assertEqual(self.calculator.multiplication(2, 2), 4)

    def test_multiply_fractional(self):
        # Тесты с числами с плавающей точкой
        self.assertEqual(self.calculator.multiplication(1.2, 2), 2.4)
        self.assertEqual(self.calculator.multiplication(1.2, 2.3), 2.76)
        self.assertEqual(self.calculator.multiplication(1.2, -2.3), -2.76)

    def test_multiply_zero(self):
        # Тесты с нулем
        self.assertEqual(self.calculator.multiplication(0, 2), 0)
        self.assertEqual(self.calculator.multiplication(1, 0), 0)
        self.assertEqual(self.calculator.multiplication(-1, 0), 0)
        self.assertEqual(self.calculator.multiplication(0, 0), 0)

    def test_multiply_negative(self):
        # Тесты с отрицательными числами
        self.assertEqual(self.calculator.multiplication(-1, 2), -2)
        self.assertEqual(self.calculator.multiplication(-1, -2), 2)
        self.assertEqual(self.calculator.multiplication(-1.2, 2), -2.4)
        self.assertEqual(self.calculator.multiplication(-1.2, -2.3), 2.76)

    def test_multiply_infinity(self):
        # Тесты с бесконечностью
        self.assertTrue(math.isnan((self.calculator.multiplication(math.inf, 0))))
        self.assertEqual(self.calculator.multiplication(math.inf, 2), math.inf)
        self.assertEqual(self.calculator.multiplication(math.inf, -1), -math.inf)
        self.assertEqual(self.calculator.multiplication(math.inf, math.inf), math.inf)
        self.assertEqual(self.calculator.multiplication(-math.inf, math.inf), -math.inf)

    def test_multiply_exception(self):
        # Тест на исключения
        with self.assertRaises(TypeError):
            self.calculator.multiplication(2, [1, 2])
            self.calculator.multiplication("a", [1, 2])
            self.calculator.multiplication("hello", 1)
            self.calculator.multiplication("hello", "world")

    def test_subtract_integers(self):
        # Тесты с целыми числами
        self.assertEqual(self.calculator.subtraction(2, 1), 1)
        self.assertEqual(self.calculator.subtraction(2, 2), 0)
        self.assertEqual(self.calculator.subtraction(1, 0), 1)
        self.assertEqual(self.calculator.subtraction(0, 0), 0)

    def test_subtract_fractional(self):
        # Тесты с числами с плавающей точкой
        self.assertEqual(self.calculator.subtraction(2.6, 1.1), 1.5)
        self.assertEqual(self.calculator.subtraction(2.0, 1.2), 0.8)
        self.assertEqual(self.calculator.subtraction(1.2, 0), 1.2)

    def test_subtract_negative(self):
        # Тесты с отрицательными числами
        self.assertEqual(self.calculator.subtraction(-1, -2), 1)
        self.assertEqual(self.calculator.subtraction(-2.6, -1.3), -1.3)
        self.assertEqual(self.calculator.subtraction(-1, 0), -1)
        self.assertEqual(self.calculator.subtraction(-1, 1), -2)

    def test_subtract_infinity(self):
        # Тесты с бесконечностью
        self.assertTrue(math.isnan(self.calculator.subtraction(math.inf, math.inf)))
        self.assertEqual(self.calculator.subtraction(math.inf, -math.inf), math.inf)
        self.assertEqual(self.calculator.subtraction(-math.inf, math.inf), -math.inf)

    def test_subtract_exception(self):
        # Тесты на исключения при неправильных типах данных
        with self.assertRaises(TypeError):
            self.calculator.subtraction(2, [1, 2])
            self.calculator.subtraction("a", 1)
            self.calculator.subtraction("hello", [1, 2])

    def test_division_integers(self):
        # Тесты с целыми числами
        self.assertEqual(self.calculator.division(6, 2), 3)
        self.assertEqual(self.calculator.division(5, 2), 2.5)
        self.assertEqual(self.calculator.division(0, 1), 0)

    def test_division_fractional(self):
        # Тесты с числами с плавающей точкой
        self.assertEqual(self.calculator.division(5.5, 2), 2.75)
        self.assertEqual(self.calculator.division(7.2, 3.6), 2.0)

    def test_division_negative(self):
        # Тесты с отрицательными числами
        self.assertEqual(self.calculator.division(-6, 2), -3)
        self.assertEqual(self.calculator.division(-5, -2), 2.5)
        self.assertEqual(self.calculator.division(6, -3), -2)

    def test_division_infinity(self):
        # Тесты с бесконечностью
        self.assertTrue(math.isnan(self.calculator.division(math.inf, math.inf)))
        self.assertEqual(self.calculator.division(math.inf, 2), math.inf)
        self.assertEqual(self.calculator.division(-math.inf, -2), math.inf)

    def test_division_by_zero(self):
        # Тесты на исключение при делении на ноль
        self.assertEqual(self.calculator.division(1, 0), None)
        self.assertEqual(self.calculator.division(0, 0), None)

    def test_division_periodic(self):
        # Тесты с числом в периоде
        self.assertEqual(self.calculator.division(1, 3), float(1 / 3))
        self.assertEqual(self.calculator.division(1, -3), -float(1 / 3))

    def test_division_exception(self):
        # Тесты на исключения при неправильных типах данных
        with self.assertRaises(TypeError):
            self.calculator.division(2, [1, 2])
            self.calculator.division("a", 1)
            self.calculator.division("hello", [1, 2])

    def test_absolute_positive(self):
        # Тесты с положительными числами
        self.assertEqual(self.calculator.absolute(5), 5)
        self.assertEqual(self.calculator.absolute(1.23), 1.23)

    def test_absolute_negative(self):
        # Тесты с отрицательными числами
        self.assertEqual(self.calculator.absolute(-5), 5)
        self.assertEqual(self.calculator.absolute(-1.23), 1.23)

    def test_absolute_zero(self):
        # Тесты с нулем
        self.assertEqual(self.calculator.absolute(0), 0)

    def test_absolute_infinity(self):
        # Тесты с бесконечностью
        self.assertEqual(self.calculator.absolute(math.inf), math.inf)
        self.assertEqual(self.calculator.absolute(-math.inf), math.inf)

    def test_absolute_invalid_types(self):
        # Тесты на исключения при неправильных типах данных
        with self.assertRaises(TypeError):
            self.calculator.absolute([1, 2])
            self.calculator.absolute("a")
            self.calculator.absolute("hello")

    def test_degree_positive(self):
        # Тесты с положительными числами
        self.assertEqual(self.calculator.degree(2, 3), 8)
        self.assertEqual(self.calculator.degree(5, 2), 25)
        self.assertEqual(self.calculator.degree(10, 1), 10)
        self.assertEqual(self.calculator.degree(7, 0), 1)

    def test_degree_negative(self):
        # Тесты с отрицательными числами
        self.assertEqual(self.calculator.degree(-2, 3), -8)
        self.assertEqual(self.calculator.degree(-2, 2), 4)
        self.assertEqual(self.calculator.degree(-5, 1), -5)
        self.assertEqual(self.calculator.degree(-5, 0), 1)

    def test_degree_float(self):
        # Тесты с числами с плавающей точкой
        self.assertEqual(self.calculator.degree(2.5, 2), 6.25)
        self.assertEqual(self.calculator.degree(9, 0.5), 3)

    def test_degree_infinity(self):
        # Тесты с бесконечностью
        self.assertEqual(self.calculator.degree(math.inf, 2), math.inf)
        self.assertEqual(self.calculator.degree(math.inf, -1), 0)
        self.assertEqual(self.calculator.degree(1, math.inf), 1)
        self.assertEqual(self.calculator.degree(0, math.inf), 0)

    def test_degree_invalid_types(self):
        # Тесты на исключения при неправильных типах данных
        with self.assertRaises(TypeError):
            self.calculator.degree(2, [1, 2])
            self.calculator.degree("a", 2)
            self.calculator.degree(2, "b")

    def test_ln_positive(self):
        # Тесты с положительными числами
        self.assertEqual(self.calculator.ln(1), 0)
        self.assertEqual(self.calculator.ln(math.e), 1)
        self.assertAlmostEqual(self.calculator.ln(10), 2.302585, places=6)

    def test_ln_float(self):
        # Тесты с числами с плавающей точкой
        self.assertAlmostEqual(self.calculator.ln(2.71828), 0.999999, places=6)

    def test_ln_infinity(self):
        # Тесты с бесконечностью
        self.assertEqual(self.calculator.ln(math.inf), math.inf)

    def test_ln_exceptions(self):
        # Тесты на исключения для недопустимых значений
        with self.assertRaises(ValueError):
            self.calculator.ln(0)
            self.calculator.ln(-1)

    def test_ln_type_exceptions(self):
        # Тесты на исключения при неправильных типах данных
        with self.assertRaises(TypeError):
            self.calculator.ln("a")
            self.calculator.ln([1, 2])

    def test_log_base_10(self):
        # Тесты логарифма по основанию 10
        self.assertEqual(self.calculator.log(1, 10), 0)
        self.assertEqual(self.calculator.log(10, 10), 1)
        self.assertAlmostEqual(self.calculator.log(100, 10), 2, places=6)

    def test_log_base_2(self):
        # Тесты логарифма по основанию 2
        self.assertEqual(self.calculator.log(8, 2), 3)
        self.assertAlmostEqual(self.calculator.log(5.5, 2), 2.459432, places=6)

    def test_log_with_e(self):
        # Тесты логарифма по основанию e
        self.assertAlmostEqual(self.calculator.log(2.71828, math.e), 1, places=5)

    def test_log_infinity(self):
        # Тесты логарифма для бесконечности
        self.assertEqual(self.calculator.log(math.inf, 10), math.inf)

    def test_log_exceptions(self):
        # Тесты на исключения для недопустимых значений
        with self.assertRaises(ValueError):
            self.calculator.log(0, 10)
            self.calculator.log(-1, 10)
            self.calculator.log(10, -2)
            self.calculator.log(10, 1)
            self.calculator.log(10, 0)

    def test_log_type_exceptions(self):
        # Тесты на исключения для неверных типов данных
        with self.assertRaises(TypeError):
            self.calculator.log("a", 10)
            self.calculator.log(10, "b")
            self.calculator.log([1, 2], 10)

    def test_sqrt_positive(self):
        # Тесты для положительных чисел
        self.assertEqual(self.calculator.sqrt(4), 2)
        self.assertEqual(self.calculator.sqrt(9), 3)
        self.assertAlmostEqual(self.calculator.sqrt(2), 1.414214, places=6)
        self.assertAlmostEqual(self.calculator.sqrt(4.5), 2.12132034)

    def test_sqrt_zero_one(self):
        # Тесты для нуля и единицы
        self.assertAlmostEqual(self.calculator.sqrt(0), 0)
        self.assertEqual(self.calculator.sqrt(1), 1)

    def test_sqrt_infinity(self):
        # Тесты для бесконечности
        self.assertEqual(self.calculator.sqrt(math.inf), math.inf)

    def test_sqrt_negative_number(self):
        # Тесты для отрицательных чисел
        self.assertAlmostEqual(self.calculator.sqrt(-1), 1j)

    def test_sqrt_exceptions(self):
        # Тесты на исключения для недопустимых типов
        with self.assertRaises(TypeError):
            self.calculator.sqrt("a")
            self.calculator.sqrt([1, 2])

    def test_nth_root_positive_integers(self):
        # Тесты для положительных целых чисел
        self.assertEqual(self.calculator.nth_root(27, 3), 3)
        self.assertEqual(self.calculator.nth_root(16, 4), 2)
        self.assertAlmostEqual(self.calculator.nth_root(81, 4), 3, places=6)

    def test_nth_root_square_root(self):
        # Тесты для квадратного корня
        self.assertAlmostEqual(self.calculator.nth_root(2, 2), 1.414214, places=6)
        self.assertEqual(self.calculator.nth_root(0, 5), 0)
        self.assertEqual(self.calculator.nth_root(1, 10), 1)

    def test_nth_root_decimal_numbers(self):
        # Тесты для вещественных чисел
        self.assertAlmostEqual(self.calculator.nth_root(27.5, 4), 2.2899878)
        self.assertAlmostEqual(self.calculator.nth_root(27, 4.5), 2.0800838)

    def test_nth_root_infinity(self):
        # Тесты для бесконечности
        self.assertEqual(self.calculator.nth_root(math.inf, 2), math.inf)

    def test_nth_root_zero_division(self):
        # Тест на деление на ноль
        with self.assertRaises(ZeroDivisionError):
            self.calculator.nth_root(1, 0)

    def test_nth_root_type_errors(self):
        # Тесты на типовые ошибки
        with self.assertRaises(TypeError):
            self.calculator.nth_root("a", 2)
            self.calculator.nth_root(2, "b")
            self.calculator.nth_root([1, 2], 2)


if __name__ == "__main__":
    unittest.main()
