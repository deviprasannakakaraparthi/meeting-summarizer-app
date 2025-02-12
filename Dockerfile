# Use the official Python image from Docker Hub
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Copy project files into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port for Streamlit app (default is 8501)
EXPOSE 8501

# Set the command to run your application (Streamlit in this case)
CMD ["streamlit", "run", "app.py"]

