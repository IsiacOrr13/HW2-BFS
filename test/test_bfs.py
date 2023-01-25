from search import Graph
import pytest
import pathlib


def test_valid_graph():
    f = pathlib.Path(__file__).resolve().parent.parent / 'data/tiny_network.adjlist'
    x = Graph(f)
    start = 'Luke Gilbert'
    end = 'Martin Kampmann'
    assert x.bfs(start) == ['Luke Gilbert',
                            '33483487',
                            '31806696',
                            '31626775',
                            '31540829',
                            'Martin Kampmann',
                            'Neil Risch',
                            'Nevan Krogan',
                            '32790644',
                            '29700475',
                            '34272374',
                            '32353859',
                            '30944313',
                            'Steven Altschuler',
                            'Lani Wu',
                            'Michael Keiser',
                            'Atul Butte',
                            'Marina Sirota',
                            'Hani Goodarzi',
                            '32036252',
                            '32042149',
                            '30727954',
                            '33232663',
                            '33765435',
                            '33242416',
                            '31395880',
                            '31486345',
                            'Michael McManus',
                            'Charles Chiu',
                            '32025019']
    assert x.bfs(start, end) == ['Luke Gilbert', '33483487', 'Martin Kampmann']


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
    end = 'Michael Keiser'
    assert x.bfs(start) == ['31806696', 'Luke Gilbert']
    assert not x.bfs(start, end)


def test_valid_graph_invalid_start():
    f = pathlib.Path(__file__).resolve().parent.parent / 'data/tiny_network.adjlist'
    x = Graph(f)
    start = 'Flop'
    end = 'Martin Kampmann'
    assert x.bfs(start) is None
    assert x.bfs(start, end) is None
