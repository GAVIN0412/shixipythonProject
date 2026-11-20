"""
langchain当中加载markdown文档
    pip install markdown
    pip install "unstructured[pdf,md]"
    pip install langchain_community
"""
# 导包
from langchain_community.document_loaders import UnstructuredMarkdownLoader
# 创建一个加载器,用来读取markdown
loader = UnstructuredMarkdownLoader(
    file_path="../data/test.md",  # 表示的就是你要读取的那个文件
    mode="elements",  # 表示把文件拆分成多个小小的部分,比如:标题,段落来读取
    encoding="utf-8"
)
list = loader.load()
for item in list:
    print(item.page_content)