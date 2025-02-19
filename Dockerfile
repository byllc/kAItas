FROM python:3.10.8
WORKDIR /home/kaitas 

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y build-essential bash-completion

# hdf5 needed for pytables installation
# libgles2-mesa needed for pytest-qt
RUN apt-get install -y libhdf5-dev libgles2-mesa-dev

RUN python -m pip install --upgrade pip
COPY requirements.txt /tmp
RUN python -m pip install -r /tmp/requirements.txt
RUN git config --global --add safe.directory /home/kaitas


ENV SHELL="/bin/bash"
CMD ["/bin/bash"]