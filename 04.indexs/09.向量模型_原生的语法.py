"""
向量和embedding的定义
    将我们的文本通过一个叫做向量模型(embedding)转换成一段很长的小数的集合
    向量就是一段有距离的,有方向的量
        方向代表的向量的方向
        长度代表的向量的大小
作用: 就是将文本转换成一组浮点数,每一个下标(索引)都对应着一个维度,整个数组对应
    这个n维度里面的某一个点,这个这个点到点之间的距离可以计算,距离的远近代表的
    语义相似度的大小
embedding model,embedding模型,嵌入模型,向量模型 => 指的都是同一个东西
"""
# 下载zhipuai的包 => pip install zhipuai
from zhipuai import ZhipuAI
# api_key="YOUR_API_KEY" 这个可以删除掉
# 因为我们之前有把zhipuai_api_key 配置到环境当中去了
# zhipuai他会自动的去环境里面找一个叫做zhipuai_api_key
client = ZhipuAI()
response = client.embeddings.create(
    model="embedding-2", #填写需要调用的模型编码
    input=[ # 就是将这三句话通过embedding-3的模型,转换一组浮点数
        "美食非常美味，服务员也很友好。",
        "这部电影既刺激又令人兴奋。",
        "文渊"
    ],
)
print(len(response.data[0].embedding),response.data[0].embedding)
print(len(response.data[1].embedding),response.data[1].embedding)
print(len(response.data[2].embedding),response.data[2].embedding)