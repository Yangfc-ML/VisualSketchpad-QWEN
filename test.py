import autogen

# 配置 OpenAI API 密钥
config_list = [
    {
        "model": "Qwen2.5-VL-3B-Instruct",
        "api_key": "EMPTY",
        "base_url": "http://localhost:8000/v1"
    }
]

# 创建用户代理
user_proxy = autogen.UserProxyAgent(
    name="User",
    human_input_mode="ALWAYS",
    is_termination_msg=lambda x: x.get("content", "").strip().lower() == "exit",
    code_execution_config={"use_docker": False}  # 不执行代码，只进行对话
)

# 创建 AI 代理
assistant = autogen.AssistantAgent(
    name="Assistant",
    llm_config={"config_list": config_list, "temperature": 0.2, "frequency_penalty": 0.5},
    system_message="你是有问必答的 AI 助手，回答时需详细完整！"
)

# 代理之间的交互
user_proxy.initiate_chat(assistant, message="你好！你叫什么名字，你都能干什么？")
