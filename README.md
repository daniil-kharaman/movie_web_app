# Movie Library

Web application for managing personal movie collections with AI-powered movie recommendations.

## 📋 Overview

Movie Library is a Flask-based web application that allows users to create personal movie libraries, track their favorite films, and receive personalized movie recommendations based on their existing collection and current mood using Google's Gemini AI.

## ✨ Features

- **Multi-user Support**: Create and manage multiple user profiles
- **Movie Management**: Add, update, and delete movies in personal collections
- **External API Integration**: Fetch movie data from OMDb API including titles, directors, release years, ratings, and posters
- **AI-Powered Recommendations**: Get personalized movie suggestions based on your collection and mood using Google's Gemini AI
- **Responsive Design**: Clean, modern interface that works across devices

## 🛠️ Technologies

- **Backend**: Python, Flask
- **Database**: SQLAlchemy ORM
- **AI Integration**: Google Gemini AI
- **External API**: OMDb API for movie data
- **Frontend**: HTML, CSS, Jinja2 templates

## 🚀 Installation

1. Clone the repository:
git clone https://github.com/daniil-kharaman/movie_web_app.git
cd movie_web_app


2. Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate


3. Install dependencies:
pip install -r requirements.txt


4. Set up environment variables:
Create a `.env` file in the root directory with the following variables:
SECRET_KEY=your_secret_key
API_KEY=your_omdb_api_key
GEMINI_API_KEY=your_gemini_api_key


5. Initialize the database:
flask db upgrade


6. Run the application:
python app.py


7. Access the application at `http://localhost:5000`

## 📝 Usage

1. **Create a User**: Start by creating a user profile
2. **Add Movies**: Search and add movies to your collection
3. **Get Recommendations**: Specify your current mood to receive AI-powered movie recommendations
4. **Manage Collection**: Update or delete movies in your collection

## 🔄 Database Migrations

The application uses Flask-Migrate for database migrations. To create a new migration after model changes:

flask db migrate -m "Description of changes"
flask db upgrade


## 🔑 API Keys

This application requires two API keys:
- **OMDb API Key**: Get it from [OMDb API](https://www.omdbapi.com/apikey.aspx)
- **Google Gemini API Key**: Get it from [Google AI Studio](https://ai.google.dev/)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
