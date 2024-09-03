from langchain import LLMChain
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from pydantic import BaseModel, Field


class Recipe(BaseModel):
    ingredients: list[str] = Field(description="List of ingredients")
    steps: list[str] = Field(description="List of steps")


parser = PydanticOutputParser(pydantic_object=Recipe)
format_instructions = parser.get_format_instructions()

template = """
料理のレシピを考えてください。
{format_instructions}
料理名: {dish}
"""

prompt = PromptTemplate(
    template=template,
    input_variables=["dish"],
    partial_variables={"format_instructions": format_instructions},
)
formatted_prompt = prompt.format(dish="カレー")

llm = ChatGroq(
    model="mixtral-8x7b-32768",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

chain = LLMChain(prompt=prompt, llm=llm, output_parser=parser)

recipe = chain.run(dish="オムライス")
print(recipe)
