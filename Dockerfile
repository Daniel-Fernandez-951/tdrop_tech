FROM tiangolo/uvicorn-gunicorn:python3.9


RUN apt-get update && apt-get install -y git
# Get project specific requirements and copy files
COPY . /app/
RUN rm -rf .git .idea venv .gitignore images
RUN pip install -r requirements.txt




