#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 19:24:55 2019

@author: pavel
"""

from common_funs import init_gym_pygame, pg_print_state
import sys
import pygame as pg


game_name = 'gvgai-aliens-lvl0-v0'
env, screen = init_gym_pygame(game_name)
# convert pg.event.key format to ASCII for 0..9
dict_pygame_ascii = {48+i:i for i in range(10)} 


# Create the step by step game play.
# The game only progresses only if the key is pressed
while True:
    # input stream input
    for event in pg.event.get():
        # check that the input is from the keyboard
        if event.type == pg.KEYDOWN:
            # ESC is pressed exit the code
            if event.key == pg.K_ESCAPE:
                sys.exit()
            # choose an action in the action range, other than null
            if event.key in dict_pygame_ascii:
                action_id = dict_pygame_ascii[event.key]
                if action_id in range(env.action_space.n):
                    state, reward, isOver, debug = env.step(action_id)
                    pg_print_state(env, screen)


