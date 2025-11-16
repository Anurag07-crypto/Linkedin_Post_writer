from crewai import Crew, Process
from tasks import Research_agent_task, Post_writer_agent_task
from agent_gemini import research_agent, post_writer_agent

crew = Crew(
    agents=[research_agent, post_writer_agent],
    tasks=[Research_agent_task, Post_writer_agent_task],
    process=Process.sequential,
    verbose=True
)

if __name__ == "__main__":
    print("Starting the LinkedIn Post Writer Crew...")
    
    # Get user input for the LinkedIn post topic
    user_input = input("\nEnter the topic or subject for your LinkedIn post: ")
    
    try:
        # Run the crew with user input
        results = crew.kickoff(inputs={"topic": user_input})
        
        # Display the results
        print("\n" + "="*60)
        print("LINKEDIN POST CREATED SUCCESSFULLY!")
        print("="*60)
        print(results)
        
    except Exception as e:
        print(f"\nError occurred: {str(e)}")
        print("Please make sure:")
        print("1. Ollama is running with mistral-7b-v0.1 model")
        print("2. All required tools are installed")
        print("3. Internet connection is available for web scraping")