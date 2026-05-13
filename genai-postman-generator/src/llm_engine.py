from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_postman_tests(endpoint_data):
    prompt = f"""
You are an expert QA Automation Engineer.

Generate Postman Tests tab JavaScript for this API endpoint.

Endpoint details:
{endpoint_data}

Rules:
1. Generate only executable Postman JavaScript.
2. Include status code validation.
3. Validate important response fields if available.
4. Add negative test ideas as comments.
5. Store token/userId/tenantId into environment variables if found.
6. Do not add explanation.
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You generate Postman test scripts for API testing."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content
def generate_postman_tests(api_data):
    """
    Temporary placeholder function.
    Later this will call the LLM to generate Postman test scripts.
    """
    return {
        "tests": [
            {
                "name": "Verify status code is 200",
                "script": "pm.test('Status code is 200', function () { pm.response.to.have.status(200); });"
            }
        ]
    }
def generate_postman_test_script(api_data):
    return {
        "tests": [
            {
                "name": "Verify status code is 200",
                "script": "pm.test('Status code is 200', function () { pm.response.to.have.status(200); });"
            }
        ]
    }