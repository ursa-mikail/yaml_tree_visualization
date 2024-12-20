## nodes
import yaml
import matplotlib.pyplot as plt
import networkx as nx

# Load the YAML file
with open('./sample_data/tree.yaml', 'r') as file:
    tree_data = yaml.safe_load(file)

# Recursive function to add nodes to the graph
def add_nodes(graph, data, parent=None, pos=None, level=0, x=0, width=2.0, vert_gap=0.2, vert_loc=0):
    if pos is None:
        pos = {}
    for key, value in data.items():
        pos[key] = (x, vert_loc)
        if parent:
            graph.add_edge(parent, key)
        if isinstance(value, dict):
            dx = width / len(value)
            nextx = x - width / 2 - dx / 2
            for child in value:
                nextx += dx
                pos = add_nodes(graph, {child: value[child]}, key, pos, level+1, nextx, dx, vert_gap, vert_loc-vert_gap)
    return pos

# Build the graph
G = nx.DiGraph()
pos = add_nodes(G, tree_data)

# Draw the graph
plt.figure(figsize=(12, 8))
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=10, font_weight="bold", arrows=False)
plt.show()


## values
import yaml
import matplotlib.pyplot as plt
import networkx as nx

# Load the YAML file
with open('./sample_data/tree.yaml', 'r') as file:
    tree_data = yaml.safe_load(file)

# Recursive function to add nodes to the graph
def add_nodes(graph, data, parent=None, pos=None, level=0, x=0, width=2.0, vert_gap=0.2, vert_loc=0):
    if pos is None:
        pos = {}
    for key, value in data.items():
        # Use the key for position, but the value for labels in the value graph
        node_label = key if isinstance(value, dict) else value
        pos[node_label] = (x, vert_loc)
        if parent:
            graph.add_edge(parent, node_label)
        if isinstance(value, dict):
            dx = width / len(value)
            nextx = x - width / 2 - dx / 2
            for child_key, child_value in value.items():
                nextx += dx
                pos = add_nodes(graph, {child_key: child_value}, node_label, pos, level+1, nextx, dx, vert_gap, vert_loc-vert_gap)
    return pos

# Function to create a graph from YAML data
def create_graph_from_yaml(data, use_values=False):
    G = nx.DiGraph()
    pos = add_nodes(G, data)
    return G, pos

# Function to plot the graph
def plot_graph(G, pos, title):
    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=10, font_weight="bold", arrows=False)
    plt.title(title)
    plt.show()

# Create and plot graph for keys
key_graph, key_pos = create_graph_from_yaml(tree_data)
plot_graph(key_graph, key_pos, 'YAML tree')


