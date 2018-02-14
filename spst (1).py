import graph
from graph_io import load_graph, write_dot  # graphIO import graphs.py, so we do not need to import it here.
import os
import math

# Use these options to change the tests:

TEST_BELLMAN_FORD_DIRECTED = True
TEST_BELLMAN_FORD_UNDIRECTED = False
TEST_DIJKSTRA_DIRECTED = True
TEST_DIJKSTRA_UNDIRECTED = False

WRITE_DOT_FILES = True

# Use this to select the graphs to test your algorithms on:
#TestInstances = ["weightedexample.gr"]
TestInstances = ["graph1.gr", "graph2.gr", "graph3.gr", "graph4.gr", "graph5.gr",  "graph6.gr"]
# TestInstances=["randomplanar.gr"]
# TestInstances = ["randomplanar10.gr"]
# TestInstances=["bd.gr","bbf.gr"]; WriteDOTFiles=False
# TestInstances=["bbf2000.gr"]; WriteDOTFiles=False
# TestInstances=["bbf200.gr"]
# TestInstances=["negativeweightexample.gr"]
# TestInstances=["negativeweightcycleexample.gr"]
# TestInstances=["WDE100.gr","WDE200.gr","WDE400.gr","WDE800.gr","WDE2000.gr"]; WriteDOTFiles=False
# TestInstances=["weightedex500.gr"];	WriteDOTFiles=False


USE_UNSAFE_GRAPH = False


def bellman_ford_undirected(graph, start):
    """
    Arguments: <graph> is a graph object, where edges have integer <weight>
        attributes,	and <start> is a vertex of <graph>.
    Action: Uses the Bellman-Ford algorithm to compute all vertex distances
        from <start> in <graph>, and assigns these values to the vertex attribute <dist>.
        Optional: assigns the vertex attribute <in_edge> to be the incoming
        shortest path edge, for every reachable vertex except <start>.
        <graph> is viewed as an undirected graph.
    """
    # Initialize the vertex attributes:
    for v in graph.vertices:
        v.dist = math.inf
        v.in_edge = None

    start.dist = 0

    # Insert your code here.


def bellman_ford_directed(graph, start):
    """
    Arguments: <graph> is a graph object, where edges have integer <weight>
        attributes,	and <start> is a vertex of <graph>.
    Action: Uses the Bellman-Ford algorithm to compute all vertex distances
        from <start> in <graph>, and assigns these values to the vertex attribute <dist>.
        Optional: assigns the vertex attribute <in_edge> to be the incoming
        shortest path edge, for every reachable vertex except <start>.
        <graph> is viewed as a directed graph.
    """
    # Initialize the vertex attributes:
    for v in graph.vertices:
        v.dist = math.inf
        v.in_edge = None

    start.dist = 0

    # Insert your code here.
    for i in range(0, len(graph.vertices) - 1):
        for e in graph.edges:
            if e.tail.dist + e.weight < e.head.dist:
                e.head.dist = e.tail.dist + e.weight
                e.head.in_edge = e.tail

    for e in graph.edges:
        if e.tail.dist + e.weight < e.head.dist:
            print ("Graph contains a negative-weight cycle")


def dijkstra_undirected(graph, start):
    """
    Arguments: <graph> is a graph object, where edges have integer <weight>
        attributes,	and <start> is a vertex of <graph>.
    Action: Uses Dijkstra's algorithm to compute all vertex distances
        from <start> in <graph>, and assigns these values to the vertex attribute <dist>.
        Optional: assigns the vertex attribute <in_edge> to be the incoming
        shortest path edge, for every reachable vertex except <start>.
        <graph> is viewed as an undirected graph.
    """
    # Initialize the vertex attributes:
    for v in graph.vertices:
        v.dist = math.inf
        v.in_edge = None

    start.dist = 0

    # Insert your code here.


def dijkstra_directed(graph, start):
    """
    Arguments: <graph> is a graph object, where edges have integer <weight>
        attributes,	and <start> is a vertex of <graph>.
    Action: Uses Dijkstra's algorithm to compute all vertex distances
        from <start> in <graph>, and assigns these values to the vertex attribute <dist>.
        Optional: assigns the vertex attribute <in_edge> to be the incoming
        shortest path edge, for every reachable vertex except <start>.
        <graph> is viewed as a directed graph.
    """
    # Initialize the vertex attributes:
    for v in graph.vertices:
        v.dist = math.inf
        v.in_edge = None

    start.dist = 0
    # Insert your code here.
    unvisitedQ = []
    for v in graph.vertices:
        unvisitedQ.append(v)

    while not (len(unvisitedQ) == 0):
        u = getMinDist(unvisitedQ)
        unvisitedQ.remove(u)

        neighboursOfU = u.neighbours

        for v in neighboursOfU:
            if v in unvisitedQ:
                #alt = u.dist + graph.find_edge(u, v).weight
                if findEdge(u,v,graph) is not None:
                    alt = u.dist + findEdge(u,v,graph).weight
                    if alt < v.dist:
                        v.dist = alt
                        v.in_edge = u

def findEdge(u, v, g):
    for e in g.edges:
        if (e.tail == u and e.head == v):
            return e
    return None

def getMinDist(unvisitedQ):
    u = None

    for v in unvisitedQ:
        if u == None:
            u = v
        else:
            if u.dist > v.dist:
                u = v

    return u


##############################################################################
#
# Below is test code that does not need to be changed.
#
##############################################################################

def print_max_dist(graph):
    unreachable = False
    numreachable = 0
    sorted_vertices = sorted(graph.vertices, key=lambda v: v.label)
    remote = sorted_vertices[0]
    for v in graph.vertices:
        if v.dist == math.inf:
            unreachable = True
            # print("Vertex", v,"is unreachable")
        else:
            numreachable += 1
            if v.dist > remote.dist:
                remote = v
    print("Number of reachable vertices:", numreachable, "out of", len(graph))
    print("Largest distance:", remote.dist, "For vertex", remote)


def prepare_drawing(graph):
    for e in graph.edges:
        e.colornum = 0
    for v in graph.vertices:
        if hasattr(v, "in_edge") and v.in_edge is not None:
            v.in_edge.colornum = 1
    for v in graph:
        v.label = str(v.dist)


def do_testalg(testalg, G):
    if testalg[1]:
        print("\n\nTesting", testalg[0])
        startt = time()
        if testalg[0] == "Kruskal":
            ST = testalg[2](G)
            totalweight = 0
            for e in ST:
                totalweight += e.weight
        else:
            sorted_vertices = sorted(G.vertices, key=lambda v: v.label)
            testalg[2](G, sorted_vertices[0])
        endt = time()
        print("Elapsed time in seconds:", endt - startt)

        if testalg[0] != "Kruskal":
            print_max_dist(G)
            prepare_drawing(G)
        else:
            if len(ST) < len(G.vertices) - 1:
                print("Total weight of maximal spanning forest:", totalweight)
            else:
                print("Total weight of spanning tree:", totalweight)
            for e in G.edges:
                e.colornum = 0
            for e in ST:
                e.colornum = 1
            for v in G.vertices:
                v.label = v._label

        if WRITE_DOT_FILES:
            with open(os.path.join(os.getcwd(), testalg[3] + '.dot'), 'w') as f:
                write_dot(G, f, directed=testalg[4])


if __name__ == "__main__":
    from time import time

    for FileName in TestInstances:
        # Tuple arguments below:
        # First: printable string
        # Second: Boolean value
        # Third: Function
        # Fourth: Filename
        # Fifth: Whether output should be directed
        for testalg in [("Bellman-Ford, undirected", TEST_BELLMAN_FORD_UNDIRECTED, bellman_ford_undirected,
                         "BellmanFordUndirected", False),
                        ("Bellman-Ford, directed", TEST_BELLMAN_FORD_DIRECTED, bellman_ford_directed,
                         "BellmanFordDirected",
                         True),
                        ("Dijkstra, undirected", TEST_DIJKSTRA_UNDIRECTED, dijkstra_undirected, "DijkstraUndirected",
                         False),
                        ("Dijkstra, directed", TEST_DIJKSTRA_DIRECTED, dijkstra_directed, "DijkstraDirected", True)]:
            if USE_UNSAFE_GRAPH:
                print("\n\nLoading graph", FileName, "(Fast graph)")
                with open(os.path.join(os.getcwd(), FileName)) as f:
                    G = load_graph(f, graph.Graph)
            else:
                print("\n\nLoading graph", FileName)
                with open(os.path.join(os.getcwd(), FileName)) as f:
                    G = load_graph(f)

            for i, vertex in enumerate(list(G.vertices)):
                vertex.colornum = i
            do_testalg(testalg, G)
