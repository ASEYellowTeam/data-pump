FROM python:3.6
ADD ./ ./
RUN pip install -r requirements.txt
CMD celery worker -A datapump.datapump -B
