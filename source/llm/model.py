from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

def generate_code_review(code, file_name):
    """
    Generates a code review using LangChain and OpenAI GPT.
    """
    # LangChain Chat Model
    llm = ChatOpenAI(model="gpt-4", temperature=0.2)

    # Prompt 템플릿
    prompt = ChatPromptTemplate.from_template("""
    You are a senior software engineer tasked with reviewing code. 
    Provide a detailed code review for the following file:
    
    File Name: {file_name}
    Code:
    ```
    {code}
    ```
    
    Please include:
    - Code quality and readability feedback.
    - Suggestions for improvements.
    - Potential bugs or issues.
    - Best practices and optimization recommendations.
    """)

    # 리뷰 생성
    messages = prompt.format_messages(file_name=file_name, code=code)
    response = llm(messages)
    return response.content