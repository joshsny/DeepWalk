import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import pylab
links_body = pd.read_csv('data/redditHyperlinks-body.tsv', sep = '\t')
links_title = pd.read_csv('data/redditHyperlinks-title.tsv', sep = '\t')

body = links_body.drop(['PROPERTIES', 'POST_ID'],axis = 1)
title = links_title.drop(['PROPERTIES', 'POST_ID'],axis = 1)

data = pd.concat([title, body])

G = nx.from_pandas_edgelist(data, 'SOURCE_SUBREDDIT', 'TARGET_SUBREDDIT', edge_attr = 'LINK_SENTIMENT', create_using = nx.MultiGraph())


node_degree_dict=nx.degree(G)

H = nx.subgraph(G,[x for x in G.nodes() if node_degree_dict[x]>100])

pos = nx.spring_layout(H)
nx.draw_networkx_labels(H, pos)
nx.draw(H, pos)
pylab.show()
