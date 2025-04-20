# autogen_worker.py
from autogen import AssistantAgent, UserProxyAgent
import os
from dotenv import load_dotenv

load_dotenv("deepseekkey.env")  # Load your API key

def analyze_code(code: str, n_runs: int = 3):
    # DeepSeek config
    config_list = [{
        "model": "deepseek-v3",
        "api_key": os.getenv("DEEPSEEK_API_KEY"),
        "base_url": "https://api.deepseek.com/v1"
    }]

    # Self-consistency: Parallel agents
    agents = []
    for i in range(n_runs):
        assistant = AssistantAgent(
            name=f"auditor_{i}",
            llm_config={"config_list": config_list}
        )
        user_proxy = UserProxyAgent(human_input_mode="NEVER")
        user_proxy.initiate_chat(
            assistant,
            message=f"Audit this code for WCAG 2.2 issues: {code}"
        )
        agents.append(assistant.last_message()["content"])

    # TODO: Add voting/aggregation logic
    return agents  # Temporary return raw results