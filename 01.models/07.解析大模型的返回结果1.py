import os
import logging
from langchain.chat_models import init_chat_model
# JsonOutputParser 是一个结果解析器,能够把AI大模型的输出的JSON字符串变成python的对象
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel,Field
model = init_chat_model(
    model = "deepseek-chat",
    model_provider= "deepseek",
    api_key =os.getenv("deepseek_api_key"),
    temperature = 0.6
)
# 定义一个Data类
class Data(BaseModel):
    number:list[int] = Field(description="生成素数列表")
    count:list[int] = Field(description="小于该素数的素数个数")
#日志
logging.basicConfig(level=logging.DEBUG)
# 我们AI对话的时候,要求AI返回的数格式
object1 = JsonOutputParser(pydantic_object = Data)
answer = model.invoke(
    input = [
        {"role":"system","content":object1.get_format_instructions()},
        {"role":"user","content":"任意生成5个 1000~100000 之间素数,并标出小于改素数的个数"},
    ]
)
# 打印AI大模型的回答内容,类型为字符串
print(answer.content,type(answer.content))
# 我们需要使用object对象解析器把输出的JSON字符串转换成python的对象，类型为字典
result = object1.invoke(answer)
print(result,type(result))
# 可以获取字典里面的value值,就是根据key来进行获取的
print(result["number"])
print(result["count"])
