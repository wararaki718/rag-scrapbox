# Web UI (Vite + React + TypeScript)

This directory contains the user interface for the RAG Search system, built with Vite and React.

## Features

- **React + TypeScript**: Modern component-based architecture.
- **Vite**: Ultra-fast build tool and dev server.
- **Tailwind CSS**: Utility-first styling.
- **ESLint & Prettier**: Code linting and formatting.
- **Nginx Proxy**: In production (Docker), Nginx serves the static files and proxies `/api` requests to the search API.

## Execution

### Development
```bash
npm install
npm run dev
```

### Linting & Formatting
```bash
# Run linter
npm run lint

# Run formatter
npm run format
```

### Production (Docker)
Using the root `compose.yml` is recommended.

```bash
docker compose up -d
```

Access via: [http://localhost:3000](http://localhost:3000)
