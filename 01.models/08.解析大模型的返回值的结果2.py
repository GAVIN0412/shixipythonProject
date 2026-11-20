"""
JsonOutputParser的输出类型是一个python字典/对象,作用强制AI大模型的输出JSON格式
StrOutputParser的输出类型是字符串无格式限制,输出自然语言
"""
import os
import logging
from langchain.chat_models import init_chat_model
# StrOutputParser 是一个简单的结果解析器,直接返回大模型输出的字符串的内容
from langchain_core.output_parsers import StrOutputParser
model = init_chat_model(
    model = "deepseek-chat",
    model_provider="deepseek",
    api_key =os.getenv("deepseek_api_key"),
    temperature = 0.6
)
#日志
logging.basicConfig(level=logging.DEBUG)
# 使用StrOutputParser解析器对象
parser = StrOutputParser()
answer = model.invoke(
    input=[
        {"role":"system","content":"请用清晰的文本格式输出结果,,每行素数以及对应的素数个数统计"},
        {"role":"user","content":"任意生成 5个 1000~100000之间的素数,并标出小于改素数的个数"}
    ]
)
print(answer.content,type(answer.content))
print("=================")
# 使用 StrOutputParser 解析输出,实际上就是直接输出字符串
result = parser.invoke(answer)
print(result,type(result))

