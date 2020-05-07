# https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/
from typing import List
import unittest


class Solution:
    def removeSubfolders(self, folders: List[str]) -> List[str]:
        folders.sort()

        for idx, folder in enumerate(folders):
            for other_folder in folders[idx+1:]:
                if self.isSubdirectory(folder, other_folder):
                    folders.remove(other_folder)
        return folders

    def isSubdirectory(self, folder: str, other_folder: str):
        if folder not in other_folder:
            return False

        other_directories = other_folder.split('/')
        for idx, directory in enumerate(folder.split('/')):
            if directory != other_directories[idx]:
                return False

        return True
    

class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_example_case(self):
        folders = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
        expected = ["/a","/c/d","/c/f"]
        self.assertEqual(self.solution.removeSubfolders(folders), expected)

    def test_example_case_2(self):
        folders = ["/a","/a/b/c","/a/b/d"]
        expected = ["/a"]
        self.assertEqual(self.solution.removeSubfolders(folders), expected)

    def test_gotcha(self):
        folders = ["/a/b/c","/a/b/ca","/a/b/d"]
        expected = ["/a/b/c","/a/b/ca","/a/b/d"]
        # I should really tokenize this
        self.assertEqual(self.solution.removeSubfolders(folders), expected)

    def test_gotcha_2(self):
        folders = ["/ad","/ad/af","/aa"]
        expected = ["/aa","/ad"]
        self.assertEqual(self.solution.removeSubfolders(folders), expected)


if __name__ == '__main__':
    unittest.main()
