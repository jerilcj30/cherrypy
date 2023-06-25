FROM python:3.10.7-slim-buster

# create the necessary directories
WORKDIR /app

# copy the necessary files
COPY . .

# install the dependencies
RUN pip install --user -r /app/requirements.txt

# set the PATH environment variable to include user-installed packages
ENV PATH="/root/.local/bin:${PATH}"

ENV PYTHONPATH=/app

# run the code
CMD ["python", "/app/server.py"]