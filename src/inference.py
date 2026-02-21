from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load model
model_path = "models/chatbot-model"

tokenizer = AutoTokenizer.from_pretrained(model_path)

model = AutoModelForCausalLM.from_pretrained(model_path)

model.eval()


def generate_response(user_input):

    prompt = f"User: {user_input}\nBot:"

    inputs = tokenizer(

        prompt,

        return_tensors="pt"
    )

    with torch.no_grad():

        outputs = model.generate(

            inputs["input_ids"],

            max_length=150,

            pad_token_id=tokenizer.eos_token_id,

            do_sample=True,

            temperature=0.7,

            top_p=0.9
        )

    response = tokenizer.decode(

        outputs[0],

        skip_special_tokens=True
    )

    return response.split("Bot:")[-1].strip()