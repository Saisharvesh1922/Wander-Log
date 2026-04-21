# WanderLog AI

A full-stack web application that lets users securely record, filter, search, and converse with their own travel memories. With a clean and modern UI, intelligent chatbot integration, and secure authentication, the platform transforms how you relive and interact with past journeys.

## Features

- **Secure Authentication**: User registration and login with JWT tokens
- **Travel Story Management**: Create, edit, delete, and organize travel stories
- **Image Upload**: Add photos to your travel memories with proper image handling
- **Advanced Search**: Filter and search through your travel stories
- **AI Chatbot**: Intelligent conversation with your travel history using LangChain and Groq
- **Modern UI**: Clean, responsive design built with React and Tailwind CSS
- **Real-time Updates**: Instant feedback and smooth user experience

## Tech Stack

### Frontend
- **React 19** - Modern React with hooks
- **Vite** - Fast development and build tool
- **Tailwind CSS** - Utility-first CSS framework
- **React Router** - Client-side routing
- **Axios** - HTTP client for API calls
- **React Icons** - Icon library
- **Moment.js** - Date manipulation

### Backend
- **Node.js** - JavaScript runtime
- **Express.js** - Web framework
- **MongoDB** - Database with Mongoose ODM
- **JWT** - Authentication tokens
- **Bcrypt** - Password hashing
- **Multer** - File upload handling
- **CORS** - Cross-origin resource sharing

### Chatbot
- **Python** - Chatbot backend
- **LangChain** - AI/ML framework
- **Groq API** - LLM API for chat responses
- **Flask** - Web framework for chatbot
- **FAISS** - Vector database for embeddings
- **HuggingFace** - Text embeddings

## Prerequisites

- Node.js (v18 or higher)
- Python (v3.8 or higher)
- MongoDB (local or MongoDB Atlas)
- Git

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Saisharvesh1922/WanderLog-AI.git
cd WanderLog-AI
```

### 2. Backend Setup
```bash
cd backend
npm install
```

### 3. Frontend Setup
```bash
cd frontend/dear-diary
npm install
```

### 4. Chatbot Setup
```bash
cd backend/Chat\ bot
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
pip install -r requirements.txt
```

## Environment Variables

### Backend (.env)
Create a `.env` file in the backend directory:
```env
ACCESS_TOKEN_SECRET=your_jwt_secret_key_here
```

### Chatbot (.env)
Create a `.env` file in the `backend/Chat bot` directory:
```env
GROQ_API_KEY=your_groq_api_key_here
```

### Database Configuration
Update `backend/config.json` with your MongoDB connection string:
```json
{
    "connectionString": "mongodb+srv://your_username:your_password@your-cluster.mongodb.net/?retryWrites=true&w=majority&appName=your-app"
}
```

## Running the Application

### 1. Start the Backend
```bash
cd backend
npm start
```
The backend will run on `http://localhost:8000`

### 2. Start the Frontend
```bash
cd frontend/dear-diary
npm run dev
```
The frontend will run on `http://localhost:5173`

### 3. Start the Chatbot
```bash
cd backend/Chat\ bot
python app.py
```
The chatbot will run on `http://localhost:2000`

## Usage

1. **Register Account**: Create a new user account
2. **Login**: Sign in with your credentials
3. **Add Travel Stories**: Click "Add Travel Story" to create new memories
4. **Upload Images**: Add photos to your travel stories
5. **Search & Filter**: Use the search bar to find specific stories
6. **Chat with AI**: Ask questions about your travel history to the chatbot

