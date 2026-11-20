import os
from langchain.chat_models import init_chat_model
model = init_chat_model(
    model = "deepseek-chat",
    model_provider="deepseek",
    api_key =os.getenv("deepseek_api_key"),
    temperature = 0.6
)
answers = model.batch(
    inputs = [
        "什么是langchain",
        "什么是rag",
        "什么是Agent"
    ]
)
for answer in answers:
    print("==========================")
    print(answer.content)
