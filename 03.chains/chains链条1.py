"""
chains条件 => 将prompt,llm,res组成一个链条,串行执行
"""
import os
import logging
# StrOUtputParser => 是一个字符串的解析器,把大模型的回答转换成字符串
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
# 链条的包
from langchain_core.runnables import RunnableSequence
# 定义一个函数
def prompt_template_demo(thing:str,p1:str,p2:str) -> None:
    # 日志
    logging.basicConfig(level=logging.DEBUG)
    # 定义一个提示词模板
    question = ChatPromptTemplate.from_messages([
        ("system","你是一个专业的评论员"),
        ("human","请评价{thing}的优缺点,包括{p1}和{p2}")
    ])
    # 定义一个大模型
    model = ChatOpenAI(
        model="deepseek-chat",
        openai_api_key=os.getenv("deepseek_api_key"),
        openai_api_base=os.getenv("deepseek_api_base"),
        temperature=0.6
    )
    # 定义一个字符串解析器
    word = StrOutputParser()

    # 链条的语法一 => 将问题,模型,返回的格式 形成一个链条执行
    # line = RunnableSequence(question,model,word)

    # 链条的语法二 => 管道语法
    line = question | model | word

    # 执行这个链条
    answer = line.invoke({
        "thing": thing,
        "p1": p1,
        "p2": p2
    })
    # 输出AI大模型返回结果
    print(answer)


if __name__ == '__main__':
    prompt_template_demo("iphone 15", "外观", "性能")