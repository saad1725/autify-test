
import torch
import transformers
from transformers import AutoTokenizer
model = "codellama/CodeLlama-7b-hf"

tokenizer = AutoTokenizer.from_pretrained(model)


def analyze_feedback(feedback_file):
    feedback_data = []
    feedback_entry = {}

    try:
        with open(feedback_file, 'r') as file:
            for line in file:
                line = line.strip()
                if line.startswith('User input:'):
                    feedback_entry['user_input'] = line.split(':', 1)[1].strip()
                elif line.startswith('Input prompt:'):
                    feedback_entry['input_prompt'] = line.split(':', 1)[1].strip()
                elif line.startswith('Generated code:'):
                    feedback_entry['generated_code'] = line.split(':', 1)[1].strip()
                elif line.startswith('Feedback'):
                    feedback_entry['Feedback'] = line.split(':', 1)[1].strip()
                    # Append the feedback entry to the list
                    feedback_data.append(feedback_entry)
                    # Reset the feedback entry dictionary for the next entry
                    feedback_entry = {}
                
    except FileNotFoundError:
        print(f"Error: File '{feedback_file}' not found.")
    except Exception as e:
        print(f"Error: {e}")

    return feedback_data



### Improving the model from feedback data

def fine_tune_model(feedback_data):
    # Process feedback data and prepare input-output pairs
    input_texts = [entry['user_input'] for entry in feedback_data]
    output_texts = [entry['generated_code'] for entry in feedback_data]

    # Tokenize input-output pairs
    input_encodings = tokenizer(input_texts, return_tensors='pt', padding=True, truncation=True)
    output_encodings = tokenizer(output_texts, return_tensors='pt', padding=True, truncation=True)

    # Fine-tune the model
    optimizer = torch.optim.AdamW(model.parameters(), lr=5e-5)
    for epoch in range(3):  # Example: Three epochs for fine-tuning
        for inputs, outputs in zip(input_encodings['input_ids'], output_encodings['input_ids']):
            outputs = outputs.unsqueeze(0)  # Add batch dimension
            optimizer.zero_grad()
            outputs = model(inputs.unsqueeze(0), labels=outputs)
            loss = outputs.loss
            loss.backward()
            optimizer.step()




if __name__ == "__main__":

    feedback_file = 'static/feedback.log'
    feedback_analysis = analyze_feedback(feedback_file)
    print(feedback_analysis)
    fine_tune_model(feedback_analysis)
    

