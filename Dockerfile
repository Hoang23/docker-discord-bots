From python:3.8.0-buster

# Make a directory for our application
WORKDIR /app

# Install dependencies: copy requirements txt to "." (current docker directory)
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy our source code: # copy source code to "." (current docker directory)
Copy /app .

# Run the application
CMD ["python", "bot.py"]
