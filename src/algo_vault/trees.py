"""
Binary Indexed Tree (Fenwick Tree) and Segment Tree primitives.
"""

from typing import List

class FenwickTree:
    """Fenwick Tree (Binary Indexed Tree) for prefix sum queries in O(log n)."""
    def __init__(self, size: int):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index: int, delta: int) -> None:
        """Adds delta to element at 1-based index."""
        i = index
        while i <= self.size:
            self.tree[i] += delta
            i += i & (-i)

    def query(self, index: int) -> int:
        """Returns prefix sum from index 1 to index."""
        sum_val = 0
        i = index
        while i > 0:
            sum_val += self.tree[i]
            i -= i & (-i)
        return sum_val

    def range_query(self, left: int, right: int) -> int:
        """Computes sum in range [left, right] inclusive."""
        return self.query(right) - self.query(left - 1)
