#接入TavilySearch
import  os
from langchain_openai import  ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain_tavily import  TavilySearch

model=ChatOpenAI(
    model="deepseek-chat",
    api_key=os.getenv("DeepSeek_API_KEY"),
    base_url="https://api.deepseek.com/v1", #指定请求路径
)

#绑定工具
tool=TavilySearch(max_results=3) #最大搜索返回结果
model_with_tools=model.bind_tools([tool])

#添加AiMessages到消息中
messages=[
    HumanMessage("南昌今天天气如何")
]
#AIMessages--- AI 大模型返回给你的 “一条回答消息”
ai_msg=model_with_tools.invoke(messages)
messages.append(ai_msg)
for tool_call in ai_msg.tool_calls:
    tool_msg=tool.invoke(tool_call)
    messages.append(tool_msg)
result=model_with_tools.invoke(messages)
print(result)


