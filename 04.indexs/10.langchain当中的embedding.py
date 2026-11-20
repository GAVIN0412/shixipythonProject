"""
langchain框架使用embedding模型
"""
# 导包
from langchain_community.embeddings import ZhipuAIEmbeddings
# 创建一个向量模型
embedding = ZhipuAIEmbeddings(
    model="embedding-3",
    # api_key="",   因为我们在环境当中配置的zhipuai_api_key,所以也可以省略不写
)
# 使用embed_query处理单个文本
text1 = "你好,世界"
one_vector = embedding.embed_query(text1)
print(one_vector)

# 使用embed_docuemnt处理多个文本
many_vector = embedding.embed_documents(["你好","我好","他好","大家好,才是真的好"])
print(many_vector)
print(len(many_vector))