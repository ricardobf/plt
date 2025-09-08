FROM python:3.13-slim

WORKDIR /app

COPY pyproject.toml setup.cfg setup.py requirements.txt ./
RUN pip install --no-cache-dir -e .

COPY src/ ./src/

ENTRYPOINT ["python", "-m", "plt"]
CMD []
