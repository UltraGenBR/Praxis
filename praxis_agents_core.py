# === PRAXIS Project: Multi-Agent Core Flow ===

from agents import Agent, function_tool
from agents.extensions.visualization import draw_graph
import hashlib

# Tool to register an idea and generate an ID
@function_tool
def register_idea(user_id: str, idea: str) -> dict:
    idea_id = hashlib.sha256(f"{user_id}:{idea}".encode()).hexdigest()[:10]
    return {
        "user_id": user_id,
        "idea": idea,
        "idea_id": idea_id,
        "status": "registered"
    }

# Ferramenta para simular cálculo de impacto
@function_tool
def evaluate_idea_impact(idea: str) -> str:
    return f"Impacto estimado para a ideia '{idea}' é de 1.4% no ecossistema."

# Agente responsável por registrar ideias
registry_agent = Agent(
    name="Idea Registry",
    instructions="Você registra ideias submetidas e gera um identificador único.",
    tools=[register_idea]
)

# Agente responsável por avaliar impacto
impact_agent = Agent(
    name="Impact Evaluator",
    instructions="Você avalia o impacto de ideias no contexto do projeto PRAXIS.",
    tools=[evaluate_idea_impact]
)

# Agente central que redireciona as solicitações
triage_agent = Agent(
    name="Triage Agent",
    instructions="""
Você é o agente central. 
Quando o usuário submete uma ideia, determine se deve registrar ou avaliar.
Encaminhe para o agente apropriado.
""",
    handoffs=[registry_agent, impact_agent]
)

# Visualiza o grafo da arquitetura de agentes
draw_graph(triage_agent)
