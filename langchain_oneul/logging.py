import os

def langsmith(progect_name=None, set_enable=True) :
    if set_enable :
        langchain_key = os.environ.get("LANGCHAIN_API_KEY", "")
        langsmith_key = os.environ.get("LANGSMITH_API_KEY", "")
        
        # 더 긴 API 키 선택
        result = langchain_key if len(langchain_key) > len(langsmith_key) else langsmith_key
        
        if result.strip() == "" :
            print("❗LangChain/LangSmith API key is not set.")
            return
        
        os.environ["LANGSMTH_ENDPOINT"] = (
            "https://api.smith.langchain.com" # LangSmith API 엔드포인트
            )
        os.environ["LANHSMITH_TRACING"] = "true" # 활성화
        os.environ["LANGSMITH_PROJECT"] = progect_name # LangSmith 프로젝트 이름
        print(f"LangSmith 추적을 활성화합니다.\n[프로젝트명]\n{progect_name}")
    else :
        os.environ["LANGSMITH_TRACING"] = "false" # 비활성화
        print("LangSmith 추적을 비활성화합니다.")
        
def env_variable(key, value) :
    os.environ[key] = value
    