"""
A simple Azure Function (Python v2 programming model).

This is the AZURE FUNCTION part of the assignment. It is deployed to an
Azure Function App. It exposes one HTTP endpoint, /api/hello, that returns
a greeting. Anyone can call it (anonymous access).
"""

import azure.functions as func

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)


@app.route(route="hello")
def hello(req: func.HttpRequest) -> func.HttpResponse:
    name = req.params.get("name")
    if not name:
        try:
            body = req.get_json()
        except ValueError:
            body = None
        if body:
            name = body.get("name")

    if name:
        return func.HttpResponse(f"Hello, {name}! This greeting comes from an Azure Function.")

    return func.HttpResponse(
        "Hello! This Azure Function is running. Add ?name=YourName to the URL to personalize it."
    )
