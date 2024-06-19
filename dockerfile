FROM python:3.9-slim

# Set the working directory
WORKDIR /code

# Copy the requirements file
COPY ./src/requirements.txt /code/requirements.txt

# Install dependencies
RUN pip install uvicorn
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
# Copy the FastAPI app code
COPY ./src/app /code/app

# Expose the port FastAPI is running on
EXPOSE 8000

# Run the FastAPI application
CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]