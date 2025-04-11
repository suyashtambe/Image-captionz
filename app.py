from flask import Flask, request, jsonify
from flask_cors import CORS
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Check if CUDA is available and set the device accordingly
device = 'cuda' if torch.cuda.is_available() else 'cpu'

# Load the pretrained GPT-2 model and tokenizer from the saved directory
model_name = r'C:\Users\Suyash Tambe\Desktop\caption generator\gpt_model'
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name).to(device)

def generate_quote(tags, max_length=100, temperature=1.0, top_k=50, top_p=0.95):
    input_ids = tokenizer.encode(tags, return_tensors='pt').to(device)
    output = model.generate(
        input_ids,
        max_length=max_length,
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        pad_token_id=tokenizer.eos_token_id,
        temperature=temperature,
        top_k=top_k,
        top_p=top_p,
        do_sample=True,
        eos_token_id=tokenizer.eos_token_id,
    )
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    sentences = generated_text.split('.')
    if len(sentences) > 1:
        generated_text = sentences[0] + '.'
    return generated_text

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    tags = data['tags']
    quote = generate_quote(tags)
    return jsonify({'quote': quote})

if __name__ == '__main__':
    app.run(debug=True)