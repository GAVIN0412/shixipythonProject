"""
语义相似度的计算,可以使用欧式距离和Cos余弦来计算
    欧式距离 => 计算出来的值越小越相似
    Cos余弦 => 计算出来的值越大约相似
"""
# 导包
from zhipuai import ZhipuAI
from numpy import dot
import numpy as np
from numpy.linalg import norm

# 创建一个客户端
client = ZhipuAI()

# 计算余弦距离,越大越相似
def cos_sim(a,b): # 计算a,b两个点之间的相似度,这个公式不需要大家背
    return dot(a,b) / (norm(a) * norm(b))

# 计算欧式距离
def l2(a,b):
    return norm(np.asarray(a) - np.asarray(b))

# 定义一个函数,封装一个embedding模型
def get_embedding(text):
    res = client.embeddings.create(
        model="embedding-3",
        input=text
    )
    return [x.embedding for x in res.data]

# 定义一个文本
query = "我要买水果"
document = [
    "水果摊在家门口",
    "南边有🍇",
    "乔丹是芝加哥公牛队之神",
    "文渊你好啊",
    "喜欢吃水果"
]
# 将query转换成向量
query_vet = get_embedding([query])[0]
# 将document转换成向量
doc_vet = get_embedding(document)
print("=====Cos余弦相似度的比较=====")
print(cos_sim(query_vet,query_vet))
for vet in doc_vet:
    print(cos_sim(query_vet,vet))

print("=====欧式距离的相似度比较=====")
print(l2(query_vet,query_vet))
for vet in doc_vet:
    print(l2(query_vet,vet))