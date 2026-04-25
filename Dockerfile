FROM python
WORKDIR /ss
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "main.py"]
