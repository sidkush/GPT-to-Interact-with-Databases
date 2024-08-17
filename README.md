# SQL Query Generation with GPT Model

This project implements a system that generates SQL queries based on natural language prompts using a GPT model. It includes a custom GPT class, database integration, and a Gradio interface for user interaction.
                                    ![1_qCb8l9lQpD9gePSuFpbGdw](https://github.com/user-attachments/assets/7b362c30-1f42-4e2a-b414-8f6a36cf78f8)


## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Business Problem Statement](#business-problem-statement)
- [Methodology](#methodology)
- [Solution and Approach](#solution-and-approach)
- [Example Usage](#example-usage)

## Prerequisites

- Python 3.7+
- PostgreSQL database
- OpenAI API key

## Installation

1. Clone the repository: 
https://github.com/sidkush/GPT-to-Interact-with-Databases.git
cd sql-query-generation

2. Install required packages:
pip install openai, psycopg2, fastapi, gradio

3. Set up environment variables:
Create a `.env` file in the project root and add the following:
- API_KEY=your_openai_api_key
- DB_HOST=your_db_host
- DB_PORT=your_db_port
- DB_NAME=your_database_name
- DB_USER=your_db_user
- DB_PASSWORD=your_db_password
- TABLE_NAMES=table1,table2,table3

## Running the Application

1. Start the FastAPI server:
```code
uvicorn main:app --host 0.0.0.0 --port 8000
```

2. Run the Gradio interface:
```code
python gradio_ui.py
```

## Business Problem Statement

Many users, especially those without extensive SQL knowledge, struggle to generate accurate SQL queries for their data retrieval needs. This project aims to bridge the gap between natural language and SQL by providing an intuitive interface for users to input their questions in plain English and receive corresponding SQL queries.

## Methodology

The system employs the following methodology:

1. **GPT Model Integration**: Utilizes OpenAI's GPT model to understand natural language prompts and generate SQL queries.

2. **Database Context**: Incorporates database schema information to train the model on specific table structures.

3. **Example-based Learning**: Uses a custom GPT class to store and leverage examples for improved query generation.

4. **Query Execution**: Implements a database connection to execute generated queries and return results.

5. **User Interface**: Provides a Gradio interface for easy interaction with the system.

## Solution and Approach

The solution is implemented through the following components:

1. **Custom GPT Class** (`model.py`):
- Defines a `GPT` class to encapsulate the model's properties and methods.
- Implements methods for adding examples and submitting requests to the OpenAI API.
- Includes an `Example` class to store input-output pairs for training.

2. **Database Integration** (`db.py`):
- Creates a `DB_CONTEXT` class to handle database connections and query execution.
- Utilizes environment variables for secure database configuration.

3. **Model Training and Query Generation** (`model.py`):
- Implements a `model()` function to initialize and train the GPT model with database context.
- Uses the `train_from_db()` function to generate examples based on table structures.

4. **API and User Interface** (`main.py`):
- Sets up a FastAPI endpoint for query generation.
- Creates a Gradio interface for user-friendly interaction.

5. **Query Execution** (`main.py`):
- Implements the `execute_first_query()` function to run generated SQL queries and return results.

## Example Usage

1. User inputs a natural language question:
"What are the names of all employees in the Sales department?"

2. The system processes the input:
- The GPT model generates an SQL query based on the input and learned examples.
- The generated query might look like:
  ```sql
  SELECT name FROM employees WHERE department = 'Sales';
  ```

3. The query is executed in the connected database.

4. Results are returned to the user through the Gradio interface.

This approach allows users to interact with their database using natural language, making data retrieval more accessible to non-technical users while leveraging the power of AI for accurate SQL query generation.
