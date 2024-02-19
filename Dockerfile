# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.11.6
FROM python:${PYTHON_VERSION}-slim as base

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /janus

# Copy the directory
COPY janus /janus

# install dependencies
RUN pip install poetry
RUN poetry config virtualenvs.create false \
  && poetry install


# Expose the port that the application listens on.
EXPOSE 8000

# Run the application.
# Run the application using uvicorn
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]