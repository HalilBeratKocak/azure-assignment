# Azure Cloud Deployment Assignment

A small Python project that demonstrates deploying two services to Microsoft Azure
straight from GitHub, using an automated GitHub Actions pipeline.

## What the application does

The project has two independent parts:

1. **Web App** (`app.py`) — a Flask website hosted on **Azure App Service**.
   It serves a single page describing the project. This is the "Web App" you will
   see in the Azure portal.

2. **Azure Function** (`functionapp/`) — a serverless HTTP function hosted on an
   **Azure Function App**. It exposes one endpoint, `/api/hello`, which returns a
   greeting (optionally personalized with a `?name=` parameter).

Both services are deployed automatically: whenever code is pushed to the `main`
branch on GitHub, a **GitHub Actions** workflow builds and publishes it to Azure.

## Project structure

```
azure-assignment/
├── app.py              # Flask web app  -> Azure App Service (Web App)
├── requirements.txt    # Web app dependencies (Flask, gunicorn)
├── functionapp/        # Azure Function -> Azure Function App
│   ├── function_app.py
│   ├── host.json
│   └── requirements.txt
└── README.md
```

## Run the web app locally (optional)

```bash
pip install -r requirements.txt
python app.py
```

Then open http://localhost:8000 in a browser.
