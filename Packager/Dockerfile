# FROM muccg/devpi
FROM python:3.11
RUN echo $SERVER_DIR

# USER root

RUN pip install -U devpi-web devpi-client devpi-server
# RUN devpi-init --serverdir "$SERVER_DIR"
# CMD devpi-server --serverdir "$SERVER_DIR" --host packager


# RUN devpi-gen-config
RUN devpi --init
COPY . .
# RUN devpi user -c testuser password=123
# RUN devpi login testuser --password=123
RUN devpi use http://localhost:3141
RUN devpi index -c dev bases=root/pypi
RUN devpi use testuser/dev

CMD devpi-server --serverdir "$SERVER_DIR" --host packager