import pygame as pg
import gym, gym_gvgai
# import gym_gvgai
import numpy as np




def init_gym_pygame(game_name):
    """
    Initiate OpenAI envirenment and pygame interface with a given game name
    Args:
        game_name (str): the game name available in the OpenAI catalog

    Returns:
        env (gym.make), gym invironment,
        screen (pg.display.set_mode), pygame screen

    """
    # OpenAI gym setup 
    game_name = 'gvgai-aliens-lvl0-v0'
    env = gym.make(game_name)
    env.reset()
    
    # pygame setup
    pg.init()
    height = env.observation_space.shape[0]
    width = env.observation_space.shape[1]
    screen = pg.display.set_mode((width, height))

    return env, screen

def pg_print_state(env, screen):
    """
    Given the openai gym env and screen variable,
    the function takes the state,
    renders and displays the window
    You have to perform all the flips in oder to display the image
    correctly

    Args:
        env (gym.make): gym environment
        screen (pg.display.set_mode): screen from pygame

    Returns:
        None, updates the screen of the pygame

    """

    rgb_state = env.render(mode='rgb_array')
    # rgb_state = rgb_state[:,:,1].T  one color
    rgb_state_transp = np.transpose(rgb_state,(1,0,2))
    screen.blit(pg.surfarray.make_surface(rgb_state_transp), (0,0))
    pg.display.flip()