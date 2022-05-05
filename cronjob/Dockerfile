FROM amd64/python:3.9.7-slim

WORKDIR /app

# Uncomment the line below and to add your apt-get packages
# RUN apt-get update && apt-get install -y openssh-client git

COPY requirements.txt *.whl /app/

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# These lines ensure that the latest version of the Jetpack SDK is installed
# without reinstalling your other dependencies
ADD https://releases.jetpack.io/sdk/python/version.txt ./jetpack-python-sdk-version.txt
RUN pip install jetpack-io -U

COPY ./app /app
