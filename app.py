"""
A simple Flask web application.

This is the WEB APP part of the assignment. It is deployed to Azure App Service
(a "Web App"). It serves one page that explains what the project does and links
to the Azure Function.
"""

from flask import Flask, render_template_string

app = Flask(__name__)

PAGE = """<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Azure Assignment - Web App</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f4f8fb; color: #222;
               max-width: 640px; margin: 60px auto; padding: 0 20px; line-height: 1.6; }
        h1 { color: #1f4e79; }
        .card { background: #fff; border: 1px solid #d7e3ee; border-radius: 10px;
                padding: 24px 28px; box-shadow: 0 2px 8px rgba(0,0,0,.05); }
        code { background: #eef3f8; padding: 2px 6px; border-radius: 4px; }
        .tag { display: inline-block; background: #2e75b6; color: #fff;
               font-size: 13px; padding: 3px 10px; border-radius: 20px; }
    </style>
</head>
<body>
    <div class="card">
        <span class="tag">Azure Web App</span>
        <h1>Cloud Deployment Demo</h1>
        <p>This web application is hosted on <strong>Azure App Service</strong> and was
        deployed automatically from GitHub using a <strong>GitHub Actions</strong> pipeline.</p>
        <p>The project also includes an <strong>Azure Function</strong> that returns a
        greeting message over HTTP. Together they demonstrate a basic cloud deployment
        workflow: code in GitHub, automated deployment, and two running Azure services.</p>
        <p>Try the function endpoint by visiting its URL with a name, for example:
        <code>/api/hello?name=Furkan</code></p>
    </div>
</body>
</html>"""


@app.route("/")
def home():
    return render_template_string(PAGE)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
