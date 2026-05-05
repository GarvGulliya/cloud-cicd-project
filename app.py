from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Garv Gulliya — CI/CD Project</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap');
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      background: #0a0a0a;
      color: #00ff41;
      font-family: 'Share Tech Mono', monospace;
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }
    .container { max-width: 780px; width: 100%; }
    .terminal {
      border: 1px solid #00ff41;
      border-radius: 6px;
      overflow: hidden;
      box-shadow: 0 0 40px rgba(0,255,65,0.15);
    }
    .terminal-bar {
      background: #1a1a1a;
      padding: 10px 16px;
      display: flex;
      align-items: center;
      gap: 8px;
      border-bottom: 1px solid #00ff4133;
    }
    .dot { width: 12px; height: 12px; border-radius: 50%; }
    .dot.red { background: #ff5f57; }
    .dot.yellow { background: #febc2e; }
    .dot.green { background: #28c840; }
    .terminal-title { color: #555; font-size: 13px; margin-left: auto; margin-right: auto; }
    .terminal-body { padding: 32px; background: #0d0d0d; }
    .prompt { color: #555; }
    .cmd { color: #00ff41; }
    .output { color: #00cc33; margin: 4px 0 4px 0; }
    .line { margin: 6px 0; font-size: 15px; display: flex; gap: 10px; }
    .section-gap { margin-top: 28px; }
    .label { color: #555; min-width: 160px; }
    .value { color: #00ff41; }
    .value.bright { color: #ffffff; }
    .value.dim { color: #009922; }
    .badge {
      display: inline-block;
      background: #00ff4122;
      border: 1px solid #00ff41;
      color: #00ff41;
      padding: 2px 10px;
      border-radius: 3px;
      font-size: 13px;
    }
    .badge.success { background: #00ff4122; border-color: #00ff41; color: #00ff41; }
    .divider { border: none; border-top: 1px solid #1a1a1a; margin: 24px 0; }
    .stack-grid { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 6px; }
    .tag {
      background: #111;
      border: 1px solid #00ff4155;
      color: #00cc33;
      padding: 4px 12px;
      border-radius: 3px;
      font-size: 13px;
    }
    .blink { animation: blink 1s step-end infinite; }
    @keyframes blink { 50% { opacity: 0; } }
    a { color: #00ff41; text-decoration: none; }
    a:hover { text-decoration: underline; }
    .cursor { display: inline-block; width: 10px; height: 16px; background: #00ff41; vertical-align: middle; }
  </style>
</head>
<body>
<div class="container">
  <div class="terminal">
    <div class="terminal-bar">
      <div class="dot red"></div>
      <div class="dot yellow"></div>
      <div class="dot green"></div>
      <span class="terminal-title">garv@oracle-cloud: ~/cloud-cicd-project</span>
    </div>
    <div class="terminal-body">

      <div class="line"><span class="prompt">$</span><span class="cmd"> whoami</span></div>
      <div class="line output">&nbsp;&nbsp;Garv Gulliya</div>

      <div class="line section-gap"><span class="prompt">$</span><span class="cmd"> cat project.info</span></div>
      <div class="line"><span class="label">&nbsp;&nbsp;Project</span><span class="value bright">Containerized CI/CD Production Deployment</span></div>
      <div class="line"><span class="label">&nbsp;&nbsp;Status</span><span class="badge success">&#x25CF; LIVE &amp; DEPLOYED</span></div>
      <div class="line"><span class="label">&nbsp;&nbsp;Server</span><span class="value">Oracle Cloud Infrastructure (OCI)</span></div>
      <div class="line"><span class="label">&nbsp;&nbsp;Public IP</span><span class="value">140.245.12.192</span></div>
      <div class="line"><span class="label">&nbsp;&nbsp;GitHub</span><a href="https://github.com/GarvGulliya/cloud-cicd-project" target="_blank">github.com/GarvGulliya/cloud-cicd-project</a></div>

      <hr class="divider">

      <div class="line"><span class="prompt">$</span><span class="cmd"> docker ps</span></div>
      <div class="line output">&nbsp;&nbsp;CONTAINER ID &nbsp;&nbsp;IMAGE &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;STATUS &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PORTS</div>
      <div class="line output">&nbsp;&nbsp;a3f92c1d8e04 &nbsp;&nbsp;web_app:latest &nbsp;&nbsp;Up (healthy) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0.0.0.0:5000->5000/tcp</div>

      <hr class="divider">

      <div class="line"><span class="prompt">$</span><span class="cmd"> cat stack.yml</span></div>
      <div class="stack-grid" style="margin-left:16px; margin-top:10px;">
        <span class="tag">&#x1F433; Docker</span>
        <span class="tag">&#x2699;&#xFE0F; GitHub Actions</span>
        <span class="tag">&#x1F40D; Flask (Python)</span>
        <span class="tag">&#x1F310; Nginx</span>
        <span class="tag">&#x2601;&#xFE0F; Oracle Cloud</span>
        <span class="tag">&#x1F511; SSH Auth</span>
      </div>

      <hr class="divider">

      <div class="line"><span class="prompt">$</span><span class="cmd"> git log --oneline -3</span></div>
      <div class="line output">&nbsp;&nbsp;ff901d7 &nbsp;Version 2 update</div>
      <div class="line output">&nbsp;&nbsp;ad6bff9 &nbsp;Fix SSH key</div>
      <div class="line output">&nbsp;&nbsp;2691643 &nbsp;Initial project setup</div>

      <div class="line section-gap">
        <span class="prompt">$</span>
        <span class="cmd"> _</span>
        <span class="cursor blink"></span>
      </div>

    </div>
  </div>
</div>
</body>
</html>'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)