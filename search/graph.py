from copy import deepcopy

import networkx as nx
import pathlib
from queue import Queue


class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        try:
            self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")
            self.nodes = self.graph.nodes()
            self.edges = self.graph.edges()

        except:
            print('Unreadable file -- Check file name, type, and structure')

    def bfs_search(self, node):
        q = Queue()
        visited = set()
        q.put(node)
        while q:
            curr_node = q.get()
            if curr_node not in visited:
                visited.add(curr_node)
                for edge in self.edges():
                    if edge[0] == curr_node and edge[1] not in visited:
                        q.put(edge[1])
        return visited

    def path_bfs(self, node, end):
        q = Queue()
        visited = set()
        q.put(node)
        path_lens = dict()
        path_lens[node] = 0
        prevs = dict()
        while q:
            curr_node = q.get()
            if curr_node not in visited:
                dist = path_lens[curr_node] + 1
                visited.add(curr_node)
                found_end = False
                for edge in self.edges():
                    if edge[0] == curr_node and edge[1] not in visited:
                        q.put(edge[1])
                        path_lens[edge[1]] = dist
                        prevs[edge[1]] = curr_node
                        found_end = edge[1] == end
                if found_end:
                    path = [None] * (path_lens[end] + 1)
                    at_node = end
                    for idx in range(path_lens[end] + 1):
                        path[path_lens[end] - idx] = at_node
                        if at_node != start:
                            at_node = prevs[at_node]
                    return path
        return None

    def bfs(self, node, end=None):
        if self.nodes() or self.edges():
            if node in self.nodes():
                if end:
                    if end in self.nodes():
                        return self.path_bfs(node, end)
                    else:
                        print('End node not in graph, returning result for end=None')
                        return self.bfs_search(node)
                else:
                    return self.bfs_search(node)
            else:
                print('Starting node not in graph')
                return None
        else:
            print('Graph is empty, check file')
            return None

f = pathlib.Path(__file__).resolve().parent.parent / 'data/tiny_network.adjlist'
x = Graph(f)
start = 'Luke Gilbert'
end = 'Martin Kampmann'
#end = '31540829'



print(x.bfs(start, end))