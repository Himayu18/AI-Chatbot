"# AI-Chatbot" 

# AI Chatbot Web Application

A modern, interactive AI chatbot web application powered by multiple state-of-the-art language models. Built with a clean HTML/Tailwind CSS/JavaScript frontend and a robust Django backend.

## Features

- 🤖 **Multiple AI Models**: Switch between four powerful AI models
  - Mistral AI Devstral-2512
  - Xiaomi Mimo-v2-Flash
  - NVIDIA Nemotron-3-Nano-30B
  - Cognitive Computations Dolphin-Mistral-24B (Venice Edition)
- 💬 **Real-time Chat Interface**: Smooth, responsive chat experience
- 🎨 **Modern UI**: Clean interface built with Tailwind CSS
- 🔄 **Model Switching**: Easily switch between different AI models
- 📱 **Responsive Design**: Works seamlessly on desktop and mobile devices
- ⚡ **Fast Response Times**: Optimized backend for quick AI responses

## Tech Stack

### Frontend
- **HTML5**: Semantic markup structure
- **Tailwind CSS**: Utility-first CSS framework for styling
- **JavaScript**: Interactive functionality and API communication

### Backend
- **Django**: High-level Python web framework
- **Django REST Framework**: API endpoints for frontend communication
- **Python 3.8+**: Backend logic and AI model integration

### AI Models
- **mistralai/devstral-2512**: Specialized development-focused model
- **xiaomi/mimo-v2-flash**: Fast, efficient conversational AI
- **nvidia/nemotron-3-nano-30b-a3b**: Compact yet powerful NVIDIA model
- **cognitivecomputations/dolphin-mistral-24b-venice-edition**: Enhanced Mistral variant with improved capabilities

## Prerequisites

Before running this application, ensure you have the following installed:

- Python 3.8 or higher
- pip (Python package manager)
- Node.js and npm (for Tailwind CSS CLI, optional)
- Git

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai-chatbot.git
cd ai-chatbot
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# API Keys for AI Models
MISTRAL_API_KEY=your-mistral-api-key
XIAOMI_API_KEY=your-xiaomi-api-key
NVIDIA_API_KEY=your-nvidia-api-key
DOLPHIN_API_KEY=your-dolphin-api-key
```

### 5. Run Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 7. Collect Static Files

```bash
python manage.py collectstatic
```

### 8. Run the Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser to access the application.

## Project Structure

```
ai-chatbot/
├── backend/
│   ├── chatbot/
│   │   ├── models.py          # Database models
│   │   ├── views.py           # API views
│   │   ├── serializers.py     # Data serializers
│   │   └── urls.py            # URL routing
│   ├── ai_models/
│   │   ├── mistral.py         # Mistral AI integration
│   │   ├── xiaomi.py          # Xiaomi model integration
│   │   ├── nvidia.py          # NVIDIA model integration
│   │   └── dolphin.py         # Dolphin model integration
│   └── settings.py            # Django settings
├── frontend/
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css     # Custom styles
│   │   └── js/
│   │       └── main.js        # JavaScript logic
│   └── templates/
│       └── index.html         # Main HTML template
├── requirements.txt           # Python dependencies
├── .env.example              # Environment variables example
├── manage.py                 # Django management script
└── README.md                 # This file
```

## Usage

### Starting a Conversation

1. Open the application in your browser
2. Select your preferred AI model from the dropdown menu
3. Type your message in the input field
4. Press Enter or click the Send button
5. View the AI's response in the chat window

### Switching Models

Click on the model selector dropdown in the interface to switch between available AI models. Each model has different strengths:

- **Devstral-2512**: Best for coding and development queries
- **Mimo-v2-Flash**: Fastest responses, great for quick conversations
- **Nemotron-3-Nano**: Balanced performance and efficiency
- **Dolphin-Mistral-24B**: Most capable for complex reasoning

## API Endpoints

### POST `/api/chat/`
Send a message to the chatbot

**Request Body:**
```json
{
  "message": "Hello, how are you?",
  "model": "mistralai/devstral-2512"
}
```

**Response:**
```json
{
  "response": "Hello! I'm doing well, thank you for asking...",
  "model_used": "mistralai/devstral-2512",
  "timestamp": "2024-12-29T10:30:00Z"
}
```

### GET `/api/models/`
Get list of available AI models

**Response:**
```json
{
  "models": [
    "mistralai/devstral-2512",
    "xiaomi/mimo-v2-flash",
    "nvidia/nemotron-3-nano-30b-a3b",
    "cognitivecomputations/dolphin-mistral-24b-venice-edition"
  ]
}
```

## Configuration

### Tailwind CSS

If you want to customize the Tailwind configuration:

1. Install Tailwind CSS CLI
```bash
npm install -D tailwindcss
npx tailwindcss init
```

2. Update `tailwind.config.js` with your custom configuration
3. Build your CSS
```bash
npx tailwindcss -i ./frontend/static/css/input.css -o ./frontend/static/css/output.css --watch
```

### AI Model Configuration

Edit the model configurations in `backend/ai_models/config.py`:

```python
MODEL_CONFIGS = {
    'mistralai/devstral-2512': {
        'max_tokens': 2048,
        'temperature': 0.7,
    },
    # Add other model configurations
}
```

## Troubleshooting

### Common Issues

**Issue**: Models not responding
- **Solution**: Check your API keys in the `.env` file
- Verify your internet connection
- Check API rate limits

**Issue**: Static files not loading
- **Solution**: Run `python manage.py collectstatic`
- Check your `STATIC_URL` and `STATIC_ROOT` settings

**Issue**: CORS errors
- **Solution**: Install and configure `django-cors-headers`
- Add appropriate origins to `CORS_ALLOWED_ORIGINS`

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Mistral AI for the Devstral model
- Xiaomi for the Mimo-v2-Flash model
- NVIDIA for the Nemotron model
- Cognitive Computations for the Dolphin-Mistral variant
- Django and Tailwind CSS communities

## Contact

For questions or support, please open an issue on GitHub or contact the maintainers.

---

**Note**: Remember to keep your API keys secure and never commit them to version control. Always use environment variables for sensitive configuration.
