# HireReady

TEAM MEMBERS:KAVYA,HEMIN,NITHYA
An AI-powered interview preparation and resume parsing platform designed to help candidates ace their job interviews.

## 🌟 Features

- **Resume Parsing**: Upload and analyze your resume to extract key information
- **Interview Practice**: Conduct mock interviews with AI-powered feedback
- **Interview History**: Track your interview performance and progress over time
- **User Profile**: Manage your profile and interview preferences
- **Real-time Feedback**: Get instant feedback on your responses during mock interviews

## 🛠️ Tech Stack

### Backend

- **Python** with Flask framework
- **SQLite/Database** for data persistence
- **AI/ML** integration for interview evaluation

### Frontend

- **React** with Vite for fast development
- **Tailwind CSS** for styling
- **JavaScript/JSX** for interactive components
- **Axios** for API communication

## 📋 Prerequisites

- Python 3.8+
- Node.js 14+
- npm or yarn

## 🚀 Installation & Setup

### Backend Setup

```bash
cd backend
pip install -r requirements.txt
```

### Frontend Setup

```bash
cd frontend
npm install
```

## ▶️ Running the Application

### Windows

```bash
./setup.bat
./start.bat
```

### Linux/Mac

```bash
./setup.sh
```

### Manual Start

**Backend:**

```bash
cd backend
python main.py
```

**Frontend:**

```bash
cd frontend
npm run dev
```

## 📁 Project Structure

```
HireReady/
├── backend/
│   ├── main.py              # Main Flask application
│   ├── database.py          # Database configuration
│   └── requirements.txt      # Python dependencies
├── frontend/
│   ├── src/
│   │   ├── pages/           # React pages (Interview, History, Profile, Login)
│   │   ├── api.js           # API client
│   │   ├── App.jsx          # Main App component
│   │   └── main.jsx         # Entry point
│   ├── package.json         # Node dependencies
│   └── vite.config.js       # Vite configuration
├── app.py                   # Root entry point
└── database.py              # Root database configuration
```

## 🔧 Available Pages

- **Login**: User authentication
- **Interview**: Conduct mock interviews with AI
- **History**: View past interview sessions and performance analytics
- **Profile**: Manage user profile and preferences

## 👥 Contributors

- Hemin
- Kavya
- Nithya
