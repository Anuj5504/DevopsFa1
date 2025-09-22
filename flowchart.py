import matplotlib.pyplot as plt
import networkx as nx

# Define nodes grouped by subsystems
nodes = {
    "Device": {"label": "Device Traffic", "group": "Client"},
    "Proxy": {"label": "Local Proxy\n(mitmproxy / agent)", "group": "Proxy"},
    "Backend": {"label": "Detection Backend (FastAPI)\nDeterministic → Embeddings (Qdrant) → LLM → Decision Engine", "group": "Backend"},
    "Decision": {"label": "Decision\n(Allow / Mask / Block / Quarantine)", "group": "Backend"},
    "Admin": {"label": "Admin UI / Review\n(Human feedback → Vector DB / Allowlists)", "group": "Admin"},
    "Alert": {"label": "Alerting / Integrations\n(Slack / SIEM / Logs → Postgres / Elastic)", "group": "Monitoring"},
}

# Define edges
edges = [
    ("Device", "Proxy"),
    ("Proxy", "Backend"),
    ("Backend", "Decision"),
    ("Decision", "Proxy"),
    ("Proxy", "Admin"),
    ("Proxy", "Alert")
]

# Create graph
G = nx.DiGraph()
for n, props in nodes.items():
    G.add_node(n, **props)
G.add_edges_from(edges)

# Colors by group
group_colors = {
    "Client": "#d9ead3",
    "Proxy": "#cfe2f3",
    "Backend": "#fce5cd",
    "Admin": "#fff2cc",
    "Monitoring": "#ead1dc"
}
node_colors = [group_colors[nodes[n]["group"]] for n in G.nodes()]

# Layout
pos = nx.spring_layout(G, seed=42)

# Draw
plt.figure(figsize=(12, 8))
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=5000, edgecolors="black")
nx.draw_networkx_labels(G, pos, labels={n: nodes[n]["label"] for n in G.nodes()}, font_size=9)
nx.draw_networkx_edges(G, pos, arrowstyle="->", arrowsize=20, edge_color="gray")

plt.axis("off")
plt.title("Security Traffic Analysis Flow (Presentation-Style)", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("/mnt/data/presentation_flow.png", dpi=150)
plt.close()

"/mnt/data/presentation_flow.png"
