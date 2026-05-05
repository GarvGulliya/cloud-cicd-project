from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CI/CD Deployment Pipeline — Garv Gulliya</title>
    <link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">
    <style>
        *, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }

        :root {
            --cream: #FAF8F4;
            --white: #FFFFFF;
            --ink: #1A1A2E;
            --ink-light: #4A4A6A;
            --accent: #2D6A4F;
            --accent-light: #52B788;
            --accent-pale: #D8F3DC;
            --border: #E8E4DC;
            --shadow: rgba(26, 26, 46, 0.08);
        }

        body {
            font-family: 'DM Sans', sans-serif;
            background: var(--cream);
            color: var(--ink);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
        }

        /* TOP NAV */
        nav {
            background: var(--white);
            border-bottom: 1px solid var(--border);
            padding: 0 48px;
            height: 64px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            position: sticky;
            top: 0;
            z-index: 100;
            box-shadow: 0 1px 12px var(--shadow);
        }

        .nav-brand {
            font-family: 'DM Serif Display', serif;
            font-size: 20px;
            color: var(--ink);
            letter-spacing: -0.3px;
        }

        .nav-brand span {
            color: var(--accent);
        }

        .nav-status {
            display: flex;
            align-items: center;
            gap: 8px;
            background: var(--accent-pale);
            border: 1px solid var(--accent-light);
            padding: 6px 14px;
            border-radius: 100px;
            font-size: 13px;
            font-weight: 500;
            color: var(--accent);
        }

        .status-dot {
            width: 7px;
            height: 7px;
            background: var(--accent);
            border-radius: 50%;
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0%, 100% { opacity: 1; transform: scale(1); }
            50% { opacity: 0.5; transform: scale(0.85); }
        }

        /* HERO */
        .hero {
            max-width: 900px;
            margin: 80px auto 0;
            padding: 0 32px;
            text-align: center;
            animation: fadeUp 0.7s ease both;
        }

        @keyframes fadeUp {
            from { opacity: 0; transform: translateY(24px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .hero-tag {
            display: inline-block;
            background: var(--accent-pale);
            color: var(--accent);
            font-size: 12px;
            font-weight: 600;
            letter-spacing: 1.5px;
            text-transform: uppercase;
            padding: 6px 16px;
            border-radius: 100px;
            margin-bottom: 28px;
            border: 1px solid var(--accent-light);
        }

        .hero h1 {
            font-family: 'DM Serif Display', serif;
            font-size: clamp(36px, 6vw, 64px);
            line-height: 1.1;
            color: var(--ink);
            letter-spacing: -1.5px;
            margin-bottom: 20px;
        }

        .hero h1 em {
            font-style: italic;
            color: var(--accent);
        }

        .hero p {
            font-size: 18px;
            color: var(--ink-light);
            font-weight: 300;
            line-height: 1.7;
            max-width: 560px;
            margin: 0 auto 48px;
        }

        /* STATS ROW */
        .stats {
            display: flex;
            justify-content: center;
            gap: 0;
            max-width: 700px;
            margin: 0 auto 80px;
            background: var(--white);
            border: 1px solid var(--border);
            border-radius: 16px;
            overflow: hidden;
            box-shadow: 0 4px 24px var(--shadow);
            animation: fadeUp 0.7s 0.15s ease both;
        }

        .stat {
            flex: 1;
            padding: 28px 24px;
            text-align: center;
            border-right: 1px solid var(--border);
            transition: background 0.2s;
        }

        .stat:last-child { border-right: none; }
        .stat:hover { background: var(--cream); }

        .stat-value {
            font-family: 'DM Serif Display', serif;
            font-size: 32px;
            color: var(--accent);
            line-height: 1;
            margin-bottom: 6px;
        }

        .stat-label {
            font-size: 12px;
            color: var(--ink-light);
            font-weight: 500;
            letter-spacing: 0.5px;
            text-transform: uppercase;
        }

        /* PIPELINE SECTION */
        .section {
            max-width: 900px;
            margin: 0 auto 64px;
            padding: 0 32px;
            animation: fadeUp 0.7s 0.25s ease both;
        }

        .section-label {
            font-size: 11px;
            font-weight: 600;
            letter-spacing: 2px;
            text-transform: uppercase;
            color: var(--ink-light);
            margin-bottom: 20px;
        }

        /* PIPELINE STEPS */
        .pipeline {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 16px;
        }

        .pipeline-step {
            background: var(--white);
            border: 1px solid var(--border);
            border-radius: 14px;
            padding: 24px 20px;
            position: relative;
            transition: transform 0.2s, box-shadow 0.2s;
        }

        .pipeline-step:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 32px var(--shadow);
        }

        .step-number {
            font-size: 11px;
            font-weight: 600;
            color: var(--accent-light);
            letter-spacing: 1px;
            text-transform: uppercase;
            margin-bottom: 10px;
        }

        .step-icon {
            font-size: 28px;
            margin-bottom: 12px;
            display: block;
        }

        .step-title {
            font-size: 15px;
            font-weight: 600;
            color: var(--ink);
            margin-bottom: 6px;
        }

        .step-desc {
            font-size: 13px;
            color: var(--ink-light);
            line-height: 1.5;
        }

        .step-arrow {
            position: absolute;
            right: -22px;
            top: 50%;
            transform: translateY(-50%);
            color: var(--accent-light);
            font-size: 18px;
            z-index: 1;
        }

        .pipeline-step:last-child .step-arrow { display: none; }

        /* TECH STACK */
        .stack-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 14px;
        }

        .stack-card {
            background: var(--white);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 20px;
            display: flex;
            align-items: center;
            gap: 14px;
            transition: transform 0.2s, box-shadow 0.2s;
        }

        .stack-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px var(--shadow);
        }

        .stack-icon {
            font-size: 26px;
            width: 44px;
            height: 44px;
            background: var(--cream);
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
        }

        .stack-name {
            font-size: 14px;
            font-weight: 600;
            color: var(--ink);
        }

        .stack-role {
            font-size: 12px;
            color: var(--ink-light);
            margin-top: 2px;
        }

        /* INFO CARDS */
        .info-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 16px;
        }

        .info-card {
            background: var(--white);
            border: 1px solid var(--border);
            border-radius: 14px;
            padding: 28px;
        }

        .info-card h3 {
            font-family: 'DM Serif Display', serif;
            font-size: 20px;
            color: var(--ink);
            margin-bottom: 16px;
        }

        .info-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px 0;
            border-bottom: 1px solid var(--border);
            font-size: 14px;
        }

        .info-row:last-child { border-bottom: none; }

        .info-row-key {
            color: var(--ink-light);
            font-weight: 400;
        }

        .info-row-val {
            color: var(--ink);
            font-weight: 600;
            font-family: 'DM Serif Display', serif;
            font-size: 15px;
        }

        .badge-green {
            background: var(--accent-pale);
            color: var(--accent);
            padding: 3px 10px;
            border-radius: 100px;
            font-size: 12px;
            font-weight: 600;
            font-family: 'DM Sans', sans-serif;
        }

        /* FOOTER */
        footer {
            margin-top: auto;
            background: var(--white);
            border-top: 1px solid var(--border);
            padding: 24px 48px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 13px;
            color: var(--ink-light);
        }

        footer strong { color: var(--ink); }

        footer a {
            color: var(--accent);
            text-decoration: none;
            font-weight: 500;
        }

        footer a:hover { text-decoration: underline; }
    </style>
</head>
<body>

    <nav>
        <div class="nav-brand">Cloud<span>Pipeline</span></div>
        <div class="nav-status">
            <div class="status-dot"></div>
            Production · Live
        </div>
    </nav>

    <div class="hero">
        <div class="hero-tag">Cloud-Native CI/CD · 2026</div>
        <h1>Containerized <em>Production</em><br>Deployment Pipeline</h1>
        <p>A fully automated CI/CD system that deploys code from Git commit to live server in under 60 seconds — with zero manual steps.</p>
    </div>

    <div class="stats">
        <div class="stat">
            <div class="stat-value">48s</div>
            <div class="stat-label">Avg Deploy Time</div>
        </div>
        <div class="stat">
            <div class="stat-value">6</div>
            <div class="stat-label">Total Deployments</div>
        </div>
        <div class="stat">
            <div class="stat-value">100%</div>
            <div class="stat-label">Pipeline Uptime</div>
        </div>
        <div class="stat">
            <div class="stat-value">0</div>
            <div class="stat-label">Manual Steps</div>
        </div>
    </div>

    <div class="section">
        <div class="section-label">Deployment Pipeline</div>
        <div class="pipeline">
            <div class="pipeline-step">
                <div class="step-number">Step 01</div>
                <span class="step-icon">✏️</span>
                <div class="step-title">Code Push</div>
                <div class="step-desc">Developer pushes to GitHub main branch</div>
                <div class="step-arrow">→</div>
            </div>
            <div class="pipeline-step">
                <div class="step-number">Step 02</div>
                <span class="step-icon">⚙️</span>
                <div class="step-title">GitHub Actions</div>
                <div class="step-desc">Pipeline triggers, Docker image is built</div>
                <div class="step-arrow">→</div>
            </div>
            <div class="pipeline-step">
                <div class="step-number">Step 03</div>
                <span class="step-icon">🔐</span>
                <div class="step-title">SSH Deploy</div>
                <div class="step-desc">Actions SSHs into Oracle Cloud VM securely</div>
                <div class="step-arrow">→</div>
            </div>
            <div class="pipeline-step">
                <div class="step-number">Step 04</div>
                <span class="step-icon">🌐</span>
                <div class="step-title">Live on Nginx</div>
                <div class="step-desc">New container runs, Nginx serves to the world</div>
            </div>
        </div>
    </div>

    <div class="section">
        <div class="section-label">Technology Stack</div>
        <div class="stack-grid">
            <div class="stack-card">
                <div class="stack-icon">🐍</div>
                <div>
                    <div class="stack-name">Flask (Python)</div>
                    <div class="stack-role">Web application framework</div>
                </div>
            </div>
            <div class="stack-card">
                <div class="stack-icon">🐳</div>
                <div>
                    <div class="stack-name">Docker</div>
                    <div class="stack-role">Containerization engine</div>
                </div>
            </div>
            <div class="stack-card">
                <div class="stack-icon">⚡</div>
                <div>
                    <div class="stack-name">GitHub Actions</div>
                    <div class="stack-role">CI/CD automation pipeline</div>
                </div>
            </div>
            <div class="stack-card">
                <div class="stack-icon">☁️</div>
                <div>
                    <div class="stack-name">Oracle Cloud</div>
                    <div class="stack-role">Cloud VM infrastructure</div>
                </div>
            </div>
            <div class="stack-card">
                <div class="stack-icon">🔄</div>
                <div>
                    <div class="stack-name">Nginx</div>
                    <div class="stack-role">Reverse proxy &amp; web server</div>
                </div>
            </div>
            <div class="stack-card">
                <div class="stack-icon">🔑</div>
                <div>
                    <div class="stack-name">SSH Auth</div>
                    <div class="stack-role">Secure credential management</div>
                </div>
            </div>
        </div>
    </div>

    <div class="section">
        <div class="section-label">Project Details</div>
        <div class="info-grid">
            <div class="info-card">
                <h3>Deployment Info</h3>
                <div class="info-row">
                    <span class="info-row-key">Status</span>
                    <span class="badge-green">● Live &amp; Running</span>
                </div>
                <div class="info-row">
                    <span class="info-row-key">Server</span>
                    <span class="info-row-val">Oracle Cloud (Mumbai)</span>
                </div>
                <div class="info-row">
                    <span class="info-row-key">Public IP</span>
                    <span class="info-row-val">140.245.12.192</span>
                </div>
                <div class="info-row">
                    <span class="info-row-key">OS</span>
                    <span class="info-row-val">Ubuntu 22.04 LTS</span>
                </div>
                <div class="info-row">
                    <span class="info-row-key">Container</span>
                    <span class="info-row-val">Docker + Flask</span>
                </div>
            </div>
            <div class="info-card">
                <h3>Team &amp; Project</h3>
                <div class="info-row">
                    <span class="info-row-key">Developer</span>
                    <span class="info-row-val">Garv Gulliya</span>
                </div>
                <div class="info-row">
                    <span class="info-row-key">Roll No.</span>
                    <span class="info-row-val">26511</span>
                </div>
                <div class="info-row">
                    <span class="info-row-key">Developer</span>
                    <span class="info-row-val">Mayank Sharma</span>
                </div>
                <div class="info-row">
                    <span class="info-row-key">Roll No.</span>
                    <span class="info-row-val">26931</span>
                </div>
                <div class="info-row">
                    <span class="info-row-key">Guide</span>
                    <span class="info-row-val">Mr. Ashwini (HOD)</span>
                </div>
            </div>
        </div>
    </div>

    <footer>
        <div>Built by <strong>Garv Gulliya</strong> &amp; <strong>Mayank Sharma</strong> · 2026</div>
        <div>
            <a href="https://github.com/GarvGulliya/cloud-cicd-project" target="_blank">GitHub Repo</a>
            &nbsp;·&nbsp;
            <a href="https://github.com/GarvGulliya/cloud-cicd-project/actions" target="_blank">Pipeline Logs</a>
        </div>
    </footer>

</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML)

@app.route('/health')
def health():
    return {"status": "healthy", "message": "Pipeline running"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)