FROM python:3.10.2-slim-buster AS builder

ARG INSTALL_DEV=false

COPY requirements.txt requirements.dev.txt /

RUN bash -c "if [ ${INSTALL_DEV} == 'true' ] ; \
    then \ 
        pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r /requirements.dev.txt ; \
    else \
        pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r /requirements.txt; \
    fi"


FROM python:3.10.2-slim-buster

ENV PYTHONUNBUFFERED 1

ENV PYTHONPATH /usr/src/ciplay-task

# copy from first layer pip wheels dependencies
ARG WHEELS_PATH=/usr/local/bin/wheels/
COPY --from=builder /app/wheels/* ${WHEELS_PATH}

# install dependencies
RUN apt update && \
    apt install -y netcat && \
    pip install --upgrade pip setuptools wheel && \
    pip install --no-cache ${WHEELS_PATH}*  && \
    # owner will be changed at the finish builing image 
    addgroup --system --gid 1000 ciplayapp &&\
    adduser --system --gid 1000 --uid 1000 ciplayapp

WORKDIR ${PYTHONPATH}

# copy project
COPY . .

# grant privilege
RUN chown -R 1000:1000 . && chmod +x ./scripts/*.sh

# change owner
USER ciplayapp

