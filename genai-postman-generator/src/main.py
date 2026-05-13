from parser import parse_swagger_file
from llm_engine import generate_postman_test_script

swagger_file_path = "input/swagger.json"

# Parse swagger
endpoints = parse_swagger_file(swagger_file_path)

# Generate tests for each endpoint
for endpoint in endpoints:

    print("\n====================================")
    print(f"Generating tests for: {endpoint['path']}")
    print("====================================\n")

    generated_script = generate_postman_test_script(endpoint)

    print(generated_script)