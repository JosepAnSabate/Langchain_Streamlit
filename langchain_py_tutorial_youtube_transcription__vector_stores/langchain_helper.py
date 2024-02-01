from langchain.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import OpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.vectorstores import FAISS


from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings()

def create_vector_db_from_youtube_url(video_url: str) -> FAISS:
    loader = YoutubeLoader.from_youtube_url(video_url)
    transcript = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, # 1000 characters
        chunk_overlap=100 # 100 characters overlap
        )
    
    docs = text_splitter.split_documents(transcript)
    
    # vectore store
    # https://python.langchain.com/docs/integrations/vectorstores/faiss

    db = FAISS.from_documents(docs, embeddings)
    return db#docs

#print(create_vector_db_from_youtube_url(video_url))

def get_response_from_query(db, query, k=4):
    docs = db.similarity_search(query, k)
    docs_page_content= " ".join(
        [d.page_content for d in docs]
    )

    llm = OpenAI(model='gpt-3.5-turbo-instruct')

    prompt = PromptTemplate(
        input_variables=['question', 'docs'],
        template = """
        You're a helpfull youtube assistant who can answe questions 
        about the video based on the transcript.

        Answer the following question: {question}
        By searching the transcript of the video: {docs}

        Only use the factual information from the transcription to answer.

        If you feel like you can't answer the question, just say: I don't know.

        Your answer should be detailed.
        """
    )

    chain = LLMChain(llm=llm, prompt=prompt)

    response = chain.run(
        question=query, 
        docs=docs_page_content # d'on treu la info per respondre, transcript in db vectorstore
        )
    
    response = response.replace('\n', '')

    return response