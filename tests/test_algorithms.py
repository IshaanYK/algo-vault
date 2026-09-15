"""
Unit test suite for sorting, graphs, and data structures.
"""

import unittest
from algo_vault.sorting import quick_sort, merge_sort
from algo_vault.graphs import dijkstra, has_cycle
from algo_vault.trees import FenwickTree

class TestAlgoVault(unittest.TestCase):
    def test_sorting(self):
        sample = [9, 3, 1, 5, 13, 2]
        self.assertEqual(quick_sort(sample), [1, 2, 3, 5, 9, 13])
        self.assertEqual(merge_sort(sample), [1, 2, 3, 5, 9, 13])

    def test_dijkstra(self):
        graph = {
            'A': [('B', 1.0), ('C', 4.0)],
            'B': [('C', 2.0), ('D', 5.0)],
            'C': [('D', 1.0)],
            'D': []
        }
        dist = dijkstra(graph, 'A')
        self.assertEqual(dist['D'], 4.0)

    def test_fenwick(self):
        bit = FenwickTree(10)
        bit.update(3, 5)
        bit.update(7, 2)
        self.assertEqual(bit.query(5), 5)
        self.assertEqual(bit.range_query(3, 7), 7)

if __name__ == '__main__':
    unittest.main()
