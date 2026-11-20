import os
from langchain.chat_models import init_chat_model
model = init_chat_model(
    model = "deepsek-chat",
    model_provider = "deepseek",
    api_key = os.getenv("deepseek_api_key"),
    temperature = 0.7,
)