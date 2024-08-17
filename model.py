# Create a Python class to reflect your GPT model

import openai

#class definition of custom GPT stucture to store examples
class GPT:
    def __init__(self, engine, temperature, max_tokens):
        self.engine = engine
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.examples = []

    #add examples into the GPT structure to give more context to the model
    def add_example(self, example):
        self.examples.append(example)
        
    #get the response from the openai api
    def submit_request(self, prompt):
        prompt_with_examples = self._build_prompt_with_examples(prompt)

        response = openai.Completion.create(
            engine=self.engine,
            prompt=prompt_with_examples,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            n=1,
            stop=None,
            echo=False,
        )

        return response

    def _build_prompt_with_examples(self, prompt):
        prompt_with_examples = ""
        for example in self.examples:
            prompt_with_examples += f"Q: {example.input}\nA: {example.output}\n"
        prompt_with_examples += f"Q: {prompt}\n"

        return prompt_with_examples

#data structure to store the input and output of the examples
class Example:
    def __init__(self, input, output):
        self.input = input
        self.output = output


# create a Python script to instantiate the GPT model, load it with pre-trained weights, and add examples for training
#method to initialize the model

def model(dbContext):
    openai.api_key = os.getenv("API_KEY")
    #davinci
    gpt = GPT(engine="text-davinci-003",
            temperature=0.5,
            max_tokens=100)
    # Read the table names from the .env file
    table_names_str = os.getenv("TABLE_NAMES")

    # Split the table names into a list
    table_names = table_names_str.split(',')

    # Train the model with each table
    for table_name in table_names:
        gpt = train_from_db(gpt, dbContext, table_name.strip())

    return gpt

def train_from_db(gpt, db_context, table_name):
    cursor = db_context.connection.cursor()
    cursor.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table_name}';")
    columns = cursor.fetchall()

    example_prompt = f"Fetch all columns from the {table_name} table."
    example_query = f"SELECT * FROM {table_name};"
    gpt.add_example(Example(example_prompt, example_query))

    for column in columns:
        column_name = column[0]
        example_prompt = f"Fetch the {column_name} column from the {table_name} table."
        example_query = f"SELECT {column_name} FROM {table_name};"
        gpt.add_example(Example(example_prompt, example_query))
    return gpt

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Prompt(BaseModel):
    text: str

@app.post("/generate_sql_query/")
async def generate_sql_query(prompt: Prompt):
    sql_query = get_predicted_query(gpt, prompt.text)
    return {"query": sql_query}