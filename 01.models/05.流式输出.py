import os
from langchain_core.messages import HumanMessage,SystemMessage
from langchain.chat_models import init_chat_model
model = init_chat_model(
    model = "deepseek-chat",
    model_provider="deepseek",
    api_key = os.getenv("deepseek_api_key"),
    temperature = 0.6
)
#调用大模型
answers = model.stream(
    input=[
        SystemMessage("你是一个专业的数学老师"),
        HumanMessage("你是谁")
        ]
)
for answer in answers:
    print(answer.content,end="")