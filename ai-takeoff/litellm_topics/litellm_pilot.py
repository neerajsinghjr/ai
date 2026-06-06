from os import environ
from litellm import completion, _turn_on_debug
from dotenv import find_dotenv, load_dotenv


load_dotenv(find_dotenv())


"""
ModelResponse(
    id='k1u2hk3u123090', 
    created=1780524593, 
    model='gemini-2.5-flash', 
    object='chat.completion', 
    system_fingerprint=None, 
    choices=[
        Choices(
            finish_reason='stop', 
            index=0, 
            message=Message(
                content='Hello!\n\nAs an AI, I don\'t have feelings or a physical state like humans do, so I can\'t really "be" good or bad. However, I am fully operational and ready to assist you!\n\nHow are you doing today? And how can I help you?', 
                role='assistant', 
                tool_calls=None, 
                function_call=None, 
                images=[], 
                thinking_blocks=[], 
                provider_specific_fields=None
            )
        )
    ], 
    usage=Usage(
        completion_tokens=549, 
        prompt_tokens=7, 
        total_tokens=556, 
        completion_tokens_details=CompletionTokensDetailsWrapper(
            accepted_prediction_tokens=None, 
            audio_tokens=None, 
            reasoning_tokens=489, 
            rejected_prediction_tokens=None, 
            text_tokens=60, 
            image_tokens=None, 
            video_tokens=None
        ), 
    prompt_tokens_details=PromptTokensDetailsWrapper(audio_tokens=None, cached_tokens=None, text_tokens=7, image_tokens=None, video_tokens=None), cache_read_input_tokens=None), 
    vertex_ai_grounding_metadata=[], 
    vertex_ai_url_context_metadata=[], 
    vertex_ai_safety_results=[], 
    vertex_ai_citation_metadata=[], 
    service_tier='default'
)
"""

def _quit():
    return ["quit", "exit", "babye", "bye-bye", "bye", "goodbye", "ba-bye"]


def llm_run():
    ask = str(input("ask: "))
    model = f"{environ.get('GEMINI_MODEL_PROVIDER')}/{environ.get('GEMINI_MODEL_NAME')}"
    messages = [
        {"role": "system", "content": "you are a personal assistant who is always up to serve his master in one line. If master ask from brief then he would preferene to guide him diagram and detail roadmap structure."},
        {"role": "user", "content": ask},
    ]
    while ask.lower() not in _quit():
        # _turn_on_debug()
        response = completion(
          model=model,
          messages=messages,
        )
        if not response.choices[0].message.content:
            print(f"null reply: {response}")
        else:
            print(f"reply: {response.choices[0].message.content}")
            messages.append({"assistant": response.choices[0].message.content})
        print(f"completion_tokens: {response.usage.completion_tokens}")
        print(f"prompt_tokens: {response.usage.prompt_tokens}")
        print(f"total_tokens: {response.usage.total_tokens}")
        ask = str(input("ask: "))
        if not ask.lower() in _quit():
            messages.append({"role": "user", "content": ask})
    print("App Terminated Successfully")


if __name__ == "__main__":
    try:
        llm_run()
    except Exception as ex:
        print(f"App Terminated with Exception: {ex}")