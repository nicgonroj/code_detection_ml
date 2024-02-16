# Deploy ML models with FastAPI, Docker, and Heroku

### 1. Develop and save the model

Random Forest CLF - Code Detection by Product Description.

### 2. Create Docker container

```bash
docker build -t code-detection .

docker run -p 80:80 code-detection
```

### 3. Create Git repo

```bash
git init
git add .
git commit -m ""
git branch -M main
```

### 4. Create Heroku project

```bash
heroku login
heroku create detection-heroku
heroku git:remote detection-heroku
heroku stack:set container
git push heroku main
```
# code_detection
# code_detection
