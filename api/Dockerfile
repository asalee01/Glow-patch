# python base image
FROM python:3.9

# update packages
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

# set the working directory in the container
WORKDIR /code

# add requirements file to the image
COPY ./requirements.txt /code/requirements.txt

# install dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# add python code
COPY ./app /code/app

# specify default command to run on container start
CMD ["fastapi", "run", "app/main.py", "--port", "80"]