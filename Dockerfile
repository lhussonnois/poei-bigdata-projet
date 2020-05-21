FROM python:3.8

WORKDIR /usr/src/app

RUN pip3 install --upgrade pip
RUN pip3 install python-dev-tools

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

COPY . /

RUN /bin/bash -c "source $HOME/.poetry/env && poetry install && poetry build"

RUN pip3 install /dist/poei-projet-0.1.0.tar.gz

ENTRYPOINT  ["/bin/bash", "-c"]