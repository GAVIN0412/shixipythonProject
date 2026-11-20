import os
from langchain_core.messages import SystemMessage,HumanMessage
from langchain_openai import ChatOpenAI
#日志的包
import logging
model = ChatOpenAI(
    model = "deepseek-chat",
    openai_api_key = os.getenv("deepseek_api_key"),
    openai_api_base = os.getenv("deepseek_api_base"),
)
logging.basicConfig(level=logging.DEBUG)

answer = model.invoke(
    input=[
        SystemMessage("你是一个专业的数学老师"),
        HumanMessage("你是谁")
    ]
)
print(answer)
