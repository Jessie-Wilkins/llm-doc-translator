from langchain.llms import Ollama
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.callbacks.manager import CallbackManager
import easyocr
import cv2
import re

def extract_text(image_path):
    reader = easyocr.Reader(['ch_sim','en'])
    result = reader.readtext(image_path, detail=0, )
    return result

def extract_chinese_text(input_text):
    result_text = ''
    for item in input_text:
        
        # Filter out the non-Chinese characters using regular expressions
        chinese_match = re.search('[^\u0000-\u007F]', item)

        if chinese_match:
            result_text += f'{item}\n'.replace(" ", "").replace("'","").replace("\"","")

    return result_text


# Input the path of the image you want to extract text from
image_path_file = 'pictures/test.jpg'  # Replace this with your desired image path

image_path = cv2.imread(image_path_file)

text = extract_text(image_path)



chinese_text = extract_chinese_text(text)
print(chinese_text)


template = """
Translate this to {translation_language}:
{text_to_translate}
"""

prompt = PromptTemplate(
    template=template, 
    input_variables=["translation_language", "text_to_translate"]
)

llm = Ollama(
    model="mistral-translator",
    callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
    verbose=True
    )

llm_chain = LLMChain(llm=llm, prompt=prompt)

llm_chain.run(translation_language="English", text_to_translate=chinese_text)