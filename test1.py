# #导入 Python 内置的 os 模块（全称：operating system，操作系统）
# import os
# #从 langchain_openai 这个库中，导入 ChatOpenAI 类
# from langchain_openai import ChatOpenAI
# #从 langchain_core 核心库中，导入两种消息格式：HumanMessage 和 SystemMessage。
# from langchain_core.messages import HumanMessage, SystemMessage
# #上面都是导入依赖
# from langchain_core.output_parsers import StrOutputParser
# # //定义大模型
# model = ChatOpenAI(
#     model="deepseek-chat",
#     api_key=os.getenv("DeepSeek_API_KEY"),
#
#     # api_key="sk-6f175e46c61a458aa6afa18eadb7cf02",
#     base_url="https://api.deepseek.com/v1"
#
# )
#
# #定义消息列表
# # SystemMessage ：表⽰ 系统⻆⾊ 消息，系统消息通常作为输⼊消息序列中的第⼀条传⼊，是
# # ⽤来启动 AI ⾏为的消息。
# # • HumanMessage ：表⽰ ⽤⼾⻆⾊ 消息，是来⾃⽤⼾的、从⽤⼾传递到模型的消息。
# from langchain_core.messages import HumanMessage,SystemMessage
# messages =[
#     SystemMessage(content="Translate the following from English into Chinese"),
#     HumanMessage(content="hi what's up,how are you?"),
# ]
#
# # 使⽤ .invoke ⽅法进⾏⼤模型调⽤
# #result=model.invoke(messages)
# #print(result)
#
#
# #若只想输出聊天模型返回的结果字符串，可以使⽤ StrOutputParser 输出解析器组件，将⼤模型输出结果解析为最可能的字符串,
# parser = StrOutputParser()
# #print(parser.invoke(result))
# #结果--你好
#
#
# #链式结构体现--将组件链起来 ,invoke ---调用/执行/运行/发起请求
# #Runnable接口是使用LangChain Components的基础
# chain = model | parser  ##顺序不能反
# print(chain.invoke(messages))
# #流式输出
# for chunk in chain.stream(messages):
#     print(chunk,end="",flush=True)
#
# #上面的chain
# #它通过两个 Runnable 对象去创建⼀个 RunnableSequence 。实际上 LangChain 重载了 | 运算符，使⽤ | 运算符就相当于：
#     # from langchain_core.runnables import RunnableSequence
#     # chain = RunnableSequence(first=model, last=parser)
# from langchain_core.runnables import RunnableSequence
#
# Chain=RunnableSequence(first=model,last=parser)
# print(Chain.invoke(messages))
# #也可使用.pipe代替|
# chains=model.pipe(parser)
# print(chains.invoke(messages))


