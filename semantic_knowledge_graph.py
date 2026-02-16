import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

""" 
create the graphic
 """
G = nx.DiGraph()

""" 
define the nodes showing in the graphic
 """
nodes = ["Mammals", "Persons", "Female Persons", "Male Persons", "Mary", "John", "2", "1"]

""" 
define the relationships between nodes
 """
edges = [
    ("Persons", "Mammals", {"relation": "SubsetOf"}),
    ("Female Persons", "Persons", {"relation": "SubsetOf"}),
    ("Male Persons", "Persons", {"relation": "SubsetOf"}),
    ("Mary", "Female Persons", {"relation": "MemberOf"}),
    ("John", "Male Persons", {"relation": "MemberOf"}),
    ("Mary", "John", {"relation": "SisterOf"}),
    ("Persons", "2", {"relation": "Legs"}),
    ("John", "1", {"relation": "Legs"}),
]


""" 
add them to the graphic
 """
G.add_nodes_from(nodes)
G.add_edges_from([(u, v, d) for u, v, d in edges])

""" 
define attributes from the nodes, in this case the number of legs
 """
attributes = {
    "Persons": 2,
    "Mary": 2,
    "John": 1,
}


""" 
set the coordinates of the nodes to display it in a similar way to the example
 """
pos = {
    "Mammals": (0, 3),
    "Persons": (0, 2),
    "Female Persons": (-1.5, 1),
    "Male Persons": (1.5, 1),
    "Mary": (-2, 0),
    "John": (2, 0),
    "2": (0.5, 1.5),
    "1": (3, 0),
}

""" 
set the size and color of the nodes
 """
plt.figure(figsize=(10, 7))
node_colors = ['lightblue' if node in ["Mammals", "2", "1"] else 
               'lightgreen' if node in ["Mary", "John"] else 
               'plum' if node in ["Female Persons", "Male Persons"] else 
               'lightcoral' for node in nodes]

""" 
draw the nodes and edges
 """
nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=3000, font_size=10, font_weight="bold", arrows=True)

""" 
draw the labels.
(u,v) represents an edge
 """
edge_labels = {(u, v): d['relation'] for u, v, d in G.edges(data=True) if 'relation' in d}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="darkgreen", font_size=9)

""" 
add a curved arrow for the "HasMother" relationship
 """
ax = plt.gca()
arrow = FancyArrowPatch(
    posA=pos["Persons"], posB=pos["Female Persons"],
    connectionstyle="arc3,rad=0.2",
    arrowstyle='->', mutation_scale=15, color='black'
)
ax.add_patch(arrow)

""" 
add a boxed label for the "HasMother" relationship and set the coordinates
 """
plt.text(
    (pos["Persons"][0] + pos["Female Persons"][0]) / 2 - 0.1,
    (pos["Persons"][1] + pos["Female Persons"][1]) / 2 + 0.25,
    "HasMother", fontsize=9, color="black",
    bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3')
)

""" 
function to query the number of legs
 """
def query_legs(entity):
    """ get the attributes (legs) for the selected entity (node) """
    legs = attributes.get(entity, "unknown")
    return f"{entity} has {legs} legs."

""" 
display the graphic
 """
plt.title("Knowledge Graph Representation with Enhanced Labels")
plt.show()

""" 
in this case we ask, how many legs does Mary have?
 """
print(query_legs("Mary"))
