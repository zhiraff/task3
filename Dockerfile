FROM python:3.12

ENV PYTHONUNBUFFERED=1
ENV POETRY_VERSION=1.8.3

ARG INSTALL_PATH=/srv/rest_api

WORKDIR $INSTALL_PATH

RUN rm -rf /etc/localtime
RUN ln -s /usr/share/zoneinfo/Europe/Moscow /etc/localtime
RUN echo "Europe/Moscow" > /etc/timezone
RUN apt update; apt install graphviz graphviz-dev build-essential -y
# RUN apt -o "Acquire::https::Verify-Peer=false" update ; apt -o "Acquire::https::Verify-Peer=false" install build-essential graphviz graphviz-dev -y
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
ENV PATH="${PATH}:/root/.poetry/bin"
COPY . .
RUN poetry install --no-root

RUN chown -R www-data $INSTALL_PATH

USER www-data
EXPOSE 8000
ENV PYTHONPATH "${PYTHONPATH}:${INSTALL_PATH}"
CMD ["litestar", "run"]