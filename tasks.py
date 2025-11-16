from crewai import Task
from agent import research_agent, post_writer_agent

Research_agent_task = Task(
    description="""Use the Research Agent to gather relevant information for creating LinkedIn posts based on the user's input.
    Your Research Should :
    1. Utilize the available tools to collect accurate and up-to-date information.
    2. Ensure the information gathered is comprehensive and relevant to the user's input.
    3. Provide clear and concise summaries of the information collected.
    4. Prepare the information in a format that can be easily used by the Post Writer Agent.
    5. Focus on quality over quantity, ensuring that the data is valuable and actionable.,
    6. Make sure the Content you fetch have very high virality rate (9.9/10)""",
    expected_output="A well-researched summary of information relevant to the user's input, ready for the Post Writer Agent to use in crafting LinkedIn posts.",
    agent=research_agent,
    output_file= "tasks_outputs/research_agent_output.txt"
)

Post_writer_agent_task = Task(
    description="""Use the Post Writer Agent to create engaging and well-structured LinkedIn posts based on the research findings provided by the Research Agent.
    Your Posts Should :
    1. Be tailored to resonate with LinkedIn's professional audience.
    2. Provide value, insights, and actionable takeaways.
    3. Be well-structured and easy to read.
    4. Include proper hashtags and emojis to increase engagement.
    5. Aim for a high virality rate (9.9/10)""",
    expected_output="Engaging and well-structured LinkedIn posts based on the research findings.",
    agent=post_writer_agent,
    output_file= "tasks_outputs/post_writer_agent_output.txt"
)