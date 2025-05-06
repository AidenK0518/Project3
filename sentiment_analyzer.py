# Begin by importing PyTorch and Transformers. Most of this is covered in project 1, so comments will be scarce.

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

class SentimentAnalyzer:
    def __init__(self, model_name):
        print(f"Loading model: {model_name}")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.float16,
            device_map="auto"
        )
        self.model_name = model_name

    def analyze_sentiment(self, text):
        # Send phi-2 this exact prompt. By asking it to keep it only to the three words, we can get a defenitive result with a low amount of tokens.
        prompt = (
            "Only using one word, classify the sentiment of the headline as Positive, Negative, or Neutral.\n"
            "Do not explain your reasoning, keep it to one word ONLY.\n"
            f"{text}\nA:"
        )

        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.model.device)

        with torch.no_grad():
            outputs = self.model.generate(**inputs, max_new_tokens=1)

        result = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        # Extract only the part after the prompt (this will be the models answer, which is what we want.)
        answer = result.split("A:")[-1].strip().lower()

        # This is mostly here for debugging, but it will let the user know what the model output is and what the code says the expected answer should be.
        # If there is an error, the extracted answer will differ from what the actual result is.
        print(f"Model output: {result}")
        print(f"Extracted answer: {answer}")

        # Go through the possible ways that it can start, as all three answers differ in the first 3 letters, that is all we need to look at to get our answer.
        if answer.startswith("pos"):
            return "Positive"
        elif answer.startswith("neg"):
            return "Negative"
        elif answer.startswith("neu"):
            return "Neutral"
        else:
            return "Unknown"