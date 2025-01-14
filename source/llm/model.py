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
	당신은 코드 리뷰 작업을 담당하는 최고의 시니어 소프트웨어 엔지니어입니다.
	다음 파일에 대한 자세한 코드 리뷰를 제공해주세요.:
	
	File Name: {file_name}
	Code:
	```
	{code}
	```
	
	포함 되어야할 내용:
	- 코드 품질과 가독성 피드백.
	- 코드 개선을 위한 제안.
	- 가능한 버그나 이슈.
	- 모범 사례와 최적화 권장 사항.
	""")

	# 리뷰 생성
	messages = prompt.format_messages(file_name=file_name, code=code)
	response = llm(messages)
	return response.content