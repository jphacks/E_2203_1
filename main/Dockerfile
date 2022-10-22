FROM python

WORKDIR /app
COPY ./work/ /app/

RUN pip install Flask
RUN pip install pandas
RUN pip install mysql-connector-python

CMD ["python", "main.py"]