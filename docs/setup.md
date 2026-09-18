# Local Setup

## Prerequisites

- Python 3.11 or newer
- Node.js and npm
- PostgreSQL 16 or newer, or Docker Desktop
- Docker Compose for PostgreSQL and Kafka services
- Git
- Java and Apache Spark only when running Spark jobs

## Frontend

```powershell
Copy-Item .env.example .env.local
cd frontend
npm install
npm run dev
```

Copy-Item backend/.env.example backend/.env
Open `http://localhost:5173`.

Production build:

```powershell
npm run build
```

## Backend

Copy-Item .env.example .env
From the repository root:

```powershell
python -m venv .venv
The root `.env` supplies Compose variables. The backend loads `backend/.env` through `python-dotenv`. The frontend `.env.local` supplies Vite variables and is intentionally not committed.
.\.venv\Scripts\Activate.ps1
`backend/.env.example` lists the supported environment variables. PowerShell variables override values from the backend `.env` file when both are present.
cd backend
python manage.py migrate
python manage.py runserver
```

The API runs at `http://localhost:8000/api/`.

## PostgreSQL and Kafka with Docker

From the repository root:

```powershell
docker compose up -d
docker compose ps
```

The development services expose PostgreSQL on `5432` and Kafka on `9092`.

Stop services:

```powershell
docker compose down
```

The database volume is persistent. To recreate it and reset local data, use `docker compose down -v` only when data loss is acceptable.

## Existing local PostgreSQL

If another PostgreSQL service already owns port `5432`, configure Django for that server:

```powershell
$env:POSTGRES_DB = "agrimarket"
$env:POSTGRES_USER = "agrimarket"
$env:POSTGRES_PASSWORD = "your-local-password"
$env:POSTGRES_HOST = "localhost"
$env:POSTGRES_PORT = "5432"
python manage.py runserver
```

The supported variables are listed in [backend/.env.example](../backend/.env.example). Django reads process environment variables; PowerShell variables must be set in the same terminal used to start Django.

## Sample utilities

Replay sample market events:

```powershell
python -m streaming.producers.replay_market_data
```

Run Python validation:

```powershell
python -m compileall backend data_engine ml streaming
```

## Troubleshooting

- **Password authentication failed:** the PostgreSQL role password does not match the environment variable. Update the role password or set `POSTGRES_PASSWORD` to the existing password.
- **Connection refused:** PostgreSQL is not running, Docker is stopped, or port `5432` is occupied by another service.
- **Frontend dependency missing:** run `npm install` inside `frontend`, not the repository root.
- **CORS error:** run the frontend on `http://localhost:5173`, which is allowed by the development settings.
