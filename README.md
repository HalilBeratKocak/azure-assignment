# Azure Cloud Deployment Assignment

A small project that demonstrates deploying two services to Microsoft Azure,
with the web app deployed automatically from GitHub using a GitHub Actions pipeline.

## What the application does

The project has two independent parts:

1. **Web App** (`app.py`) — a Python (Flask) website hosted on **Azure App Service**.
   It serves a single page describing the project. It is connected to this GitHub
   repository and deployed automatically via **GitHub Actions** on every push to `main`.

2. **Azure Function** (`functionapp/`) — a serverless, HTTP-triggered function
   (Node.js) hosted on an **Azure Function App**. It exposes one endpoint, `hello`,
   which returns a greeting (optionally personalized with a `?name=` parameter).

## Project structure

```
azure-assignment/
├── app.py              # Flask web app  -> Azure App Service (Web App)
├── requirements.txt    # Web app dependencies (Flask, gunicorn)
├── functionapp/        # Azure Function -> Azure Function App (Node.js)
│   ├── host.json
│   ├── package.json
│   └── hello/
│       ├── function.json
│       └── index.js
└── README.md
```

## Run the web app locally (optional)

```bash
pip install -r requirements.txt
python app.py
```

Then open http://localhost:8000 in a browser.
