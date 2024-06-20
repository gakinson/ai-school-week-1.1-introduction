from langchain_core.messages import AIMessage, HumanMessage,SystemMessage
from langchain_openai import ChatOpenAI

chat = ChatOpenAI()
partnerChat = ChatOpenAI()

chatMessages = [
    SystemMessage(
        content="You are an opinionated developer who is an expert in the knowledge of CRUD applications. You are going to have a discussion with someone about how to build a CRUD application"
    ),
    HumanMessage(
        content="I would like to discuss how to build a CRUD application"
    ),
]

partnerChatMessages = [
    SystemMessage(
        content="You are a naive developer who has little knowledge of CRUD applications. You want to learn how to build a CRUD application from an expert. You are going to have a discussion with someone about how to build a CRUD application."
                "Ensure to ask questions and seek clarification on any topic you do not understand."
    ),
    AIMessage(
        content="I would like to discuss how to build a CRUD application"
    ),
]

print('Expert: ' +  chatMessages[0].content)
print('Naive: ' +  chatMessages[1].content)

for _ in range(5):
    result = chat.invoke(chatMessages).content
    chatMessages.append(AIMessage(content=result))
    partnerChatMessages.append(HumanMessage(content=result))

    print('Expert: ' +  result)

    result2 = partnerChat.invoke(partnerChatMessages).content
    chatMessages.append(HumanMessage(content=result2))
    partnerChatMessages.append(AIMessage(content=result2))
    print('Naive: ' +  result2)



