import openai;
from openai import OpenAI
from dotenv import load_dotenv
import os

class Summarizer:
    load_dotenv()
    messages = []
    api_key = os.getenv("OPEN_AI_API_KEY")
    openai_client = OpenAI(api_key=api_key)  

    
    def get_completion_openai(self,prompt, model="gpt-4o-mini"):
        self.messages.append({"role": "user", "content": prompt})
        response = self.openai_client.chat.completions.create(model=model,messages=self.messages, temperature=1) 
        # this is the degree of randomness of the model's output) 
        self.messages.append({"role":"assistant", "content": response.choices[0].message.content})
        return response.choices[0].message.content

    def main():
        #Test Open AI API
        """
        question = input("What is your question: ")
        while(question!=""):
            print(self.get_completion_openai(question))
            question = input("What is your question ")
        """

if __name__ == "__main__":
    summarizer_instance = Summarizer()  # Create an instance of the AI class
    summarizer_instance.main()
