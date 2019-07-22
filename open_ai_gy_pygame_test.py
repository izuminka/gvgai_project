#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 19:24:55 2019

@author: pavel
"""

import time

import gym
# import gym_gvgai

import pygame as pg


def pg_print_state(env, screen):
    """
    Given the openai gym env and screen variable,
    the function takes the state,
    renders and displays the window
    You have to perform all the flips in oder to display the image
    correctly
    """
    rgb_state = env.render(mode='rgb_array')
    rgb_state_transp = np.transpose(rgb_state,(1,0,2))
#    rgb_state = rgb_state[:,:,1].T  one color
    screen.blit(pg.surfarray.make_surface(rgb_state_transp), (0,0))
    pg.display.flip()


env = gym.make('gvgai-aliens-lvl0-v0')
env.reset()
time.sleep(5)

pg.init()
height = env.observation_space.shape[0]
width = env.observation_space.shape[1]
screen = pg.display.set_mode((width, height))

import numpy as np

while True:
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            sys.exit()
#        if event.type == pygame.KEYDOWN:            
            action_id = env.action_space.sample()
            state, reward, isOver, debug = env.step(action_id)
            pg_print_state(env, screen)
        
            time.sleep(0.1)

