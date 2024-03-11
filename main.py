from fastapi import FastAPI, Form, Request

from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from transformers import AutoTokenizer, AutoModelForCausalLM
from transformers import AutoTokenizer
import transformers
import torch
from fastapi.staticfiles import StaticFiles
import os

from pathlib import Path
# Load the fine-tuned CodeLama model
model = "codellama/CodeLlama-7b-hf"

tokenizer = AutoTokenizer.from_pretrained(model)

app = FastAPI()

# Mount a static directory to serve static files like CSS and JavaScript
app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.absolute() / "static"),
    name="static",
)

# Define the path to the feedback log file
log_file = "static/feedback.log"



templates = Jinja2Templates(directory="templates")




# Function to generate code snippets based on user input
def generate_code(user_input):
    

    result=[]
    # Tokenize and encode the user input
    pipeline = transformers.pipeline(
        "text-generation",
        model=model,
        torch_dtype=torch.float16,
        device_map="auto",
    )

    sequences = pipeline(
        user_input,
        do_sample=True,
        top_k=10,
        temperature=0.1,
        top_p=0.95,
        num_return_sequences=1,
        eos_token_id=tokenizer.eos_token_id,
        max_length=1024,
    )
    for seq in sequences:
        
        result.append(seq['generated_text'])

    return " ".join(result)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    # print(templates.TemplateResponse("index.html", {"request": request}))
    return templates.TemplateResponse("index.html", {"request": request})



def save_to_file(data):
    with open(log_file, "a") as file:
        file.write(data + "\n")





@app.post("/feedback/")
async def save_feedback(feedback: str = Form(...)):
    # Save the feedback to the log file
    save_to_file(f"Feedback: {feedback}")
    return {"message": "Feedback saved successfully!"}





@app.post("/generate_code/")
async def generate_code_route(description: str = Form(...)):
    # Generate code snippet based on user input
    print(description)
    input_prompt="Generate a code snippet for " + str(description)    ##prompting the code to generate snippets only
    generated_code = generate_code(input_prompt)

    # Evaluate the generated code against constraints
    if validate_code_constraints(generated_code):
        # Save user input, input prompt, and generated code to the log file
        save_to_file(f"User input: {description}")
        save_to_file(f"Input prompt: {input_prompt}")
        save_to_file(f"Generated code: {generated_code}")

        return {"generated_code": generated_code}
    else:
        # Handle the case where the generated code does not meet the constraints
        return {"message": "Generated code does not meet constraints"}
    
def validate_code_constraints(code: str) -> bool:
    #we can add contraints based on the output of the LLM 
    #since i am not able to run the LLM on my machine i will not be able to write an example test here.
    #the pseudo code can be something like this: user can input the output data type or output format and this function will run the code and match the outputs and return a boolean

     return True



if __name__ == "__main__":
    if not os.path.exists(log_file):
        with open(log_file, "w") as file:
            pass
    # import uvicorn
    # uvicorn.run(app, host="127.0.0.1", port=8000)