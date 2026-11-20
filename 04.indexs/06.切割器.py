"""
切割器
    separator => 切分文本字符或者字符串
    chunk_size => 每一个文本块的最大长度
    chunk_overlap => 文本块直接的重叠字符串
"""
# 导包
from langchain_text_splitters import CharacterTextSplitter
# 创建一个切割器
text_spliter = CharacterTextSplitter(
    separator="，",
    chunk_size=10,
    chunk_overlap=2
)
# 使用切割器开始切割
result = text_spliter.split_text(
    "今天天气这么好，确，实适合出去走走、晒晒太阳，或者约上朋友喝杯东西。你那边现在是什么季节？春光正好的话，别辜负了这好风光～"
)
"""
既然今天天气这么好，
好，确实适合出去走走
走走、晒晒太阳，或者
或者约上朋友喝杯东西
东西。你那边现在是什
是什么季节？春光正好
正好的话，别辜负了这
了这好风光～

切割的原理
    1. 如果说,没有指定 separator,那么就是按照 chunk_size 和 chunk_overlap 来进行切割
    2. 将文本按逗号(，)进行切割
    3. 如果切割之后的文本小于10,则可以进行合并,单个文本的长度小于10,合并之后也不大于10
    4. 如果切割之后的文本长度大于10,那么大于10的长度的文本,无法按照chunk_size来进行切割
"""
# 输出result
print(result)

print("-------------")
# 多个文本切割 => text_spliter.create_documents 和 text_spliter.split_text 切割原理是一样的
texts = text_spliter.create_documents([
"今天天气这么好，确，实适合出去走走、晒晒太阳，或者约上朋友喝杯东西。你那边现在是什么季节？春光正好的话，别辜负了这好风光～",
"如果说,没有指定 separator,那么就是按照 chunk_size 和 chunk_overlap 来进行切割",
])
# 输出
# print(texts)
for t in texts:
    print(t.page_content)