from search import Graph
import pytest
import pathlib


def test_empty_graph():
    f = pathlib.Path(__file__).resolve().parent.parent / 'data/empty.adjlist'
    x = Graph(f)
    start = 'Check'
    assert x.bfs(start) is None
    end = 'Mate'
    assert x.bfs(start, end) is None

def test_path_unconnected_graph():
    f = pathlib.Path(__file__).resolve().parent.parent / 'data/unconnected.adjlist'
    x = Graph(f)
    start = '31806696'
    assert x.bfs(start) is ['31806696', 'Luke Gilbert']

def test_valid_graph():
    f = pathlib.Path(__file__).resolve().parent.parent / 'data/tiny_network.adjlist'
    x = Graph(str(f))
    start = 'Luke Gilbert'
    end = 'Martin Kampmann'
    assert x.bfs(start) is None
    assert x.bfs(start, end) is None

def test_bfs():
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """
    pass
