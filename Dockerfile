FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src

EXPOSE 8501

CMD [ "streamlit", "run", "src/app.py"]
