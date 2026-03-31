import  os
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from typing_extensions import Annotated
from langchain_core.messages import SystemMessage,HumanMessage
from langchain_core.output_parsers import StrOutputParser
from typing_extensions import Annotated
#一:api调用
model=ChatOpenAI(
    model="deepseek-chat",
    api_key=os.getenv("DeepSeek_API_KEY"),
    base_url="https://api.deepseek.com/v1", #指定请求路径
)
@tool
def add(
    a: Annotated[int, ..., "First integer"],
    b: Annotated[int, ..., "Second integer"]
) -> int:
    """Add two integers."""
    return a + b
@tool
def multiply(
    a: Annotated[int, ..., "First integer"],
    b: Annotated[int, ..., "Second integer"]
) -> int:
    """Multiply two integers."""
    return a * b
#绑定工具,返回一个Runnable案例`
# tools=[add,multiply]
# model_with_tools=model.bind_tools(tools)
#
# #调用工具
# result=model_with_tools.invoke("3*5等于多少")
# print(result)
# # ⼯具调⽤的⼀个关键原则是，模型根据输⼊的相关性决定何时使⽤⼯具。模型并不总是需要调⽤⼯
# ret =model_with_tools.invoke(str(5*6))
# print(ret)

#强制模型使用工具
# tools=[add,multiply]
# model_with_tools=model.bind_tools(tools,tool_choice="any") #至少选择一个工具
# result=model_with_tools.invoke("3*5等于多少")
# print(result)

#遍历工具调用请求
tools=[add,multiply]
model_with_tools=model.bind_tools(tools)
#添加AIMessages到消息中去
messages=[
    HumanMessage("9*5等于几?9+6等于几?")
]
ai_msg=model_with_tools.invoke(messages)
messages.append(ai_msg)
for tool_call in ai_msg.tool_calls:
    #根据工具名选择对应工具函数(不区分大小写)
    #工具名字 → 工具函数的对照表
    tool_map = {"add": add, "multiply": multiply}
    #tool_call 要调用某name函数
    selected_tool = tool_map[tool_call["name"].lower()]
    #执行工具调用,返回ToolMessage
    tool_msg=selected_tool.invoke(tool_call)
    #将ToolMessage加入消息
    messages.append(tool_msg)
print(messages)
#总共调用两次大模型
result=model.invoke(messages)
print(result)


