#docker run -p 12345:8000 -it ping_app

FROM python:3.9-buster

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /var/app

RUN pip install --upgrade pip "poetry==1.8.3"
RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./

RUN poetry install

COPY ./fastapi_ping ./

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

EXPOSE 8000