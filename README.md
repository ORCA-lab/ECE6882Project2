# Welcome to ECE6882 Reinforcement Learning Project 2 Repo


1. Description and tasks of project:
   
      This project used environment from gymnasium (gym) and it has three problems: Car-Racing-v3, LunarLander-v3, and Humanoid.
   CarRacing-v3 and LunarLander-v3 are from Box2D environment while Humanoid is from MuJoCo environment.
      More details can be found in gym library:
      ```
      https://gymnasium.farama.org/
      ```

   For each of the problem, you are required to write an agent to get the optimizaed solutions. In order to be evaluated easily, please use the following template for each 3 problems and finish those functions:
   ```
   #Agent class:
   class xxxAgent:
       #initialize the agent, with input of number of actions
       def __init__(self,n_actions: int,):

       #agent takes action, with input indicating current state
       #important !!! don't change this function name
       def act(self, state: np.ndarray):

       #agent load parameter (you need to implement this function if you use model based framework such as DQN, PPO, etc)
       def load_parameter(self,file):
   ```
   The agent function names should be: CarRace-v3: CarRaceAgent, LunarLander-v3: LunarLanderAgent, Humanoid: HumanoidAgent
   
   Besides the required functions listed above, you can implement other functions inside the agent class as you wish.
   
   **For CarRaceAgent, if you would like to define a wrapper of the environment to better fit into your agent, please finish the following classes in xxx.py:**
   ```
   def make_env(render_mode=None):
   ```

3. Running evaluation script:

   I provided **two sample testcases** for each problems to help you verify your agent functionalities and improve your agent performance. However, the eventual official scores for each problems will be tested more cases besides these two. In order to make the evaluation fair, please don't change the testcases by yourself.
   To run the evaluation, simply run the following command for each agent. 
   ```
   python evaluation.py
   ```
   It will output the scores for each testcase. 

4. Rubrics for each agent:

   The overal score are composed of the **mean** of original returns from 8 test cases where 2 of them are released for you for reference, other 6 test cases are hidden for final scores. This score will be used for ranking among all teams.

5. Submission of problems:

   For each problem, First, change the file "xxx.py" into your own group name, for example "Henry.py" with the group name "Henry". Next, put both **evaluation.py**, **{groupname}.py** and your **training parameter** into a folder "{groupname}_project2" and compress it as "{groupname}_project2.zip", then submit that file into the following link: https://docs.google.com/forms/d/e/1FAIpQLSevo4xUkgtBl3whhFJzD5qNL_C4yFytgyyy4W-gMaPv9bpzFw/viewform?usp=dialog

# LeaderBoard

1. Car Racing
<table>
     <thead>
       <tr>
         <th style="width:30%">Team</th>
         <th style="width:70%">Score</th>
       </tr>
     </thead>
     <tbody>
        <tr>
         <td>
           <code>Hajimi</code>
         </td>
         <td>
           <code>829.71</code>
         </td>
       </tr>
       <tr>
         <td>
           <code>JAC</code>
         </td>
         <td>
           <code>758.51</code>
         </td>
       </tr>
        <tr>
           <td>
           <code>Ziyuan_Zhou901</code>
           </td>
           <td>
           <code>717.33</code>
           </td>
        </tr>
         <tr>
           <td>
           <code>Desi_Reinforcement</code>
           </td>
           <td>
           <code>565.95</code>
           </td>
        </tr>
        <tr>
           <td>
           <code>Vu_Dao</code>
           </td>
           <td>
           <code>484.89</code>
           </td>
        </tr>
        <tr>
           <td>
           <code>Jani</code>
           </td>
           <td>
           <code>238.77</code>
           </td>
        </tr>
        <tr>
           <td>
           <code>Arante_Andre</code>
           </td>
           <td>
           <code>207.49</code>
           </td>
        </tr>
     </tbody>
   </table>
2. LunarLander
<table>
     <thead>
       <tr>
         <th style="width:30%">Team</th>
         <th style="width:70%">Score</th>
       </tr>
     </thead>
     <tbody>
       <tr>
         <td>
           <code>JAC</code>
         </td>
         <td>
           <code>242.35</code>
         </td>
       </tr>
        <tr>
           <td>
           <code>Arante_Andre</code>
           </td>
           <td>
           <code>193.93</code>
           </td>
        </tr>
        <tr>
         <td>
           <code>Hajimi</code>
         </td>
         <td>
           <code>169.89</code>
         </td>
       </tr>
         <tr>
           <td>
           <code>Ziyuan_Zhou901</code>
           </td>
           <td>
           <code>161.63</code>
           </td>
        </tr>
        <tr>
           <td>
           <code>Desi_reinforcement</code>
           </td>
           <td>
           <code>159.16</code>
           </td>
        </tr>
        <tr>
           <td>
           <code>Vu_Dao</code>
           </td>
           <td>
           <code>147.92</code>
           </td>
        </tr>
        <tr>
           <td>
           <code>Jani</code>
           </td>
           <td>
           <code>146.09</code>
           </td>
        </tr>
     </tbody>
   </table>
3. Humanoid
<table>
     <thead>
       <tr>
         <th style="width:30%">Team</th>
         <th style="width:70%">Score</th>
       </tr>
     </thead>
     <tbody>
       <tr>
         <td>
           <code>JAC</code>
         </td>
         <td>
           <code>7854.19</code>
         </td>
       </tr>
        <tr>
           <td>
           <code>Ziyuan_Zhou901</code>
           </td>
           <td>
           <code>5973.70</code>
           </td>
        </tr>
        <tr>
         <td>
           <code>Arante_Andre</code>
         </td>
         <td>
           <code>5775.82</code>
         </td>
       </tr>
         <tr>
           <td>
           <code>Desi_reinforcement</code>
           </td>
           <td>
           <code>5473.13</code>
           </td>
        </tr>
        <tr>
           <td>
           <code>Hajimi</code>
           </td>
           <td>
           <code>5029.13</code>
           </td>
        </tr>
        <tr>
           <td>
           <code>Vu_Dao</code>
           </td>
           <td>
           <code>4494.77</code>
           </td>
        </tr>
        <tr>
           <td>
           <code>Jani</code>
           </td>
           <td>
           <code>365.66</code>
           </td>
        </tr>
     </tbody>
   </table>

