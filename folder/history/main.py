from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="llama3.2")

template = """
You are an expert restaurant advisor. Your answers must strictly come from the provided reviews. 
If the reviews do not mention the answer, respond with:
"I’m not sure based on the reviews provided."

Keep your answers short (2–3 sentences). 
Only ask a follow-up question if it is essential for accuracy.

Here is the recent conversation: {history}
Here are some relevant reviews: {reviews}

Here is the question to answer: {question}

"""
prompt = ChatPromptTemplate.from_template(template)

conversation_history = []
MAX_TURNS = 5
chain = prompt | model

first_time = True

while True:
    print("\n\n-------------------------------")
    
    if first_time:
        question = input("Hi! I am your advisor. You can ask me your question\n(press q to quit): ")
        first_time = False
    else:
        question = input("Ask your question (press q to quit): ")
    
    print("\n\n")
    
    if question.lower() == "q":
        break
    
    reviews = retriever.invoke(question)
    recent_history = "\n".join(
        [f"User: {q}\nAssistant: {a}" for q, a in conversation_history[-MAX_TURNS:]]
    )

    result = chain.invoke({"reviews": reviews, "question": question, "history": recent_history})
    print(result)

    conversation_history.append((question, result))
