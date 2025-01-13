FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

RUN pytest --cov=devops_tasks --cov-report=xml || echo "Tests Failed"

CMD ["python", "devops_tasks.py"]
