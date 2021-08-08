FROM python:3.8-slim

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV FLASK_ENV=development
ENV FLASK_APP=main.py
EXPOSE 5000

# Install dependencies:
WORKDIR /web
ADD . /web
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN pip install -e .

# Run the application:
CMD ["python","main.py"]