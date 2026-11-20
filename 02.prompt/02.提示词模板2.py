"""
PromptTemplate.from_template => 也是提示词模板的语法
"""
import os
from langchain_openai import  ChatOpenAI
from langchain_core.prompts import PromptTemplate

# 定义一个函数
def prompt_template_demo(thing:str,part_1:str,part_2:str) -> None:
    model = ChatOpenAI(
        model = "deepseek-chat",
        openai_api_key =os.getenv("deepseek_api_key"),
        openai_api_base = os.getenv("deepseek_api_base"),
        temperature = 0.6
    )
# 使用PromptTemplate创建提示词模板
    question = PromptTemplate.from_template(
        "请评价{thing}的优缺点,包括{part_1}和{part_2}两部分"
    )
    # 调用提示词模板将变量替换成真实的内容
    ask = question.format(
        thing=thing,
        part_1=part_1,
        part_2=part_2
    )
    print("==========")
    print(ask)
    print("==========")
    # 调用AI大模型
    answer = model.invoke(ask)
    # 输出AI大模型的返回结果
    print(answer.content)


if __name__ == '__main__':
    prompt_template_demo("苹果15", "外观", "性能")
