# Google Agent Development Kit (ADK) / Gemini Integration

This guide explains how to use **Google's Agent Development Kit** (Gemini API / Vertex AI) with your LinkedIn post writer.

## Overview

Your `tools.py` now includes a wrapper class `GoogleGenAITool` that integrates Google's latest Gen AI SDK (`google-genai`). This allows you to:

- **Replace Ollama** with Google Gemini models (2.5 Flash, Pro, etc.)
- **Use Vertex AI** from Google Cloud with your own models
- **Access advanced features**: images, videos, embeddings, function calling, and more

## Installation

Google Gen AI SDK is already installed:

```powershell
pip install google-genai
```

## Quick Start

### Option 1: Use Gemini Developer API (Free)

1. **Get an API Key:**
   - Go to [ai.google.dev](https://ai.google.dev)
   - Create a new API key

2. **Add to `.env`:**
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

3. **Use in your agent:**
   ```python
   from tools import google_tool
   
   # Generate content with Gemini
   response = google_tool.generate("Write a LinkedIn post about AI")
   print(response)
   ```

### Option 2: Use Vertex AI (Google Cloud)

1. **Setup Google Cloud:**
   - Create a project in [Google Cloud Console](https://console.cloud.google.com)
   - Enable Vertex AI API
   - Create a service account with Vertex AI permissions
   - Download JSON key and set `GOOGLE_APPLICATION_CREDENTIALS`

2. **Add to `.env`:**
   ```
   GOOGLE_GENAI_USE_VERTEXAI=true
   GOOGLE_CLOUD_PROJECT=your-project-id
   GOOGLE_CLOUD_LOCATION=us-central1
   ```

3. **Use in your agent:**
   ```python
   from tools import google_tool
   
   response = google_tool.generate("Write a LinkedIn post about AI")
   print(response)
   ```

## Integration with CrewAI

### Replace Ollama LLM with Google Gemini

Modify `agent.py`:

```python
from crewai.llm import LLM
from tools import google_tool

# Replace Ollama with Gemini
llm = LLM(
    model="gemini-2.5-flash",  # or any Gemini model
    provider="google",
    api_key=os.environ.get("GEMINI_API_KEY"),
    temperature=0.7,
    max_tokens=1500
)

research_agent = agent.Agent(
    role="Research Agent",
    name="Research Agent",
    llm=llm,
    goal="Gather information for LinkedIn posts",
    tools=[dev_tool, scrape_tool, file_reader],
    verbose=True,
)
```

### Use Google GenAI as a Custom Tool

Add `google_tool` to any agent:

```python
from tools import google_tool, GOOGLE_GENAI_AVAILABLE

if GOOGLE_GENAI_AVAILABLE:
    research_agent = agent.Agent(
        role="Research Agent",
        tools=[dev_tool, scrape_tool, file_reader, google_tool],
        # ...
    )
```

## Available Models

### Gemini Developer API
- `gemini-2.5-flash` (fastest, most affordable)
- `gemini-2.5-pro` (higher quality)
- `gemini-2.0-flash-001`
- `gemini-pro`
- `gemini-pro-vision` (image understanding)

### Vertex AI (Google Cloud)
- All Gemini models
- Custom tuned models
- Open source models (Gemma, Llama 3.2, etc.)

## Advanced Usage

### With Custom Configuration

```python
from tools import GoogleGenAITool

# Create custom instance
tool = GoogleGenAITool(
    model="gemini-2.5-pro",
    vertex=False,  # Use Gemini Developer API
)

result = tool.generate("Your prompt here", max_output_tokens=500, temperature=0.3)
```

### With Function Calling (Vertex AI)

```python
from google import genai
from google.genai import types

client = genai.Client(
    vertexai=True,
    project="your-project",
    location="us-central1"
)

# Define a function the model can call
def get_weather(location: str) -> str:
    return f"Sunny in {location}"

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="What's the weather in Boston?",
    config=types.GenerateContentConfig(
        tools=[get_weather]
    ),
)
```

### Image Analysis

```python
from google.genai import types

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[
        "Analyze this LinkedIn post image",
        types.Part.from_uri(
            file_uri="gs://bucket/image.png",
            mime_type="image/png"
        )
    ]
)
```

## Pricing

- **Gemini Developer API**: Free tier + pay-as-you-go
  - Text input: $0.075 per 1M tokens
  - Text output: $0.30 per 1M tokens
  
- **Vertex AI**: Requires Google Cloud subscription
  - Pay per API call (varies by model)
  - Includes free tier credits

## Environment Variables Reference

```bash
# Gemini Developer API
GEMINI_API_KEY=your_api_key

# Vertex AI
GOOGLE_GENAI_USE_VERTEXAI=true
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_CLOUD_LOCATION=us-central1
GOOGLE_APPLICATION_CREDENTIALS=/path/to/service-account.json
```

## Troubleshooting

### API Key Not Found
```
Error: No API key found
```
Solution: Set `GEMINI_API_KEY` in `.env` or environment

### Vertex AI Auth Failed
```
Error: Authentication failed
```
Solution: Ensure service account has Vertex AI permission and `GOOGLE_APPLICATION_CREDENTIALS` is set

### Model Not Found
```
Error: Model not found
```
Solution: Verify model name in your region. Check available models:
```python
client = genai.Client()
for model in client.models.list():
    print(model.name)
```

## Resources

- [Gemini API Docs](https://ai.google.dev/gemini-api/docs)
- [Vertex AI Docs](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)
- [Python SDK GitHub](https://github.com/googleapis/python-genai)
- [CrewAI Integration Guide](https://docs.crewai.com)

## Next Steps

1. Choose Gemini Developer API or Vertex AI
2. Get credentials and add to `.env`
3. Update `agent.py` to use Google LLM
4. Run your crew with Gemini models
5. Monitor usage and costs
