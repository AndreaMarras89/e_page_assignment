FROM python:3.11.7-slim

WORKDIR /app
COPY ./requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .
EXPOSE 8088
CMD ["python", "-m", "be_ecommerce"]