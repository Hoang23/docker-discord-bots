From python:3.8.0-buster

# Make a directory for our application
WORKDIR /app
ENV coin_discord_token=NzM4NzgwOTU4OTQxMTE4NTc1.XyQ5Yg.PAxImaLxZ-5NaZIqvKSK7zuHMyg
# 0e7189c08e24 

# Install dependencies: copy requirements txt to "." (current docker directory)
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy our source code: # copy source code to "." (current docker directory)
Copy /app .

# Run the application
CMD ["python", "bot.py"]
