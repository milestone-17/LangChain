import  os
from langchain_openai import  ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain_tavily import  TavilySearch

model=ChatOpenAI(
    model="deepseek-chat",
    api_key=os.getenv("DeepSeek_API_KEY"),
    base_url="https://api.deepseek.com/v1", #指定请求路径
    # model="qwen-max",
    # api_key=os.getenv("QWEN_API_KEY"),  # 使用千问的 API Key
    # base_url="https://dashscope.aliyuncs.com/compatible/v1",  # 千问的正确地址
)
# from pydantic import BaseModel, Field
# from langchain_core.tools import tool
# from langchain_core.messages import HumanMessage
# # 结构输出对象
# class SearchResult(BaseModel):
#     """结构化搜索结果。"""
#     query: str = Field(description="搜索查询")
#     findings: str = Field(description="调查结果摘要")
# @tool
# def web_search(query: str) -> str:
#     """在⽹上搜索信息。
#     Args:
#     query: 搜索查询
#     """
#     return "西安今天多云转⼩⾬，⽓温18-23度，东南⻛2级，空⽓质量良好"
# # ⼿动将⼯具结果加⼊消息列表
# model_with_search = model.bind_tools([web_search])
# messages = [
# HumanMessage("搜索当前最新的西安的天⽓")
# ]
# ai_msg = model_with_search.invoke(messages)
# messages.append(ai_msg)
# for tool_call in ai_msg.tool_calls:
#     tool_msg = web_search.invoke(tool_call)
#     messages.append(tool_msg)
#
# from langchain_core.prompts import ChatPromptTemplate
#
# # 在提示词里明确要求 JSON 格式
# prompt = ChatPromptTemplate.from_messages([
#     ("system", "你是一个助手，请用 JSON 格式回答，包含字段")])
# result = model.invoke(messages)
# print(result)
# messages = [
#     {"role": "user", "content": "Hello, Who are you?"},
#     {"role": "assistant", "content": "I'm doing well, thank you for asking."},
#     {"role": "user", "content": "Can you tell me a joke?"}
# ]
# result = model.invoke(messages)
# print(result)

#
# #跨聊天模型使⽤
# deepseek_model = init_chat_model("deepseek-chat", model_provider="deepseek")

#内存缓存,实现多轮对话
# from langchain_core.messages import  HumanMessage,SystemMessage
# from langchain_core.chat_history import BaseChatMessageHistory,InMemoryChatMessageHistory
# from langchain_core.runnables.history import RunnableWithMessageHistory
# stort={}
# 接受⼀个 session_id 并返回⼀个消息历史对象。
# 这个 session_id ⽤于区分不同的对话，并应作为配置的⼀部分在调⽤新链时传⼊
# def get_session_histroy(session_id:str)->BaseChatMessageHistory:
#     if session_id  not in stort:
#     # InMemoryChatMessageHistory() 将消息存储在内存列表中。
#         stort[session_id] = InMemoryChatMessageHistory()
#     return stort[session_id]
# # 包装model，管理聊天消息历史记录
# with_message_history = RunnableWithMessageHistory(model,get_session_histroy)
# config={"configurable":{"session_id":"1"}}   #模型会记住这个 ID:1 下的所有历史对话，实现连贯聊天
# with_message_history.invoke(
#     [HumanMessage(content="Hi! I'm Bob")],
#     config=config,
# ).pretty_print()
# with_message_history.invoke(
#     [HumanMessage(content="What's my name?")],
#     config=config,
# ).pretty_print()

#消息裁剪
# from langchain_core.messages import HumanMessage,SystemMessage,AIMessage,trim_messages
#
# messages=[
#     SystemMessage(content="you're a good assistant"),
#     HumanMessage(content="hi! I'm bob"),
#     AIMessage(content="hi!"),
#     HumanMessage(content="I like vanilla ice cream"),
#     AIMessage(content="nice"),
#     HumanMessage(content="whats 2 + 2"),
#     AIMessage(content="4"),
#     HumanMessage(content="thanks"),
#     AIMessage(content="no problem!"),
#     HumanMessage(content="having fun?"),
#     AIMessage(content="yes!"),
#     HumanMessage(content="What's my name?"),
# ]
# from langchain_core.runnables import RunnableLambda
# #裁剪
# trimmer=trim_messages(
#     max_tokens=60,  # 你要保留的最大 token 数
#     strategy="last",  # 保留最后 N 个 token
#     token_counter=model,  # 用模型自带的 token 计算器
#     include_system=True,  # 是否包含 system prompt
#     allow_partial=False,
#     start_on="human",  # 从 user 消息开始裁剪
# )
# # print(model.invoke(messages))
# print(trimmer.invoke(messages))


#消息过滤
# from langchain_core.messages import HumanMessage, SystemMessage, AIMessage,filter_messages
# # 历史消息记录
# messages = [
#     SystemMessage("你是⼀个聊天助⼿", id="1"),
#     HumanMessage("⽰例输⼊", id="2"),
#     AIMessage("⽰例输出", id="3"),
#     HumanMessage("真实输⼊", id="4"),
#     AIMessage("真实输出", id="5"),
# ]
# #按类型
# print(filter_messages(messages,include_types="human"))
# #按类型+ID
# print(filter_messages(messages,include_types=[HumanMessage,AIMessage],exclude_ids=["3"]))


from langchain_core.prompts import PromptTemplate
# #字符串模板
# #1.定义模板
# prompt_template=PromptTemplate.from_template("Translate the following into {language}")
# #2.实例化模拟
# print(prompt_template.invoke({"language":"Chinese"}))

#聊天消息模板
# from langchain_core.prompts import  ChatPromptTemplate
# chatprompt_template=ChatPromptTemplate(
#     [
#         ("system", "Translate the following into {language}."),
#         ("user", "{text}")
#     ]
# )
# messagesValue=chatprompt_template.invoke(
#     {
#         "language":"Chinese",
#         "text":"What are you talking about?"
#     }
# )
# print(messagesValue.to_messages())

from langsmith import  Client  # 它就是导入 LangSmith 的客户端工具，用来手动上传、查看、管理你的 AI 调用日志。
# 从 hub 拉取 "hardkothari/prompt-maker" 提⽰词模板。
client=Client()
prompt=client.pull_prompt("hardkothari/prompt-maker",include_model=True)  #true连模板里绑定的模型配置一起下载

#定义链
chain=prompt | model
while True:
    task=input("\n你当前的任务是什么(输入quit退出聊天)")
    if task == 'quit':
        break
    lazy_prompt=input("\n你当前的提示词是什么(输入quit退出聊天)")
    if lazy_prompt=='quit':
        break
    print("\n Response:")
    chain.invoke({"lazy_prompt":lazy_prompt,"task":task}).pretty_print()
