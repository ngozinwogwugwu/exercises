# https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/
from typing import List
from collections import defaultdict
import unittest


class Solution:
    def removeSubfolders(self, folders: List[str]) -> List[str]:
        folders.sort()

        directory_sets = defaultdict(list)
        for folder in folders:
            directory = folder.split('/')[1:]
            directory_sets[directory[0]].append(directory)

        top_directories = []
        for (_, full_paths) in directory_sets.items():
            for idx, full_path in enumerate(full_paths):
                for other_path in full_paths[idx + 1:]:
                    if self.isSubdirectory(full_path, other_path):
                        full_paths.remove(other_path)

            top_directories += full_paths

        filtered_folders = []
        for top_dir in top_directories:
            filtered_folders.append('/' + '/'.join(top_dir))

        return filtered_folders

    def isSubdirectory(self, path: List[str], other_path: List[str]):
        for idx, directory in enumerate(path):
            if directory != other_path[idx]:
                return False

        return True


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_example_case(self):
        folders = ["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]
        expected = ["/a", "/c/d", "/c/f"]
        self.assertEqual(self.solution.removeSubfolders(folders), expected)

    def test_example_case_2(self):
        folders = ["/a", "/a/b/c", "/a/b/d"]
        expected = ["/a"]
        self.assertEqual(self.solution.removeSubfolders(folders), expected)

    def test_gotcha(self):
        folders = ["/a/b/c", "/a/b/ca", "/a/b/d"]
        expected = ["/a/b/c", "/a/b/ca", "/a/b/d"]
        # I should really tokenize this
        self.assertEqual(self.solution.removeSubfolders(folders), expected)

    def test_gotcha_2(self):
        folders = ["/ad", "/ad/af", "/aa"]
        expected = ["/aa", "/ad"]
        self.assertEqual(self.solution.removeSubfolders(folders), expected)


if __name__ == '__main__':
    unittest.main()
