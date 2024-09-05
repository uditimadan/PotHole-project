FROM python:3.9

# Set environment variables

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Run migrations and collect static files
RUN python app/manage.py migrate
RUN python app/manage.py collectstatic --noinput

# Command to run the application
CMD ["python", "app/manage.py", "runserver", "0.0.0.0:8000"]
