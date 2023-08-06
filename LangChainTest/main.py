SERPAPI_API_KEY = '20a03798fc4bc6ac6fc3863067dbd380c06b35267d2f60b03109c992f1088dfb'
OPENAI_API_KEY = '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'

from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate, LLMChain
from langchain.prompts.chat import ChatPromptTemplate, SystemMessagePromptTemplate, AIMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from langchain.document_loaders import PyPDFLoader, TextLoader
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import RetrievalQA, RetrievalQAWithSourcesChain
from langchain.text_splitter import CharacterTextSplitter

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

class PaperAsk:
    def __init__(self, paperLocs):
        self.chatLLM = ChatOpenAI(temperature=0)
        self.papers = []

        embeddings = OpenAIEmbeddings()
        self.db = None

        for loc in paperLocs:
            docs = TextLoader(loc).load_and_split()
            if self.db is None:
                self.db = FAISS.from_documents(docs, embeddings)
            else:
                self.db.add_documents(docs)
            
        # self.index = VectorstoreIndexCreator().from_loaders(list(map(lambda paperLoc: TextLoader(paperLoc, encoding='utf8'), paperLocs)))
    
    def addPaper(self, fileLoc: str):
        # loader = PyPDFLoader(fileLoc)
        loader = TextLoader(fileLoc)
        docs = loader.load_and_split()
        self.db.add_documents(docs)
    
    def ask(self, question: str):
        print(f"{color.BOLD}Question: {question}{color.END}")
        # docs = self.db.similarity_search_with_score(question)
        # for idx, doc in enumerate(docs):
        #     print(f"{idx}. {doc}\n")

        retriever = self.db.as_retriever()
        qa = RetrievalQAWithSourcesChain.from_chain_type(llm=self.chatLLM, chain_type="stuff", retriever=retriever, return_source_documents=True)
        
        response = qa({"question": question})
        print(response['answer'])
        print(response['sources'])


        # response = self.index.query_with_sources(question)
        # print("Answer:", response['answer'])
        # print("Sources:", response['sources'])


        # faiss_index = FAISS.from_documents(self.papers[0][1], OpenAIEmbeddings())
        # docs = faiss_index.similarity_search(question, k=2)
        # for doc in docs:
        #     print(doc)
        #     print("\n--------")
            # print(f"{str(doc.metadata['page'])}: {doc.page_content[:300]}")

    def run(self):
        while True:
            response = input("[>] ")
            if response[0] == 'q':
                pass
            elif response[0] == 'a':
                pass

paperAsk = PaperAsk([
    'files/test0.txt',
    'files/sotu.txt',
    'files/biography.txt',
    'files/research0.txt'
])
# paperAsk.ask("Give a short description of all of Evelyn Hastings's honors and achievements.")
# paperAsk.ask("What's a nirfhal?")
paperAsk.ask('What did the president say about Ketanji Brown Jackson?')
# paperAsk.addPaper("files/test0.txt")
# paperAsk.ask("What is a nirfhal?")


# llm = OpenAI(temperature=0)
# chat = ChatOpenAI(temperature=0)

# response = chat([
#     SystemMessage(content="Act like a rude assistant."),
#     HumanMessage(content="Do you like me?")
# ])

# print(llm.predict('say hi!'))
# print(llm)