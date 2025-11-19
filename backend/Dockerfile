
FROM python:3.9
WORKDIR /backend

COPY requirements.txt .
COPY ./app ./app

RUN pip install -r requirements.txt

ENV PYTHONPATH="/backend/app:${PYTHONPATH}"

ARG BACKEND_PORT
ENV BACKEND_PORT=$BACKEND_PORT

CMD ["sh", "-c", "python -m uvicorn main:app --host 0.0.0.0 --port ${BACKEND_PORT}"]