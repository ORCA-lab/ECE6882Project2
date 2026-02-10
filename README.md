# Welcome to ECE6882 Reinforcement Learning Project 2 Repo


1. Description and requirement of project:
   
      This project used environment from gymnasium (gym) and it has three problems: Car-Racing-v3, LunarLander-v3, and Humanoid.
   CarRacing-v3 and LunarLander-v3 are from Box2D environment while Humanoid is from MuJoCo environment.
      More details can be found in gym library:
      ```
      https://gymnasium.farama.org/
      ```

   For each of the problem, you are required to write an agent which facilitate to get the optimizaed solutions. In order to be evaluated easily, please use the following template for each 3 problems:
   ```
   #Car Racing Agent
   class CarRaceAgent:
       #initialize the agent, with input of number of actions
       def __init__(self,n_actions: int,):

       #agent takes action, with input indicating current state
       def act(self, state: np.ndarray):

       #agent load parameter (you need to implement this function if you use model based framework such as DQN, PPO, etc)
       def load_parameter(self,qfile):

       #agent save parameter (you need to implement this function if you use model based framework such as DQN, PPO, etc)
       def save_parameter(self,qfile,qtarfile):
   ```

3. Running evaluation script

4. Detailed Rubrics 
