"""
导包 =>
    pip install "unstructured[docx]"
"""
# 导包
from langchain_community.document_loaders import UnstructuredWordDocumentLoader
# 创建一个loader对象
loader = UnstructuredWordDocumentLoader(
    file_path="test.docx",  # 文件路径
    mode="elements",    # 把文档拆分成多个小片段
    encoding="utf-8"
)
# 调用加载器
docs = loader.load()

# 获取里面的片段
for doc in docs:
    print(type(doc))
    print(doc.page_content)