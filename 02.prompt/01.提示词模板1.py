"""
提示词模板的语法 =>ChatPromptTemplate.from_messages(...)
"""
import os
from langchain_openai import ChatOpenAI
# 提示词模板的包
from langchain_core.prompts import ChatPromptTemplate


# 定义一个函数,函数的作用就是提示词模板
def prompt_template_demo(thing: str, part_1: str, part_2: str) -> None:
    model = ChatOpenAI(
        model="deepseek-chat",
        openai_api_key=os.getenv("deepseek_api_key"),
        openai_api_base=os.getenv("deepseek_api_base"),
        temperature=0.6
    )

    # 编写提示词
    question = ChatPromptTemplate.from_messages([
        ("system", "你是一个专业的评论员"),
        ("human", "请评价{thing}的优缺点，包括{part_1}和{part_2}两方面")
    ])

    # 填充变量,得到一个真正的 PromptValue(还没发给模型)
    ask = question.invoke({
        "thing": thing,
        "part_1": part_1,
        "part_2": part_2
    })

    print("+++++++++")
    print(ask)
    print("+++++++++")

    # 把填充好的提示词交给模型
    answer = model.invoke(ask)
    print(answer)
    print(answer.content)


if __name__ == "__main__":
    prompt_template_demo("华为Mate60", "性能", "拍照")
