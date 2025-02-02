# Use official Python image
FROM python:3.9

# Set the working directory
WORKDIR /app

# ✅ Copy only requirements.txt first (improves Docker cache efficiency)
COPY requirements.txt .

# ✅ Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# ✅ Copy the rest of the application files
COPY . /app

# Expose port 8000 for Django
EXPOSE 8000

# Run migrations and start Django server
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
