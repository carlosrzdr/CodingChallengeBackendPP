FROM python:3.8-slim

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN export FLASK_ENV=development

# Install dependencies:
WORKDIR /web
ADD . /web
RUN pip install -r requirements.txt

RUN pip install -e .

# Run the application:
CMD ["flask","run"]