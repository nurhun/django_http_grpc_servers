FROM python:3.7

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
RUN python manage.py migrate

# RUN python manage.py makemigrations
# RUN python manage.py migrate

EXPOSE 8000
EXPOSE 50051

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# CMD ["python", "manage.py", "grpcrunserver", "0.0.0.0:50051"]

##### Run HTTP & gRPC Servers #####
CMD ["python", "manage.py", "runboth"]