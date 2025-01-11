import openai
import time

def openai_completion(messages, api_key, model="", temperature=0, max_tokens=256, n=1, patience=100, sleep_time=0):
    while patience > 0:
        patience -= 1
        try:
            response = openai.ChatCompletion.create(model=model,
                                                    messages=messages,
                                                    api_type="azure",
                                                    api_base="https://lechuang.openai.azure.com",
                                                    api_key=api_key,
                                                    api_version="2023-05-15",
                                                    engine="lechuang-gpt-35-bak",
                                                    temperature=temperature,
                                                    max_tokens=max_tokens,
                                                    n=n)
            if n == 1:
                prediction = response['choices'][0]['message']['content'].strip()
                if prediction != "" and prediction != None:
                    return prediction
            else:
                prediction = [choice['message']['content'].strip() for choice in response['choices']]
                if prediction[0] != "" and prediction[0] != None:
                    return prediction

        except Exception as e:
            print(e)
            if sleep_time > 0:
                time.sleep(sleep_time)
    return ""


messages = [
    {"role": "user", "content": "hello"},
]
print(openai_completion(messages, "bc709d6234e04a80ab2d744eb2434086"))