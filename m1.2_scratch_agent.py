from deepagents import create_deep_agent

from models import model

from langchain_aws import ChatBedrockConverse
import os
from dotenv import load_dotenv

load_dotenv()
model = ChatBedrockConverse(
    model=os.getenv("AWS_MODEL_ID"),
    region_name=os.getenv("AWS_REGION"),)

agent = create_deep_agent(model=model)

result = agent.invoke({"messages": [{"role": "user", "content": "What is an LLM?"}]})

print(result["messages"][-1].text)
