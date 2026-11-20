"""
RecursiveCharacterTextSplitter =>
    递归切割器,也是最常用的切割器
    一般都是针对数据量比较大的
"""
# 导包
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import UnstructuredWordDocumentLoader
# 想要切割,那么先加载文档
docs = UnstructuredWordDocumentLoader("test.docx").load()
# 切割
chunks = RecursiveCharacterTextSplitter(
    separators=["\n\n","\n","，",",",""],
    chunk_size=400,
    chunk_overlap=40
).split_documents(docs)
# 输出切割的结果
print(chunks)