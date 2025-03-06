import os

# set up the agent
MAX_REPLY = 10

# set up the LLM for the agent
# os.environ['QWEN_API_KEY'] = 'sk-6d98fbab76b348b0a7ba7b61fe964b3a'

os.environ["AUTOGEN_USE_DOCKER"] = "False"
llm_config={
    "cache_seed": None,
    "config_list": [
        {
            "model": "Qwen2.5-VL-3B-Instruct",
            "temperature": 0.0,
            "api_key":"EMPTY",
            "base_url":"http://localhost:8000/v1"
        }
    ]
}


# use this after building your own server. You can also set up the server in other machines and paste them here.
SOM_ADDRESS = "http://localhost:8080/"
GROUNDING_DINO_ADDRESS = "http://localhost:8081/"
DEPTH_ANYTHING_ADDRESS = "http://localhost:8082/"
