# 如果本地尚未安装 huggingface_hub，请先安装
# !pip install huggingface_hub

from huggingface_hub import snapshot_download

# 指定模型仓库
repo_id = "Qwen/Qwen2.5-VL-7B-Instruct"

# 指定下载后保存的本地目录
local_dir = "Qwen2.5-VL-7B-Instruct"

# 开始下载
snapshot_download(
    repo_id=repo_id,
    local_dir=local_dir,
    revision="main",        # 默认分支/版本，可改为其它分支或commit ID
    allow_patterns=["*"],   # 允许下载所有文件
)

print("模型下载完成，保存在：", local_dir)
