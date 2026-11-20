"""
面试题一
    langchain的六大组件
        models,prompt,chains,indexs(rag),Agent,memory
面试题二
    如果区分文件格式
        # => 标题 => Title
        - => 列表 => ListItem
        ![](imgxxx.png) => 图片 => Image
        | 表格 | => 表格 => Table
面试题三
    rag切割的时候,碰到的图片怎么办?
        1. 区分图片还是文字
        2. 如果是文字,我们需要使用嵌入模型(embedding model),存储到向量数据库
           如果是图片,那么需要使用多模态大模型(CLIP)或者ORC,存储到向量数据库
           如果是PDF,那么直接使用 MinerU 模型(VLM)
        3. 检索的时候 => 用户提问 => 同时检索文字或者图片向量 => 合并结果
"""