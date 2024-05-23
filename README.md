# api-resume-reviewer
API for reviewing resumes via gen ai

## running through docker
1. Make sure you have the docker daemon running
2. run `docker compose up --build`

## deployed to fly.io
1. `fly deploy` - currently in person account <jjustin634@gmail.com>

## type annotation check
1. `mypy .`

## code linting, formatting, and sorting imports
1. `ruff .`
    - For sorting then use `ruff . --fix`
2. `ruff format`

