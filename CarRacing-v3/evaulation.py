import gymnasium as gym
from agent import CarRaceAgent
import imageio.v2 as imageio
from env import ImageEnv
import pdb
import torch
import numpy as np
from utils import *

def test(agent,alpha):
    env_v = gym.make("CarRacing-v3", render_mode="rgb_array",domain_randomize=True)
    agent.PPO_Net.load_state_dict(torch.load("param.pt", map_location="cpu"))
    agent.PPO_Net.eval()
    frames = []
    steers = []
    #various test case:
    #out_of_track
    numofftrack=0

    #for _ in range(50):
    state_v, info_v = env_v.reset()

    # play one episode
    done_v = False
    score=0

    while not done_v:
        # select an action A_{t} using S_{t} as input for the agent
        frames.append(env_v.render())
        with torch.no_grad():
            action_v = agent.select_action(state_v[None,:])

        a = action_v.detach().cpu().numpy().squeeze().astype(np.float32)
        a = np.clip(a, [-1.0, 0.0, 0.0], [1.0, 1.0, 1.0])
        steers.append(float(a[0]))

        # perform the action A_{t} in the environment to get S_{t+1} and R_{t+1}
        state_v, reward_v, terminated_v, truncated_v, info_v = env_v.step(action_v.detach().cpu().numpy().squeeze())
        score+=reward_v
        # update if the environment is done
        done_v = terminated_v or truncated_v

    env_v.close()

    #zigzag penalty
    m = zigzag_metrics(steers, deadband=0.5)
    if(m>10):
        print("car zigzags too much")
    else:
        print("car isn't zigzag too much")

    #U turn penalty
    uturn=uturn_metrics(steers,threshold=20)
    if(uturn!=0):
        print("car has U turn")
    else:
        print("car hasn't U turn")

    #test case 4
    halt=is_halted_speed(env_v)
    if(halt!=0):
        print("car halts for long time")
    else:
        print("car isn't halt for long time")

    print("total score is ",score-alpha*halt-alpha*m-alpha*uturn)

