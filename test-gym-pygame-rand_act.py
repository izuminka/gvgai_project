#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 19:24:55 2019

@author: pavel
"""

import time
from common_funs import init_gym_pygame, pg_print_state

SLEEP_RATE = 0.1
game_name = 'gvgai-aliens-lvl0-v0'
env, screen = init_gym_pygame(game_name)

while True:
    action_id = env.action_space.sample()
    state, reward, isOver, debug = env.step(action_id)
    pg_print_state(env, screen)
    time.sleep(SLEEP_RATE)

