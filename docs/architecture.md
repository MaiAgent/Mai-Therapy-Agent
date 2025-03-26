# Mai Therapy Agent - System Architecture

## Overview
Mai Therapy Agent is a web-based AI chatbot designed to provide trading therapy and meme coin trading guidance. It leverages OpenAI's GPT-3.5-turbo model for natural language processing, delivered through a sleek, professional front-end interface.

## Components
1. **Front-End**:
   - HTML/CSS/JavaScript: Responsive UI with a modern design.
   - Static assets (images, styles) served from `src/static/`.

2. **Back-End**:
   - Python-based logic in `src/main.py`.
   - Integrates with OpenAI API for AI-driven responses.

3. **Deployment**:
   - Designed for easy deployment on platforms like Heroku or AWS.
   - CI pipeline via GitHub Actions ensures code quality.

## Data Flow
1. User inputs a message via the web interface.
2. The input is sent to `main.py`, which processes it and queries the OpenAI API.
3. The AI response is formatted and displayed in the chatbox.

## Scalability
- Modular design allows for additional features (e.g., real-time market data integration).
- Stateless architecture supports horizontal scaling.

## Security
- API key stored securely (not hardcoded in production).
- Input sanitization to prevent injection attacks.
