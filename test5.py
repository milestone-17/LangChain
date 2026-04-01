#接入TavilySearch
import chunk
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
#
# #绑定工具
# tool=TavilySearch(max_results=3) #最大搜索返回结果
# model_with_tools=model.bind_tools([tool])
#
# #添加AiMessages到消息中
# messages=[
#     HumanMessage("南昌今天天气如何")
# ]
# #AIMessages--- AI 大模型返回给你的 “一条回答消息”
# ai_msg=model_with_tools.invoke(messages)
# messages.append(ai_msg)
# for tool_call in ai_msg.tool_calls:
#     tool_msg=tool.invoke(tool_call)
#     messages.append(tool_msg)
# result=model_with_tools.invoke(messages)
# print(result)

#结构化输出
# schema={"foo":"bar"}
#绑定schema ,其实是⽣成⽀持结构化返回的 Runnable 实例  Runnable可以被调用、可以被链式组合、LangChain 里所有组件的 “统一接口”
# 只要是 Runnable，就一定能调用：.invoke(input)
#with_structured_output()
from pydantic import BaseModel,Field
# from typing import List,Optional
# class Joke(BaseModel):
#     """给用户讲一个笑话"""
#     setup:str=Field(description="笑话开头")
#     punchline: str = Field(description="这个笑话的妙语")
#     rating: Optional[int] = Field(
#         default=None, description="从1到10分，给这个笑话评分"
#     )
# class Data(BaseModel):
#     """获取笑话的数据"""
#     jokes:List[Joke]
# model_with_structure=model.with_structured_output(Data)
# # 3. 执⾏
# structured_output = model_with_structure.invoke("请分别讲一个关于骄傲和同理心的笑话，并严格按照JSON格式返回，字段包括 setup, punchline, rating，外层是 jokes 列表"
# )
# print(structured_output)

# from typing import TypedDict
# class User(TypedDict):
#     name: str
#     age: int
#     email: str
#     is_active: bool = True # 默认值
#
# user1: User = {
#     "name": "Bob",
#     "age": 25,
#     "email": "bob@example.com"
# }
# # 类型检查器会捕获这些错误
# bad_user: User = {
#     "name": "Dave",
#     "age": "forty", # 错误：应该是int
#     "emial": "dave@example.com" # 错误：拼写错误
# }

# # 定义输出结构： TypedDict
# from   typing_extensions import  Annotated,TypedDict
# from typing import  Optional
# class Joke(TypedDict):
#     """给⽤⼾讲⼀个笑话。"""
#     setup: Annotated[str, ..., "这个笑话的开头"]
#     punchline: Annotated[str, ..., "这个笑话的妙语"]
#     rating: Annotated[Optional[int], None, "从1到10分，给这个笑话评分"]
# structured_model = model.with_structured_output(Joke)
#
# result = structured_model.invoke("给我讲⼀个关于唱歌的笑话")
# print(result)

#流式输出
# chunks=[]
# for chunk in model.stream("讲一个50字笑话"):
#     chunks.append(chunk)
#     print(chunk.content,end="|",flush=True)
import chunk
#异步输出,协程
# import asyncio
#
# #定义协程
# async def boil_water_async():
#     print("开始煮水")
#     await asyncio.sleep(5)
#     ## 关键！ await 表⽰“等待这个操作完成，但期间让事件循环去做别的事”
#     print("水开了")
# async def sendmessage_async():
#     print("开始发消息")
#     await asyncio.sleep(2)
#     print("发完")
# async def main():
#     # 创建两个任务，并交给事件循环去调度
#     task1 = asyncio.create_task(boil_water_async())
#     task2 = asyncio.create_task(sendmessage_async())
#
#     # 等待两个任务都完成
#     await task1
#     await task2
# asyncio.run(main())

# 异步调⽤
# async def async_stream():
#     print("=== 异步调⽤ ===")
#     async for chunk in model.astream("讲⼀个50字的笑话"):
#        print(chunk.content, end="|", flush=True)
# import asyncio
# asyncio.run(async_stream())

# from langchain_core.output_parsers import StrOutputParser
# parset=StrOutputParser()
# chain=model|parset
# # for chunk in chain.stream("给5句话"):
# #     print(chunk)
#
# #

