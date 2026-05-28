FROM python:3.11

WORKDIR /app

COPY .. /app

RUN pip install -r /app/API_Projects/DataTypeConversion_Operations/requirements.txt

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "API_Projects.DataTypeConversion_Operations.app:app"]