from agents.agent import agent


result = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": "show all employees"
        }
    ]
})


for message in result["messages"]:
    print(message.content)
