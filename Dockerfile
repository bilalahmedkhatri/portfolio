FROM python:3.8-buster-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /app
EXPOSE 8000
# RUN apt-get update \
# 	&& apt-get install -y --no-install-recommends \
# 		postgresql-client \
# 	&& rm -rf /var/lib/apt/lists/*
COPY requirements.txt /app
RUN pip3 install -r requirements.txt
COPY . /app
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]