FROM python:3.5-alpine
COPY . /code
WORKDIR /code
RUN python setup.py install
RUN pip install gunicorn
CMD ["gunicorn", "test_package:app", "-w", "4", "-b", "0.0.0.0:8910"]
