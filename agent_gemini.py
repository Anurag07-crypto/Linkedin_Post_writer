
import os
from dotenv import load_dotenv
from crewai import agent
from crewai.llm import LLM
from tools import dev_tool, scrape_tool, file_reader

# Load environment variables
load_dotenv()

# Check if we're using Vertex AI or Gemini API
use_vertex_ai = os.environ.get("GOOGLE_GENAI_USE_VERTEXAI", "false").lower() == "true"

if use_vertex_ai:
    # Configuration for Vertex AI (Google Cloud)
    llm = LLM(
        model="gemini-2.5-flash",
        provider="vertexai",
        project=os.environ.get("GOOGLE_CLOUD_PROJECT"),
        location=os.environ.get("GOOGLE_CLOUD_LOCATION", "us-central1"),
        temperature=0.7,
        max_tokens=1500,
    )
else:
    # Configuration for Gemini Developer API
    llm = LLM(
        model="gemini-2.5-flash",
        provider="google",
        api_key=os.environ.get("GEMINI_API_KEY"),
        temperature=0.7,
        max_tokens=1500,
    )

def system_template():
    return """You are an elite level LinkedIn post writer.
            Your task is to create engaging, well-structured LinkedIn posts based on the user's
            input and any relevant information you can gather using the available tools.
            Use a professional and conversational tone, and ensure that your posts are tailored to resonate with LinkedIn's professional audience.
            Always aim to provide value, insights, and actionable takeaways in your posts.
            Make sure to utilize the tools at your disposal to gather accurate and up-to-date information."""

research_agent = agent.Agent(
    role="Research Agent",
    name="Research Agent",
    llm=llm,
    goal="Gather relevant Information for creating LinkedIn posts according to the user's input, make sure to use the available tools to collect accurate and up-to-date information.",
    backstory="""You are an expert researcher specialized in collecting information for LinkedIn posts.
            You have access to various tools that can help you find and scrape information from the web, as well as read files provided by the user.
            Your objective is to gather comprehensive and relevant data that will aid in crafting engaging LinkedIn posts.
            Always ensure the information you collect is accurate and up-to-date.""",
    tools=[dev_tool, scrape_tool, file_reader],
    system_template=system_template(),
    verbose=True,
    max_iter=3,
    max_rpm=15
)

post_writer_agent = agent.Agent(
    role="Post Writer",
    name="Post Writer",
    llm=llm,
    goal="Create engaging and well-structured LinkedIn posts based on the research findings provided by the Research Agent.",
    backstory="""You are a skilled LinkedIn post writer with a knack for crafting content that resonates with professionals.
            Your role is to take the information gathered by the Research Agent and transform it into compelling LinkedIn posts.
            You understand the nuances of LinkedIn's audience and know how to write posts that are both informative and engaging.
            Always aim to provide value, insights, and actionable takeaways in your posts.
            Also make sure that the posts are well-structured and easy to read.
            Also make sure that the posts have proper hashtags and emojis to increase engagement.
            Aim for posts with high virality potential (9.9/10 rating).""",
    tools=[],
    system_template=system_template(),
    verbose=True,
    max_iter=3,
    max_rpm=15
)
