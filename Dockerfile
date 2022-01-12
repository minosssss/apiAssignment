FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/minosssss/apiAssignment

WORKDIR /home/apiAssignment/

RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]