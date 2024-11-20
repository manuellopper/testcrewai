from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task


# Uncomment the following line to use an example of a custom tool
# from research_crew.tools.custom_tool import MyCustomTool

from src.successFlow.config import SuccessStoriesList,llm


@CrewBase
class ValidationCrew:
	"""ValidationCrew crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def validation_expert(self) -> Agent:
		return Agent(
			config=self.agents_config['validation_expert'],
			verbose=True,				
			llm=llm,
		)

	@task
	def success_stories_validation_task(self) -> Task:
		return Task(
			config=self.tasks_config['success_stories_validation_task'],
			output_pydantic=SuccessStoriesList,
		)

	
	@crew
	def crew(self) -> Crew:
		"""Creates the ValidationCrew crew"""		
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator			
			verbose=True,			
			process=Process.sequential,						
		)
