# Finder

## Installation
1. [Install Docker](https://docs.docker.com/desktop/)
1. `git clone https://github.com/CS-338-Project-4/finder`
1. `cd finder`
1. `docker compose up`
1. App should be running at http://localhost:8000

## Testing
Run all tests
`docker exec -t finder-backend-1 pytest`
Run unit tests
`docker exec -t finder-backend-1 pytest test_unit.py`
Run acceptance tests
`docker exec -t finder-backend-1 pytest test_acceptance.py`

## Other Helpful Commands
See running docker containers
`docker ps`
Run docker container in background
`docker compose up -d`
Run docker container and rebuild image
`docker compose up --build`
Stop and remove docker containers
`docker compose down`
Open interactive shell in running backend container
`docker exec -it finder-backend-1 bash`

## Contributors
- Archit Chopra
- Darryl Forbes
- Riya Singh
- Bill Wang
