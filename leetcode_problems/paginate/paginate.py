# coding challenge from yesterday
import unittest
from typing import List
from math import floor

class Solution:
    def paginate(self, selected_page: int, total_pages: int, pages_to_display: int) -> str:
        pages = self.get_pages_to_display(selected_page, total_pages, pages_to_display)
        return self.pages_list_to_string(pages, selected_page)
        

    def get_pages_to_display(self, selected_page: int, total_pages: int, pages_to_display: int) -> List[int]:
        pages = set([1, selected_page, total_pages])

        num_pages_to_left = floor((pages_to_display - len(pages))/2)
        for page in range(selected_page-num_pages_to_left, selected_page):
            if page > 0:
                pages.add(page)

        num_pages_to_right = pages_to_display - len(pages)
        for page in range(selected_page+1, selected_page+num_pages_to_right+1):
            if page < total_pages:
                pages.add(page)

        remaining_pages = pages_to_display - len(pages)
        if remaining_pages > 0:
            for page in range(selected_page-num_pages_to_left-remaining_pages, selected_page-num_pages_to_left):
                if page > 0:
                    pages.add(page)

        return list(pages)

    def pages_list_to_string(self, pages: List[int], selected_page: int) -> str:
        pages.sort()
        pages_string = ""
        previous_page = 0
        for page in pages:
            if page - previous_page > 1:
                pages_string += "... "
            previous_page = page

            if page == selected_page:
                pages_string += "[" + str(page) + "] "
            else:
                pages_string += str(page) + " "

        return pages_string[:-1]


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_example_case_1(self):
        self.assertEqual(self.solution.paginate(3, 10, 7), "1 2 [3] 4 5 6 ... 10")

    def test_example_case_2(self):
        self.assertEqual(self.solution.paginate(7, 20, 7), "1 ... 5 6 [7] 8 9 ... 20")

    def test_example_case_3(self):
        self.assertEqual(self.solution.paginate(10, 10, 7), "1 ... 5 6 7 8 9 [10]")

    def test_example_case_4(self):
        self.assertEqual(self.solution.paginate(3, 5, 7), "1 2 [3] 4 5")

    def test_example_case_5(self):
        self.assertEqual(self.solution.paginate(15, 20, 5), "1 ... 14 [15] 16 ... 20")


if __name__ == '__main__':
    unittest.main()
