# LinkedIn Post Writer AI Crew 📝✨

An intelligent AI-powered system that automatically researches topics and creates engaging, viral-worthy LinkedIn posts using CrewAI framework with local Ollama models or Google Gemini.

## 🎯 Overview

This project leverages multi-agent AI collaboration to:
1. **Research Agent**: Gathers comprehensive, up-to-date information on any topic
2. **Post Writer Agent**: Crafts professional, engaging LinkedIn posts optimized for virality

## 🚀 Features

- ✅ Multi-agent workflow with sequential task processing
- ✅ Web scraping and search capabilities for real-time information
- ✅ Support for both **Ollama (local)** and **Google Gemini AI**
- ✅ Automated hashtag and emoji integration
- ✅ High virality-focused content (9.9/10 rating target)
- ✅ Structured output saved to files
- ✅ Interactive CLI interface

## 📋 Prerequisites

- Python 3.8+
- Ollama (for local model) OR Google Gemini API key
- Internet connection for web scraping

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd linkedin-post-writer-crew
```

### 2. Install Dependencies
```bash
pip install crewai crewai-tools python-dotenv
```

### 3. Setup Ollama (Local Option)
```bash
# Install Ollama from https://ollama.ai
# Pull the required model
ollama pull mistral-7b-v0.1

# Start Ollama service
ollama serve
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

**For Ollama (Local):**
```env
OPENAI_API_KEY=sk-dummy-key-for-ollama
OLLAMA_MODEL=mistral-7b-v0.1
OLLAMA_BASE_URL=http://localhost:11434
```

**For Google Gemini:**
```env
GEMINI_API_KEY=your_gemini_api_key_here
```

**For Vertex AI (Google Cloud):**
```env
GOOGLE_GENAI_USE_VERTEXAI=true
GOOGLE_CLOUD_PROJECT=your_project_id
GOOGLE_CLOUD_LOCATION=us-central1
```

## 📁 Project Structure

```
linkedin-post-writer-crew/
│
├── main.py                 # Main execution file
├── agent.py               # Agent definitions (Ollama version)
├── agent_gemini.py        # Agent definitions (Gemini version)
├── tasks.py               # Task definitions
├── tools.py               # Tool configurations
├── .env                   # Environment variables
├── tasks_outputs/         # Output directory (auto-created)
│   ├── research_agent_output.txt
│   └── post_writer_agent_output.txt
└── README.md             # This file
```

## 🎮 Usage

### Using Ollama (Local Model)

1. Ensure Ollama is running:
```bash
ollama serve
```

2. Run the application:
```bash
python main.py
```

3. Enter your LinkedIn post topic when prompted:
```
Enter the topic or subject for your LinkedIn post: AI in Healthcare 2025
```

### Using Google Gemini

1. Update your imports in `main.py` and `tasks.py`:
```python
# Change from:
from agent import research_agent, post_writer_agent

# To:
from agent_gemini import research_agent, post_writer_agent
```

2. Run the application:
```bash
python main.py
```

## 📊 Output

The system generates two output files in `tasks_outputs/`:

1. **research_agent_output.txt**: Comprehensive research findings
2. **post_writer_agent_output.txt**: Final LinkedIn post with hashtags and emojis

## 🔧 Configuration

### Agent Settings

Both agents support customization in their respective files:

- `temperature`: Controls creativity (0.0 - 1.0)
- `max_tokens`: Maximum response length
- `max_iter`: Maximum iterations per agent (default: 3)
- `max_rpm`: Rate limit per minute (default: 15)

### Available Tools

- **SerperDevTool**: Web search capabilities
- **ScrapeWebsiteTool**: Extract content from websites
- **FileReadTool**: Read local files

## ⚠️ Troubleshooting

### Common Issues

**Issue**: "Ollama connection refused"
```bash
# Solution: Ensure Ollama is running
ollama serve
```

**Issue**: "Model not found"
```bash
# Solution: Pull the required model
ollama pull mistral-7b-v0.1
```

**Issue**: "Import error for crewai_tools"
```bash
# Solution: Install the correct package
pip install crewai-tools
```

**Issue**: "Google API authentication error"
```
# Solution: Verify your API key in .env file
# For Vertex AI, ensure gcloud CLI is configured:
gcloud auth application-default login
```

## 🎯 Best Practices

1. **Topic Selection**: Be specific with your topics for better research results
2. **Internet Connection**: Ensure stable connection for web scraping
3. **Model Selection**: 
   - Use Ollama for privacy and no API costs
   - Use Gemini for faster, more capable responses
4. **Rate Limits**: Respect API rate limits (configured in agent settings)

## 📈 Future Enhancements

- [ ] Add support for multiple post formats (carousel, video scripts)
- [ ] Implement A/B testing for post variants
- [ ] Add analytics prediction for engagement
- [ ] Multi-language support
- [ ] Integration with LinkedIn API for direct posting
- [ ] Custom prompt templates

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.


## 👨‍💻 Author

[Anurag kumar]

## 🙏 Acknowledgments

- [CrewAI](https://github.com/joaomdmoura/crewAI) - Multi-agent framework
- [Ollama](https://ollama.ai) - Local LLM runtime
- [Google Gemini](https://ai.google.dev/) - AI model provider

---

**Note**: This project is for educational and professional content creation purposes. Always review and edit AI-generated content before posting.
