FROM python:3.8-slim
WORKDIR /usr/mail-dashboard
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8181
CMD ["uvicorn", "main:app", "--reload"]
