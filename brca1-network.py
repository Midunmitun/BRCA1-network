import requests
import networkx as nx
import matplotlib.pyplot as plt

protein = "BRCA1"
species = "9606"

url = f"https://string-db.org/api/json/interaction_partners?identifiers={protein}&species={species}&limit=10"

response = requests.get(url)
data = response.json()

for item in data:
    print(item['preferredName_A'], "-->", item['preferredName_B'], "| Score:", item['score'])

G = nx.Graph()

for item in data:
    G.add_edge(item['preferredName_A'], item['preferredName_B'], weight=item['score'])

plt.figure(figsize=(10, 8))
nx.draw(G, with_labels=True, node_color='lightblue', 
        node_size=2000, font_size=10, font_weight='bold')
plt.title("BRCA1 Protein Interaction Network")
plt.savefig("brca1_network.png")
plt.show()