from graphviz import Digraph

# Create flowchart
dot = Digraph("TrafficFlow", format="png")
dot.attr(rankdir="LR", size="8,5")

# Nodes
dot.node("A", "Device Traffic")
dot.node("B", "Local Proxy (mitmproxy/agent)\n- TLS intercept\n- Regex prechecks")
dot.node("C", "Detection Backend (FastAPI)\nPipeline: Deterministic checks → Embeddings/RAG (Qdrant) → Local LLM → Decision engine")
dot.node("D", "Decision\n(Allow / Mask / Block / Quarantine)")
dot.node("E", "Admin UI / Review\n- Event ingest\n- Human review\n- Feedback → Vector DB / Allowlists")
dot.node("F", "Alerting / Integrations\n- Slack / SIEM\n- Logs → Postgres / Elastic")

# Edges
dot.edge("A", "B")
dot.edge("B", "C")
dot.edge("C", "D")
dot.edge("D", "B", label="Action enforced")
dot.edge("B", "E", label="Logs / Events")
dot.edge("B", "F", label="Security Alerts / Audit Logs")

# Render
file_path = "/mnt/data/traffic_flow"
dot.render(file_path, format="png", cleanup=True)

file_path + ".png"
