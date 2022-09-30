import networkx as nx
import assortnet
import numpy as np

G = nx.karate_club_graph()
attr = "club"
weight = "weight"

mm = assortnet.mixing_matrix(G,
                              attr,
                              attr_type_list=["Mr. Hi", "Officer"],
                              weight = "weight", 
                              )
print("Mixing matrix of club:")
print(mm)

r, s = assortnet.assortment_discrete(G,
                                    attr,
                                    attr_type_list=None,
                                    weight = "weight",
                                    SE = True,
                                    M = 1
                                    )

print("Assortivity coef:{:.3f}".format(r))
print("Jackknife SE:{:.3f}".format(s))

# add random continuous node attribute
attr = "height"
mu = 170
sigma = 10
np.random.seed(114514)
heights = np.random.normal(mu, sigma, len(list(G.nodes)))
for i, (u,v) in enumerate(G.nodes(data=True)):
    v[attr] = heights[i]

r, s = assortnet.assortment_continuous(G,
                                    attr,
                                    weight = "weight",
                                    SE = True,
                                    M = 1
                                    )

print("Assortivity coef:{:.3f}".format(r))
print("Jackknife SE:{:.3f}".format(s))