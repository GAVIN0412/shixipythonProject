"""
MinerU是一个可以把 PDF 文件里面的内容(文字,表格,图片,公式)都可以准确的提取出来
普通的方式或者PDF的时候,文字,格式会乱掉,表格也会散掉,公式也会变成乱码,MinerU就可以解决这个问题
具体的流程:
    1. 调用API上传PDF给MinerU
    2. MinerU会告诉你一个任务编号(唯一的)batch_id
    3. 使用ID进行轮询查询是否解析任务
    4. MinerU完成了解析任务,MinerU就会告诉 Markdown 文件在哪里下载(下载地址) => 把pdf转成md
    5. 咱们使用地址进行下载
官网 => https://mineru.net
    token => 从环境变量 MINERU_TOKEN 读取（不要硬编码到代码里）
"""
# import os
# import requests

# token = os.getenv("MINERU_TOKEN")   # 从环境变量读取，禁止硬编码
# url = "https://mineru.net/api/v4/file-urls/batch"
# header = {
#     "Content-Type": "application/json",
#     "Authorization": f"Bearer {token}"
# }
# data = {
#     "files": [
#         {"name":"test.pdf", "data_id": "abcd"}
#     ],
#     "model_version":"vlm"
# }
# file_path = ["test.pdf"]
# try:
#     response = requests.post(url,headers=header,json=data)
#     if response.status_code == 200:
#         result = response.json()
#         print('response success. result:{}'.format(result))
#         if result["code"] == 0:
#             batch_id = result["data"]["batch_id"]
#             urls = result["data"]["file_urls"]
#             print('batch_id:{},urls:{}'.format(batch_id, urls))
#             for i in range(0, len(urls)):
#                 with open(file_path[i], 'rb') as f:
#                     res_upload = requests.put(urls[i], data=f)
#                     if res_upload.status_code == 200:
#                         print(f"{urls[i]} upload success")
#                     else:
#                         print(f"{urls[i]} upload failed")
#         else:
#             print('apply upload url failed,reason:{}'.format(result["msg"]))
#     else:
#         print('response not success. status:{} ,result:{}'.format(response.status_code, response))
# except Exception as err:
#     print(err)

"""
response success. result:{'code': 0, 'msg': 'ok', 'trace_id': '36d1c148ce853162ce50970e0fc28180', 'data': {'batch_id': 'd8b48ba8-10d7-4cb0-8017-7faec7c20e9a', 'file_urls': ['https://mineru.oss-cn-shanghai.aliyuncs.com/api-upload/extract/2026-11-19/d8b48ba8-10d7-4cb0-8017-7faec7c20e9a/5e6da91a-9ac9-4b78-bb23-fef512173159.pdf?Expires=1795138224&OSSAccessKeyId=LTAI5t6sXp5gszd8yWZ85dAL&Signature=fPbO6CFHK9zIX%2BtL66LKt89ZsY4%3D']}}
batch_id:d8b48ba8-10d7-4cb0-8017-7faec7c20e9a,urls:['https://mineru.oss-cn-shanghai.aliyuncs.com/api-upload/extract/2026-11-19/d8b48ba8-10d7-4cb0-8017-7faec7c20e9a/5e6da91a-9ac9-4b78-bb23-fef512173159.pdf?Expires=1795138224&OSSAccessKeyId=LTAI5t6sXp5gszd8yWZ85dAL&Signature=fPbO6CFHK9zIX%2BtL66LKt89ZsY4%3D']
https://mineru.oss-cn-shanghai.aliyuncs.com/api-upload/extract/2026-11-19/d8b48ba8-10d7-4cb0-8017-7faec7c20e9a/5e6da91a-9ac9-4b78-bb23-fef512173159.pdf?Expires=1795138224&OSSAccessKeyId=LTAI5t6sXp5gszd8yWZ85dAL&Signature=fPbO6CFHK9zIX%2BtL66LKt89ZsY4%3D upload success
Process finished with exit code 0
"""

import os
import requests

# token 从环境变量读取，避免密钥进入 Git 历史
# 设置方式（PowerShell，设置后需重开终端）：
#     setx MINERU_TOKEN "你的token"
token = os.getenv("MINERU_TOKEN")
if not token:
    raise RuntimeError("未找到环境变量 MINERU_TOKEN，请先执行 setx MINERU_TOKEN \"你的token\"")
batch_id = "d8b48ba8-10d7-4cb0-8017-7faec7c20e9a"
url = f"https://mineru.net/api/v4/extract-results/batch/{batch_id}"
header = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {token}"
}

res = requests.get(url, headers=header)
print(res.status_code)
print(res.json())
print(res.json()["data"])


"""
https://cdn-mineru.openxlab.org.cn/pdf/2026-11-19/0d542dd8-1547-4974-91b2-bdf895a3cabe.zip
"""