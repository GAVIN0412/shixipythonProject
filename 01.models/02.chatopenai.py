import os
from langchain_core.messages import SystemMessage,HumanMessage
from langchain_openai import ChatOpenAI
model = ChatOpenAI(
    model = "deepseek-chat",
    openai_api_key =os.getenv("deepseek_api_key"),
    openai_api_base = "https://api.deepseek.com/v1",
    temperature =0.7,
)
#字典写法
# answer = model.invoke(
#     input = [
#         {"role":"system","content":"你是一个专业的数学老师"},
#         {"role":"user","content":"1+1=?"},
#     ]
# )
answer = model.invoke(
    input=[
        SystemMessage("你是一个专业的数学老师"),
        HumanMessage("你是谁")
    ]
)

print(answer.content)