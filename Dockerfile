FROM python:3.6.9
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /orderClusteringService
COPY requirements.txt /orderClusteringService/
RUN pip install -r requirements.txt
COPY . /orderClusteringService/
CMD [ "python","./orderClustering/manage.py","runserver","0.0.0.0:8000" ]
EXPOSE 8000