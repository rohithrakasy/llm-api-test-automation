import json


def parse_swagger_file(file_path):

    with open(file_path, "r") as file:
        swagger_data = json.load(file)

    endpoints = []

    paths = swagger_data.get("paths", {})

    for path, methods in paths.items():

        for method, details in methods.items():

            endpoint = {
                "path": path,
                "method": method.upper(),
                "summary": details.get("summary", ""),
                "requestBody": {},
                "responses": {}
            }

            # Request body example
            request_body = details.get("requestBody", {})

            content = request_body.get("content", {})

            app_json = content.get("application/json", {})

            example = app_json.get("example", {})

            endpoint["requestBody"] = example

            # Responses
            responses = details.get("responses", {})

            for status_code, response_details in responses.items():

                endpoint["responses"][status_code] = {
                    "description": response_details.get("description", "")
                }

            endpoints.append(endpoint)

    return endpoints