FROM python:3.10-slim
ENV TOKEN='6418244705:AAFOVRyoorh6CWNv9WdGdm-dkc-lCwPVzio'
COPY . .
RUN pip install -r requirements.txt
CMD python bot.py