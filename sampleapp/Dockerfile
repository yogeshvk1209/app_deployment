FROM centos:7
MAINTAINER yogeshvk1209@gmail.com
# Install py, pip and sudo
RUN yum install -y epel-release && yum install -y python3 python-pip sudo && pip install --upgrade pip && yum clean all
# Add taskuUser and provide sudo access
RUN useradd -m taskuser && echo "taskuser:taskuser" | chpasswd && echo 'taskuser ALL=(ALL:ALL) NOPASSWD: ALL' | sudo EDITOR='tee -a' visudo
# Install app dependencies
COPY ./src/ /src/
RUN pip3 install -r /src/requirements.txt
# Start app source
EXPOSE  8080
USER taskuser
CMD ["python3", "/src/pytask.py", "-p 8080"]
