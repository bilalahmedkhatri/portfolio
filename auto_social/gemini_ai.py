import google.generativeai as genai
import os

class llm_models_auto:

    def __init__(self, prompt, model_api_key=None, AI_model="gemini-1.5-flash"):
        self.prompt= prompt
        self.ai_model = AI_model
        self.model_api_key = model_api_key

    def Generate_gemini_res(self):
        gen = genai.configure(api_key = self.model_api_key)
        model = genai.GenerativeModel(str(self.ai_model))
        response = model.generate_content(self.prompt)
        return response.text

API_KEY = "AIzaSyDGW8WxiJxK6X-EUnNq5Haou4Ld5oF8feA"
# prompt = "I am generating autobot with gemini which can post on linkedin on daily basis give some examples"

prompt = 'here is link, check this get insightfull data from this link, "https://www.linkedin.com/posts/iamarifalam_%F0%9D%97%96%F0%9D%97%BC%F0%9D%97%BA%F0%9D%97%BD%F0%9D%97%B9%F0%9D%97%B2%F0%9D%98%81%F0%9D%97%B2-%F0%9D%97%A6%F0%9D%97%A4%F0%9D%97%9F-%F0%9D%97%A6%F0%9D%98%86%F0%9D%97%B9%F0%9D%97%B9%F0%9D%97%AE%F0%9D%97%AF%F0%9D%98%82%F0%9D%98%80-activity-7243865319864213504-TWbd?utm_source=share&utm_medium=member_desktop"'
result = llm_models_auto(prompt, API_KEY)

print(result.Generate_gemini_res())

