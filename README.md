# MCP Tools Server

Production-ready **Model Context Protocol (MCP)** server with 5 built-in tools.

## Tools Available
| Tool | Description |
|------|-------------|
| Weather | Real-time weather via OpenWeatherMap |
| Search | Web search via Tavily + SerpAPI |
| Code Exec | Sandboxed Python/JS execution |
| Browser | Playwright-based web automation |
| Database | PostgreSQL/SQLite query tool |

## Stack
Python 3.12 · FastAPI · MCP SDK 1.0 · Playwright · asyncpg · Docker

## Quick Start
```bash
git clone https://github.com/b24repo/mcp-tools-server
cd mcp-tools-server
pip install -r requirements.txt
cp .env.example .env
python server.py
```

## GitHub
github.com/b24repo/mcp-tools-server