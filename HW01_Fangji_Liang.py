'''
Homework for 567
'''

from itertools import combinations as comb
import unittest
import math as m


def classify_triangle(a, b, c):
    '''
    This method is to examine the three parameters is 
    what kind of triangle and whether it is a triangle.
    Six kinds of triangle: RightIsosceles, Equilateral, RightScalene, Isosceles, Scalene
    and return false if the parameters can't form a triangle
    '''
    if a + b <= c or a + c <= b or b + c <= a:
        return False

    if a == b == c:
        return "Equilateral"
    else:
        temp = ''
        sides = [a, b, c]
        if a ** 2 + b ** 2 + c ** 2 == max(sides) ** 2 * 2:
                temp += "Right"
        for e in comb(sides, 2):
            if len(set(e)) == 1:
                temp += "Isosceles"
                break
        else:
            temp += "Scalene"
    return temp


def classify_triangle_bug(a, b, c):
    '''
    bug method
    '''
    if a + b <= c or a + c <= b or b + c <= a:
        return False

    temp = ''
    if a == b == c:
        temp += "Equilateral"
    sides = [a, b, c]
    if a ** 2 + b ** 2 + c ** 2 == max(sides) ** 2 * 2:
            temp += "Right"
    for e in comb(sides, 2):
        if len(set(e)) == 1:
            temp += "Isosceles"
    else:
        temp += "Scalene"
    return temp


def main():
    print(classify_triangle(1, 1, 2))
    print(classify_triangle(m.sqrt(2), m.sqrt(2), 2))
    print(classify_triangle(1, 1, 1))
    print(classify_triangle(3, 4, 5))
    print(classify_triangle(2, 2, 3))
    print(classify_triangle(2, 3, 4))


class TestTriangles(unittest.TestCase):
    '''
    Test cases for classify_triangle
    '''
    def test_classify_triangle(self):
        self.assertEqual(classify_triangle(1, 1, 2), False)
        self.assertEqual(classify_triangle(m.sqrt(2), m.sqrt(2), 2), "RightIsosceles")
        self.assertEqual(classify_triangle(1, 1, 1), "Equilateral")
        self.assertEqual(classify_triangle(3, 4, 5), "RightScalene")
        self.assertEqual(classify_triangle(2, 2, 3), "Isosceles")
        self.assertEqual(classify_triangle(2, 3, 4), "Scalene")
        self.assertEqual(classify_triangle(0, 1, 2), False)
        self.assertEqual(classify_triangle(-1, -2, 1), False)

    def test_classify_triangle_bug_1(self):
        self.assertEqual(classify_triangle_bug(m.sqrt(2), m.sqrt(2), 2), "RightIsosceles")
        self.assertEqual(classify_triangle_bug(2, 2, 3), "Isosceles")

    def test_classify_triangle_bug_2(self):
        self.assertEqual(classify_triangle_bug(1, 1, 1), "Equilateral")


if __name__ == "__main__":
    unittest.main(exit = False, verbosity = 2)
    main()

# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#         self.lanes = [a, b, c]
#         if a + b <= c or a + c <= b or b + c <= a or a*b*c == 0:
#             raise ValueError(f"{self.a}, {self.b} and {self.c} can't form a triangle.")

#     def is_right(self):
#         total = 0
#         for e in self.lanes != max(self.lanes):
#             total += e*e
#         return total == max(a, b, c) * max(a, b, c)

#     def is_equilateral(self):
#         return self.a == self.b == self.c

#     def is_scalene(self):
#         return self.a != self.b != self.c

#     def is_isosceles(self):
#         for e in comb(self.lanes, 2):
#             return len(set(e)) == 1
#     def classify_triangle(self):