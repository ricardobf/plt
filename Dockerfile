FROM python:3.13-slim

WORKDIR /app

COPY pyproject.toml requirements.txt ./
RUN pip install --no-cache-dir -e .

ENV PYTHONPATH=/app/src

COPY src/ ./src/

ENTRYPOINT ["python", "-m", "plt"]
CMD []
