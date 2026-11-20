"""
with_structured_output => 将大模型的结果解析Data对象 => 返回的是一个新的大模型对象
这个新对象会自动按照Data格式解析回答,不需要解析器
"""
import os
import logging
from langchain_openai import ChatOpenAI
from pydantic import BaseModel,Field
model = ChatOpenAI(
    model = "deepseek-chat",
    openai_api_key =os.getenv("deepseek_api_key"),
    openai_api_base =os.getenv("deepseek_api_base"),
    temperature = 0.6
)
class Date(BaseModel):
    numbers: list[int] = Field(description="5个1000~100000之间的素数,按升序排列")
    count: list[int] = Field(description="与numbers一一对应,第i个数是小于numbers[i]的素数个数")

logging.basicConfig(level=logging.INFO)
# 将大模型的结果解析成Data对象
new_model = model.with_structured_output(Date, method="function_calling")

answer = new_model.invoke(
    input=[
        {"role": "user", "content": "随机生成5个1000~100000之间的素数,按升序输出;并给出与之一一对应的、小于该素数的素数个数"}
    ]
)
print(answer)
print(answer.numbers)
print(answer.count)