# Docker Full-Stack Form

A Node.js/Express form frontend forwards registration data to a Flask API. Docker Compose builds both images and connects the services on a private bridge network.

## Run locally

Requirements: Docker Desktop with Docker Compose.

```powershell
docker compose up --build
```

Open [http://localhost:3000](http://localhost:3000), submit the registration form, and verify that Flask returns the processed name, email, course, and remarks. The Flask health check must pass before Compose starts the frontend.

Stop the services with `Ctrl+C`, then run:

```powershell
docker compose down
```

## Validate

```powershell
cd frontend
npm ci
npm test
cd ..\backend
python -m unittest
```

The backend tests use Flask's built-in test client and require the packages in `backend/requirements.txt`.

## Publish Docker images

The Compose file tags the images for Docker Hub user `sumanthgoud21`.

```powershell
docker login
docker compose build
docker compose push
```

## Publish source to GitHub

This project is being published to `https://github.com/sumanthgoud21/docker`. To push a fresh local copy:

```powershell
git init
git add .
git commit -m "Complete Docker full-stack form assignment"
git branch -M main
git remote add origin https://github.com/sumanthgoud21/docker.git
git push -u origin main
```

Do not add credentials, `.env` files, `node_modules`, Python bytecode, or IDE settings to the repository.
