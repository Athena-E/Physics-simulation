import pygame as pg
from pygame.locals import *
import random
import math
import numpy as np
from itertools import combinations

pg.init()

# color gradient from blue -> red for gas particles
colorGradient = (
(42, 139, 249),
(91, 133, 247),
(122, 126, 242),
(148, 118, 235),
(170, 110, 226),
(189, 101, 215),
(205, 91, 202),
(219, 81, 187),
(230, 72, 172),
(239, 63, 155),
(245, 56, 138),
(248, 53, 120),
(249, 53, 102),
(248, 58, 83),
(244, 65, 65)
)


