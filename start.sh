services:
  - type: web
    name: jwt-login-service
    env: python
    plan: free
    buildCommand: "pip install -r requirements.txt"
    startCommand: "./start.sh"
    envVars:
      - key: DATABASE_URL
        value: sqlite:///./jwt_users.db
