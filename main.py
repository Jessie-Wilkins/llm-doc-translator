from langchain.llms import Ollama
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.callbacks.manager import CallbackManager

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

llm_chain.run(translation_language="Chinese", text_to_translate="I cross the street to go to work.")