"""
Graph algorithms: Dijkstra, Breadth-First Search, and Cycle Detection.
"""

import heapq
from typing import Dict, List, Tuple

def dijkstra(graph: Dict[str, List[Tuple[str, float]]], start: str) -> Dict[str, float]:
    """Computes single-source shortest paths using a min-heap priority queue."""
    distances = {node: float('inf') for node in graph}
    distances[start] = 0.0
    pq = [(0.0, start)]

    while pq:
        curr_dist, u = heapq.heappop(pq)
        if curr_dist > distances[u]:
            continue
        for v, weight in graph.get(u, []):
            dist = curr_dist + weight
            if dist < distances.get(v, float('inf')):
                distances[v] = dist
                heapq.heappush(pq, (dist, v))
    return distances

def has_cycle(graph: Dict[str, List[str]]) -> bool:
    """Detects cycles in a directed graph using DFS coloring."""
    visited = {}
    
    def dfs(node):
        visited[node] = 1 # In progress
        for neighbor in graph.get(node, []):
            if visited.get(neighbor) == 1:
                return True
            if visited.get(neighbor) != 2 and dfs(neighbor):
                return True
        visited[node] = 2 # Completed
        return False

    for node in graph:
        if visited.get(node) != 2 and dfs(node):
            return True
    return False
