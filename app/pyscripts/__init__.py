import pygame as pg
from pygame.locals import *
import random
import math
import numpy as np
import csv
import sys
import json
import time

from gui_elements.input_text_box import InputTextBox
from gui_elements.toggle_button import ToggleButton
from gui_elements.button import Button
from gui_elements.textbox import TextBox
from gui_elements.slider import Slider
from gui_elements.colors import *

from particles.particle2D import Particle2D
from environments.environment2D import Environment2D
from environments.environment1D import Environment1D
from environments.gas_environment import GasEnvironment
from environments.question_environment import QuestionEnvironment
from environments.test_environment import TestEnvironment
from manage_users.registration.reg_env import RegEnvironment
from manage_users.login.login_env import LoginEnvironment
from environments.__init__ import colorOrder

pg.init()

# define screen dimensions
monitor_size = [pg.display.Info().current_w, pg.display.Info().current_h]

(width, height) = (monitor_size[0]*3/4, monitor_size[1]*(3/4))

screen = pg.display.set_mode((width, height), HWSURFACE|RESIZABLE)

pg.display.set_caption("Collision simulator")

ENV2D_MAX_PARTICLES = 4
ENV1D_MAX_PARTICLES = 2
GASENV_MAX_PARTICLES = 150










