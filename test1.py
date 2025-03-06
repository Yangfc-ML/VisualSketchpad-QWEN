import torch
from transformers import AutoTokenizer, AutoProcessor, Qwen2_5_VLForConditionalGeneration
from autogen.agentchat import ConversableAgent


class QwenConversableAgent(ConversableAgent):
    def __init__(self, model_id="Qwen2.5-VL-3B-Instruct"):
        super().__init__(name="Qwen-VL-Agent")

        # 如果有GPU资源，device_map="auto" 会自动分配到可用的GPU，否则会放到CPU
        # 也可以使用 device_map="cpu" 显式指定放到CPU上
        self.processor = AutoProcessor.from_pretrained("Qwen2.5-VL-3B-Instruct")
        self.model = Qwen2_5_VLForConditionalGeneration.from_pretrained(
            model_id,
            device_map="auto",
            trust_remote_code=True
        ).eval()

        # 用于多轮对话记录 (user, assistant) 的历史
        self.history = []

    def handle_message(self, message: str) -> str:
        """
        使用 Qwen 模型内置的 chat() 方法完成对话。
        注意 Qwen 的 chat() 方法返回 (response, history)，其中 history 可以在多轮对话中复用。
        """
        response, _ = self.model.generate(**message, max_new_tokens=128)
        # 将本轮对话写入 history，以便后续多轮上下文
        self.history.append((message, response))
        generated_ids_trimmed = [
            out_ids[len(in_ids):] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
        ]
        output_text = self.processor.batch_decode(
            generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
        )
        return response


if __name__ == "__main__":
    # 初始化对话 Agent
    agent = QwenConversableAgent()

    print("Qwen2.5-VL-3B-Instruct 对话测试，输入 'exit' 或 'quit' 结束程序。\n")

    while True:
        user_input = input("用户: ")
        if user_input.strip().lower() in ["exit", "quit"]:
            print("结束对话。")
            break

        user_input=agent.processor.apply_chat_template(
            user_input, tokenize=False, add_generation_prompt=True
        )


        response = agent.handle_message(user_input)
        print(f"助手: {response}\n")
