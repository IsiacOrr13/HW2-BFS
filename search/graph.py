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
        '''
        This method runs a search in the case that there is no end node. Takes in a start node and
        returns a list of transversed nodes in order they were transversed.
        '''
        q = Queue()
        visited = []
        q.put(node)
        while not q.empty():
            curr_node = q.get()
            if curr_node not in visited:
                visited.append(curr_node)
                for edge in self.edges():
                    if edge[0] == curr_node and edge[1] not in visited:
                        q.put(edge[1])
        return visited;

    def path_bfs(self, node, end):
        '''
        This method runs the bfs search in the case that there is a start and an end node.
        It takes in the start and end nodes and returns a list of nodes that make up the shortest
        path between start and end
        '''
        q = Queue()
        visited = set()
        q.put(node)
        path_lens = dict()
        path_lens[node] = 0
        prevs = dict()
        while not q.empty():
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
                        if at_node != node:
                            at_node = prevs[at_node]
                    return path
        return None

    def bfs(self, node, end=None):
        '''
        This method checks to see if the graph exists, the start node is in the graph, and if the end
        node exist sin the graph and calls the bfs_search or path_bfs depending on the results. If neither is
        applicable, None is returned.
        '''
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
