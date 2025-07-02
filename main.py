import pandas as pd
import networkx as nx
import json
import numpy as np
from networkx.algorithms.community import greedy_modularity_communities
from matplotlib import cm
import matplotlib.pyplot as plt
#Using pandas to read the csv file
data = pd.read_csv('ecommerce_customer_data_custom_ratios.csv')

#To take subset of data out of 2.5 lac of record data
sampled_data = data.sample(frac=0.005, random_state=42)

#To group particular columns
grouped_data = sampled_data[['Customer ID', 'Product Category', 'Quantity']].groupby(['Customer ID', 'Product Category']).sum().reset_index()

#This mapping was done so that during clustering all columnms are of same data type
category_mapping = {"Books": 1, "Electronics": 2, "Home": 3, "Clothing": 4}

# This will now map the values set in category_mapping in grouped data
grouped_data['Product Category'] = grouped_data['Product Category'].map(category_mapping)

#creates an empty undirected graph using the NetworkX library
G = nx.Graph()

#Adding nodes in the graph created previously
G.add_nodes_from(grouped_data['Customer ID'].unique(), type='customer')
G.add_nodes_from(grouped_data['Product Category'].unique(), type='product')

#Adding edges in the graph 
for _, row in grouped_data.iterrows():
    G.add_edge(row['Customer ID'], row['Product Category'], weight=row['Quantity'])

#Built-In function to detect the communities in the graph
communities = list(greedy_modularity_communities(G))

#Function to calculate the positions of nodes in a graph G for visualization purposes
pos = nx.spring_layout(G)
color_map = cm.rainbow(np.linspace(0, 1, len(communities)))

for i, community in enumerate(communities):
    nx.draw_networkx_nodes(G, pos, nodelist=community, node_color=[color_map[i]], node_size=30)
nx.draw_networkx_edges(G, pos, alpha=0.5)

plt.show(block=True)

clusters = {f"Cluster_{i}": list(map(int, community)) for i, community in enumerate(communities)}
with open("clusters.json", "w") as f:
    json.dump(clusters, f)

modularity = nx.algorithms.community.modularity(G, communities)
print(f"Modularity: {modularity}")

avg_degree = np.mean([deg for node, deg in G.degree()])
print(f"Average Degree: {avg_degree}")

try:
    diameter = nx.diameter(G)
    print(f"Diameter: {diameter}")
except nx.NetworkXError:
    diameter = "Inf"  
    print(f"Diameter: {diameter}")

try:
    avg_path_length = nx.average_shortest_path_length(G)
    print(f"Average Path Length: {avg_path_length}")
except nx.NetworkXError:
    avg_path_length = "Inf"  
    print(f"Average Path Length: {avg_path_length}")

clustering_coefficient = nx.average_clustering(G)
print(f"Clustering Coefficient: {clustering_coefficient}")

density = nx.density(G)
print(f"Graph Density: {density}")
