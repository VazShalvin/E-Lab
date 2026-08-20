#!/bin/bash

# E-Lab Setup Script
# Automates the initial setup process

echo "🚀 Starting E-Lab setup..."

echo "📋 Checking prerequisites..."
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker and try again."
    exit 1
fi

if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose is not installed. Please install Docker Compose and try again."
    exit 1
fi

echo "✅ Prerequisites satisfied"

echo "📂 Setting up environment..."
if [ ! -f ".env" ]; then
    cp .env.example .env
    echo "✅ Created .env file from example"
else
    echo "✅ .env file already exists"
fi

echo "🐳 Building Docker containers..."
docker compose up -d --build

echo "⏳ Waiting for database to initialize..."
sleep 10

echo "🗃️  Running database migrations..."
docker compose exec web python manage.py migrate

echo "👤 Creating HOD user..."
docker compose exec web python manage.py create_hod

echo "📚 Importing questions..."
docker compose exec web python manage.py import_questions

echo "🎯 Setup complete!"
echo ""
echo "📋 Next steps:"
echo "  1. Access the application at http://localhost"
echo "  2. Log in with HOD credentials:"
echo "     - Username: hod"
echo "     - Password: hodpassword"
echo "  3. IMPORTANT: Change the default HOD password immediately!"
echo ""
echo "💡 Need help? Check the README.md file or run:"
echo "  docker-compose logs  # View container logs"
echo "  docker-compose ps    # Check container status"