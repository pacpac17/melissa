import re 
from ollama import chat, ChatResponse

def logic(message):
    response = chat(model='qwen3:1.7b', messages=[
        {
            'role': 'system',
            'content': 'You are a helpful virtual assistant named Melissa. Give concise replies.',
        },
        {
            'role': 'user',
            'content': message or 'hi',
        },
    ])
    # Clean the response content
    # if 'content' in response.message and response.message['content']:
    #     response.message['content'] = re.sub(r'<think>.*?</think>', '', response.message['content'], flags=re.DOTALL).strip()

    if response.message.thinking:
        print('Thinking: ')
        print(response.message.thinking + '\n\n')
        return response.message.thinking
    if response.message.content:
        print('Content: ')
        print(response.message.content + '\n')
        return response.message.content
    
    return "Nanaicucas...."





