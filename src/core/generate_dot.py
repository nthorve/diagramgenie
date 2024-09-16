import json
import urllib
import os


class AzureInference:
    def __init__(self, **kwargs):
        self.url = kwargs["url"]
        self.key = kwargs["key"]

    def _invoke_endpoint(self, data):
        body = str.encode(json.dumps(data), encoding="utf-8")
        headers = {
            "Content-Type": "application/json",
            "Authorization": ("Bearer " + self.key),
            # "api-key": self.key
        }
        req = urllib.request.Request(self.url, body, headers)
        try:
            response = urllib.request.urlopen(req)
            result = response.read()
            return result.decode("utf-8")
        except urllib.error.HTTPError as error:
            print("The request failed with status code: " + str(error.code))
            print(error.info())
            print(error.read().decode("utf8", "ignore"))
            return "{}"

    def invoke_inference(self, prompt):
        response = self._invoke_endpoint(prompt)
        try:
            response_dict = json.loads(response)
            label = response_dict["choices"][0]["message"]["content"].strip()
        except Exception as e:
            print(e)
            label = "$$error$$"
        return label


def generate_dot(
    system_prompt, user_input, temperature=0.6, top_p=0.9, max_new_tokens=2048
):

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input},
    ]
    az_model_inf = AzureInference(url=os.getenv("ENDPOINT"), key=os.getenv("API_KEY"))
    response_text = az_model_inf.invoke_inference(
        {
            "messages": messages,
            "temperature": temperature,
            "top_p": top_p,
            "max_new_tokens": max_new_tokens,
        }
    )
    return response_text
