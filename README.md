# DevOps CI/CD Pipeline
Simple Flask application with a CI pipeline using GitHub Actions.

Tools
- Python
- Docker
- GitHub Actions
- Linux

Pipeline Steps
1. Code push to GitHub
2. Install dependencies
3. Run tests automatically

Run Locally
```bash
docker build -t ci-app .
docker run -p 5000:5000 ci-app
