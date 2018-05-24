FROM python:3.6.5-jessie

MAINTAINER "sidh711@gmail.com"

ENV PYTHONUNBUFFERED 1

RUN useradd -u 1000 siddhesh -d /home/siddhesh

RUN mkdir -p /home/siddhesh/bin
RUN chown -R siddhesh:siddhesh /home/siddhesh

ENV PATH="/home/siddhesh/bin:${PATH}"

USER siddhesh

RUN mkdir -p /home/siddhesh/psngr

RUN cd /home/siddhesh/
COPY ./requirements*.txt /home/siddhesh/psngr/


RUN python3 -m venv /home/siddhesh/psngr_env \
    && ls -al

WORKDIR /home/siddhesh/psngr
RUN /bin/bash -c "source /home/siddhesh/psngr_env/bin/activate \
    && which python \
    && cd /home/siddhesh/psngr"

RUN /bin/bash -c "source /home/siddhesh/psngr_env/bin/activate \
    && pip install --upgrade pip \
    && pwd && ls"

RUN /bin/bash -c "source /home/siddhesh/psngr_env/bin/activate \
    && pip install -r requirements.txt"
    
USER root
RUN rm -rf /home/siddhesh/psngr

RUN ln -s /home/siddhesh/psngr_env/bin/python /home/siddhesh/bin/psngr_env \
    && chmod 755 /home/siddhesh/bin/psngr_env