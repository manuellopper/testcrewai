from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_openai import ChatOpenAI

# Uncomment the following line to use an example of a custom tool
# from research_crew.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
from crewai_tools import SerperDevTool
from src.historias_exito.config import SuccessStoryList,llm, SuccessStory, SuccessStoryReqInfo


@CrewBase
class ResearchCrew():
	"""ResearchCrew crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def web_search_expert(self) -> Agent:
		return Agent(
			config=self.agents_config['web_search_expert'],
			tools=[SerperDevTool()], 
			verbose=True,
			cache=True,
			use_system_prompt=True,
			allow_delegation=False,
			llm=llm,
		)

	@agent
	def validation_expert(self) -> Agent:
		return Agent(
			config=self.agents_config['validation_expert'],
			verbose=True,
			cache=True,
			use_system_prompt=True,
			allow_delegation=False,
			llm=llm,
		)

	@agent
	def project_manager(self) -> Agent:
		return Agent(
			config=self.agents_config['project_manager'],
			verbose=True,
			cache=True,
			use_system_prompt=True,
			allow_delegation=True,
			llm=llm,			
		)

	@task
	def success_stories_research_task(self) -> Task:
		return Task(
			config=self.tasks_config['success_stories_research_task'],
			output_pydantic=SuccessStoryList,
		)

	
	@crew
	def crew(self) -> Crew:
		"""Creates the ResearchCrew crew"""
		print(self.agents)
		print(self.tasks)
		return Crew(
			agents=[self.agents[0], self.agents[1]], # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator			
			verbose=True,
			respect_context_window=True,
			process=Process.hierarchical,
			#manager_agent=self.agents[2],
			manager_llm=ChatOpenAI(temperature=0, model="gpt-4"),
			memory=True,
			planning=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
