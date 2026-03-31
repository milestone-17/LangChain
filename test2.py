import  os
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage,HumanMessage
from langchain_core.output_parsers import StrOutputParser
#
# #一:api调用
# model=ChatOpenAI(
#     model="deepseek-chat",
#     api_key=os.getenv("DeepSeek_API_KEY"),
#     base_url="https://api.deepseek.com/v1", #指定请求路径
#      max_tokens=None,   #超时时间
#     temperature=2.0,
#     timeout=None
#
# )
#
# #定义消息
# messages=[
#     SystemMessage(content="补全故事,200字内"),
#     HumanMessage(content="一只猫在?")
# ]
#
# # //定义输出解析组件
# parser=StrOutputParser()
# chain=model|parser
# print(chain.invoke(messages))

#二:init_chat_model  LangChain封装了更上层的方法,进行初始化模型
from langchain.chat_models import init_chat_model
# deepseek_model=init_chat_model(
#     model="deepseek-chat",
#     model_provider="deepseek"
# )
# print(f"DeepSeek model: {deepseek_model.invoke("你是谁").content}"+"\n")
# print(deepseek_model.invoke("hai").content)

#定义可配置模型
config=init_chat_model(timeout=None)
#运行指定模型
 #定义消息
messages=[
    SystemMessage(content="补全故事,200字内"),
    HumanMessage(content="一只猫在?")
]
config.invoke(input=messages,config={"first_model":"deepseek-chat"})


