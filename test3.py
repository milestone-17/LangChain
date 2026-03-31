# tool

import os
from langchain_openai import  ChatOpenAI
from langchain_core.tools import  tool
from langchain_core.runnables import  RunnableConfig
# @tool
# def multiply(a,b)->int:
#     #没有下面的注释会报错,没有提供文档字符串,下面的注释,编译器可以看见
#     """Multiply two numbers
#     Args:
#         a:First number
#         b:Second number
#     """
#     return a*b
# print(multiply.invoke({"a":4,"b":5}))  #需要使用大括号指明哪个参数是什么   Schema = 工具的参数规则
# print(multiply.name)
# print(multiply.description)
# print(multiply.args)

#模式一:依赖Pydantic类 #py+dantic(data,数据)
# from pydantic import BaseModel,Field
# # BaseModel 是 Pydantic 里的 **“数据模板基类”**
# # class AddInput(BaseModel) 就是在定义一个「数据格式说明书」 ,1.强制数据检验 2.自动生成Schema  3,自带序列化
# # Field 是给字段加「额外说明和约束」的工具，相当于给你的数据模板加备注和校验规则  1.给字段加描述,就像前面的注释   设置默认值 / 必填项
# class AddInput(BaseModel):
#     """"Add two numbers"""
#     a:int=Field(...,description="First number")
#     b:int=Field(...,description="Second number")
# class MutilOutput(BaseModel):
#     """"Multiply two numbers"""
#     a:int=Field(5,description="First number")
#     b:int=Field(...,description="Second number")
# # 定义工具
# @tool(args_schema=AddInput)
# def add(a,b):
#     #不用提供描述
#     return a*b
# @tool(args_schema=MutilOutput)
# def multiply(a,b):
#     return a*b
# print(add.invoke({"a":4,"b":5}))
# print(add.name)
# print(add.description)
# print(add.args)
#
# print(multiply.invoke({"b":5}))

# #模式二:依赖Annotated
# from typing_extensions import Annotated
# @tool
# def add(
#         a:Annotated[int,...,"First number"],
#          b:Annotated[int,...,"Second number"]
# )->int:
#     """Add two numbers together."""
#     return a+b
# print(add.invoke({'a':1,'b':2})),
# print(add.args)
# print(add.__annotations__)

# 使⽤ StructuredTool 类提供的函数创建⼯具
# from langchain_core.tools import StructuredTool
# from pydantic import BaseModel,Field
# class AddNumber(BaseModel):
#     a:int=Field(...,description="First number")
#     b:int=Field(...,description="Last number")
# def add(a: int, b: int) -> int:
#     return a+b
# calcultator_tool=StructuredTool.from_function(
#     func=add, #要设置的⼯具函数
#     name="Add",#⼯具名称。默认为函数名称。
#     description="两数相加",
#     args_schema=AddNumber,
# )
# # args=AddNumber(2,3)
# print(calcultator_tool.invoke({"a":2,"b":3}))
# print(calcultator_tool.name)
# print(calcultator_tool.description)
# print(calcultator_tool.args_schema)

# 加⼊ response_format 配置
from langchain_core.tools import StructuredTool
from pydantic import BaseModel,Field
from typing import List,Tuple
class Calcutor(BaseModel):
    a:int=Field(...,description="Fisrt")
    b:int=Field(...,description='Last')
def mutily(a:int,b:int)->Tuple[str,List[int]]:
    nums=[a,b]
    content=f"{nums}相乘结果{a*b}"
    return content,nums
caluctor_tool=StructuredTool.from_function(
    func=mutily,
    name="mutilY",
    description="两数相乘",
    args_schema=Calcutor,
    response_format="content_and_artifact"
)
print(caluctor_tool.invoke({'a':3,'b':2}))

# 若想要看到⼯具返回的元组，我们需要模拟⼤模型调⽤⼯具的姿势，
print(caluctor_tool.invoke(
    {
        "name":"Calcutor",
        "args":{"a":3,"b":2},
        "id":"123",
        "type":"tool_call", #必须
    }
))




