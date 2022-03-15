# Finder

## Installation
1. [Install Docker](https://docs.docker.com/desktop/)
1. `git clone https://github.com/CS-338-Project-4/finder`
1. `cd finder`
1. `docker compose up`
1. App should be running at http://localhost:8000

## Testing
| Command | Description |
| --- | --- |
| `docker exec -t finder-backend-1 pytest` | Run all tests |
| `docker exec -t finder-backend-1 pytest test_acceptance.py` | Run acceptance tests |

## Other Helpful Commands
| Command | Description |
| --- | --- |
| `docker ps` | See running docker containers |
| `docker compose up -d` | Run docker container in background |
| `docker compose up --build` | Run docker container and rebuild image |
| `docker compose down` | Stop and remove docker containers
| `docker exec -it finder-backend-1 bash` | Open interactive shell in running backend container |

## Contributors
- Archit Chopra
- Darryl Forbes
- Riya Singh
- Bill Wang
