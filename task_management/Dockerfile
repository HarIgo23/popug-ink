FROM python:alpine as base
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# deps image
FROM base as python-deps

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev libffi-dev openssl-dev cargo
# install dependencies
RUN pip install pipenv
COPY ./Pipfile.lock .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --ignore-pipfile

# runtime image
FROM base as runtime
# copy virtual env
COPY --from=python-deps /.venv /.venv
ENV PATH="/.venv/bin:$PATH"
# copy entrypoint.sh
COPY ./entrypoint.sh .
# set up workdir
WORKDIR /usr/src/app
# copy project
COPY . .
# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]