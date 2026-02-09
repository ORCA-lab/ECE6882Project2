import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import pdb
import argparse


def zigzag_metrics(steers, deadband=0.2):
    s = np.asarray(steers, dtype=np.float32)
    if len(s) < 2:
        return 0

    #pdb.set_trace()
    # Count meaningful sign flips with deadband
    flip = 0
    prev = s[0]
    for x in s[1:]:
        if (prev > deadband and x < -deadband) or (prev < -deadband and x > deadband):
            flip += 1
        prev = x
    return int(flip)/len(s)*100


def uturn_metrics(steers, threshold=20):
    s = np.asarray(steers, dtype=np.float32)
    if len(s) < 2:
        return False

    # Count meaningful sign flips with deadband
    prev = s[0]
    count=0
    for x in s[1:]:
        if(prev<0 and x<0):
            count+=1
        elif(prev<0 and x>0):
            count=0
        elif(prev>0 and x>0):
            count+=1
        else:
            count=0
        prev=x
        if(count>threshold):
            return count
    return count


def is_halted_speed(env, speed_thresh=0.2, k_steps=30):

    if not hasattr(env.unwrapped, "car") or env.unwrapped.car is None:
        return None  # can't measure

    halted_count = 0
    for _ in range(k_steps):
        v = env.unwrapped.car.hull.linearVelocity
        speed = float(np.hypot(v[0], v[1]))
        if speed < speed_thresh:
            halted_count += 1
        else:
            halted_count = 0
        if halted_count >= k_steps:
            return halted_count
    return halted_count
