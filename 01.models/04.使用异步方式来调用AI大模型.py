"""
ainvoke => 表示异步调用, invoke => 同步调用
"""
import os
import time
import asyncio
from langchain_openai import ChatOpenAI
questions = [
    "こんにちは、私は文淵です。",
    "我喜欢吃苹果",
    "你喜欢吃什么?"
]
# 定义一个同步函数 call_llm_sync
def call_llm_sync(questions):
    model = ChatOpenAI(
        model = "deepseek-chat",
        openai_api_key = os.getenv("deepseek_api_key"),
        openai_api_base = os.getenv("deepseek_api_base"),
        temperature  = 0.6,
    )
    start = time.time()
    for question in questions:
        model.invoke(question)
    end = time.time()
    print(end - start)
# 定义一个异步函数 call_llm_async
async def call_llm_async(questions):
    model = ChatOpenAI(
        model = "deepseek-chat",
        openai_api_key = os.getenv("deepseek_api_key"),
        openai_api_base = os.getenv("deepseek_api_base"),
        temperature = 0.6,
    )
    start = time.time()
    jobs = [model.ainvoke(question) for question in questions]
    await asyncio.gather(*jobs)
    end = time.time()
    print(end - start)

if __name__ == '__main__':
    call_llm_sync(questions)
    asyncio.run(call_llm_async(questions))