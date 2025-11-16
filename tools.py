import vagent

from crewai_tools import SerperDevTool, ScrapeWebsiteTool, FileReadTool
import os

# Optional: Google Gen AI (Agent Development Kit / Vertex AI)
try:
	from google import genai
	from google.genai import types
	GOOGLE_GENAI_AVAILABLE = True
except Exception:
	genai = None
	types = None
	GOOGLE_GENAI_AVAILABLE = False

file_reader=FileReadTool()
dev_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()

if GOOGLE_GENAI_AVAILABLE:
	class GoogleGenAITool:
		"""Simple wrapper tool to call Google GenAI (Gemini/Vertex) from CrewAI.

		Requirements:
		- pip install google-genai
		- Set GOOGLE_GENAI_USE_VERTEXAI=true, GOOGLE_CLOUD_PROJECT and GOOGLE_CLOUD_LOCATION
		  for Vertex AI integration, or set GEMINI_API_KEY for Gemini Developer API.

		"""

		def __init__(self, model: str = "gemini-2.5-flash", vertex: bool = True, project: str | None = None, location: str | None = None):
			self.model = model
			self.vertex = vertex
			# Use environment if project/location are not provided
			self.project = project or os.environ.get("GOOGLE_CLOUD_PROJECT")
			self.location = location or os.environ.get("GOOGLE_CLOUD_LOCATION")
			if self.vertex:
				self.client = genai.Client(vertexai=True, project=self.project, location=self.location)
			else:
				# For Gemini Developer API key
				api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
				self.client = genai.Client(api_key=api_key)

		def generate(self, prompt: str, max_output_tokens: int = 250, temperature: float = 0.7):
			response = self.client.models.generate_content(
				model=self.model,
				contents=prompt,
				config=types.GenerateContentConfig(
					max_output_tokens=max_output_tokens,
					temperature=temperature,
				),
			)
			return response.text

	# Lazy initialization: only create tool when explicitly used
	google_tool = None
else:
	google_tool = None