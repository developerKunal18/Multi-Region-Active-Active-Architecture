# Multi-Region Active-Active Architecture

A learning project demonstrating a multi-region active-active Flask architecture.

## Features

- Multiple application regions
- NGINX traffic distribution
- Regional health endpoints
- Docker-based deployment
- Failure simulation

## Technologies

- Python
- Flask
- NGINX
- Docker

## Architecture

```text
             Global Gateway
                /      \
               /        \
          Region A    Region B
             │           │
           Flask       Flask
```

## Run

```bash
docker compose up --build
```

Open:

```text
http://localhost:8080
```

## Purpose

Day 298 introduces multi-region active-active architecture and the challenges of distributed availability, data consistency, and failover.
