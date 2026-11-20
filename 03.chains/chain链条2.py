"""
多个链条并行执行
    RunnableParallel(
        变量1 = 链条1,
        变量2 = 链条2
    )
"""
# 导包
import os
import logging
# 大模型一般就是两种输出 StrOutptParser和JsonOutputParser
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableParallel
# 创建AI大模型
model = ChatOpenAI(
    model="glm-4-flash",
    openai_api_key=os.getenv("zhipuai_api_key"),
    openai_api_base=os.getenv("zhipuai_api_base"),
    temperature=0.6
)
# 定义一个解析器
word = StrOutputParser()
# 配置日志
logging.basicConfig(level=logging.DEBUG)
# 提示词1
question1 = ChatPromptTemplate([("human","把这个句子{question}翻译成英文")])
# 创建链条1
line_1 = question1 | model | word
# 提示词2
question2 = ChatPromptTemplate([("human","把这个句子{question}翻译成中文")])
# 创建链条2
line_2 = question2 | model | word
# 把两个链条并且在一个容器当中,执行的时候,会同时执行两个链条
# 两个链条同时执行,结果我们想要 {"english":英文翻译,"chinese":中文翻译}
lines = RunnableParallel(
    english=line_1,
    chinese=line_2
)
# 两个链条并行执行
answer = lines.invoke({
    "question":"こんにちは、私は文淵です。"
})

# 输出最终的答案
print(answer,type(answer))