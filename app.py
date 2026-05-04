from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Cloud CI/CD Project</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #0d1117;
            color: #c9d1d9;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .box {
            text-align: center;
            border: 1px solid #30363d;
            padding: 40px 60px;
            border-radius: 12px;
            background: #161b22;
        }
        h1 { color: #58a6ff; }
        p { color: #8b949e; }
        .badge {
            background: #238636;
            color: white;
            padding: 6px 14px;
            border-radius: 20px;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <div class="box">
        <h1>🚀 Cloud-Native CI/CD</h1>
        <p>Containerized Deployment Pipeline</p>
        <p>Built by: <strong>Garv Gulliya</strong></p>
        <br>
        <span class="badge">Hello World</span>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML)

@app.route('/health')
def health():
    return {"status": "healthy", "message": "Pipeline working"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)