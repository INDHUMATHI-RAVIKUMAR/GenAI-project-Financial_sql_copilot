import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_sql(question):

    prompt = f"""
You are a financial data analyst.

Convert the user's question into a SQLite SQL query.

Database table:

financial_data

Columns:

id
year
quarter
department
revenue
expenses
profit

Rules:
- Return ONLY SQL.
- Do not use markdown.
- Do not modify the database.
- Only use SELECT queries.
- Do not use INSERT, UPDATE, DELETE, DROP, ALTER or CREATE.
- Use SQLite syntax.

User question:
{question}
"""

    response = client.responses.create(
        model="gpt-5",
        input=prompt
    )

    return response.output_text.strip()