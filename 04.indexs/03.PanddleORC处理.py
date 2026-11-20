"""
PaddleORC的作用: 可以把照片,截取中的文字提取成可以编辑的文本,方便复制或者搜索
核心语法:
    PaddleORC(....) -> 创建一个PaddleORC,作用相当于一台识字机
    orc.predict("图片名") -> 让识字机读取指定的图片
    res.json -> 把机器读取到的结果变成字典格式
导包
    pip install paddleocr==3.7.0
    pip install --upgrade "paddlepaddle==3.3.1" -i https://www.paddlepaddle.org.cn/packages/stable/cpu/
注意: 下载模型的路径
"""
from paddleocr import PaddleOCR
# 创建ORC
orc = PaddleOCR(
    use_textline_orientation=True,  # 自动判断文字方向(横排/竖排)
    lang="ch",  # 语言设置成中文
    enable_mkldnn = False   # 不使用加速,普通运行即可,可以当做默认写法
)
# 让orc几区读取 "1.jpg" 图片,识别结果
output = orc.predict("1.jpg")
# 遍历每一个检测结果,通常一张图片只有一个结果
for item in output:
    # 获取当前的结果 => 是一个字典
    info = item.json
    # 提取核心的数据
    # print(info)
    # print(info["res"])
    print(info["res"].get("rec_texts",[]))      # 获取所有识别出来的文字(列表)
    print(info["res"].get("rec_scores",[]))     # 对应的可信度(列表)
    print(info["res"].get("rec_boxes",[]))      # 矩形的坐标(x1,y1,x2,y2)