FROM python

WORKDIR /app
#COPY ./work/ /app/

RUN pip install Flask
RUN pip install pandas
RUN pip install sqlalchemy
RUN pip install mysql-connector-python
RUN pip install requests
RUN pip install xgboost
RUN pip install scikit-learn
RUN pip install numpy

 CMD ["python", "main.py"]