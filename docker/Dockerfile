FROM python:3.9



ARG HOST_USER_UID=1000
ARG HOST_USER_GID=1000



RUN set -ex                                                 && \
                                                               \
    echo 'Creating notroot user and group '                 && \
    groupadd -g $HOST_USER_GID notroot                      && \
    useradd -lm -u $HOST_USER_UID -g $HOST_USER_GID myuser  && \
    echo 'creating work-dir' && \
    mkdir /opt/work-dir  && \ 
    mkdir /opt/work-dir/data



COPY  ../src/main.py ../src/model_dump ../src/requirements.txt /opt/work-dir/

 

RUN chown -R $HOST_USER_UID:$HOST_USER_GID /opt/work-dir/


WORKDIR /opt/work-dir/ 

USER myuser
RUN cd /opt/work-dir/ && python3 -m pip install --upgrade pip && pip3 install -r requirements.txt
CMD ["python3","main.py"]