from graphs.breadth_first import bfs


def test_graph():
    assert bfs([0,1,0,2,0,3,2,4]) == [0,1,2,3,4]