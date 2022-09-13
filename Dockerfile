# build stage
FROM python:3.10-alpine 

WORKDIR /app 

# install pdm 
RUN pip install pdm

# copy pyproject.toml 
COPY pyproject.toml .
COPY pdm.lock .

# install dependencies
RUN pdm install --prod --no-lock

# copy project
COPY . .

ENTRYPOINT [ "pdm", "run", "start" ]
