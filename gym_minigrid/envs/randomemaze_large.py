#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gym_minigrid.minigrid import *
from gym_minigrid.register import register
import numpy as np

class RandomMazeLarge(MiniGridEnv):
    """
    Classic 4 rooms gridworld environment.
    Can specify agent and goal position, if not it set at random.
    """

    def __init__(self, agent_pos=None, goal_pos=None, walls=True):
        self._agent_default_pos = agent_pos
        self._goal_default_pos = goal_pos
        self.walls = walls
        super().__init__(grid_size=50, max_steps=2000)

    def _gen_grid(self, width, height):
        np.random.seed(23)
        # Create the grid
        self.grid = Grid(width, height)

        # Generate the surrounding walls
        self.grid.horz_wall(0, 0)
        self.grid.horz_wall(0, height - 1)
        self.grid.vert_wall(0, 0)
        self.grid.vert_wall(width - 1, 0)

        self.wallss = set()
        if self.walls:
            for y in (13, 14):
                self.grid.vert_wall(y, 0, 38)
                for x in range(38):
                    self.wallss.add((y, x))
            self.grid.horz_wall(0, 32, 5)
            self.grid.horz_wall(0, 31, 5)
            for x in range(0, 5):
                for y in (31, 32):
                    self.wallss.add((x, y))
            self.grid.horz_wall(14, 12, 24)
            self.grid.horz_wall(14, 11, 24)
            for x in range(14, 14 + 24):
                for y in range(11, 13):
                    self.wallss.add((x, y))
            self.grid.horz_wall(19, 24, 24)
            self.grid.horz_wall(19, 23, 24)
            for x in range(19, 19 + 24):
                for y in range(23, 25):
                    self.wallss.add((x, y))
            self.grid.vert_wall(32, 12,12)
            self.grid.vert_wall(31, 12,12)
            for x in (31, 32):
                for y in range(12, 12 + 12):
                    self.wallss.add((x, y))
            self.grid.vert_wall(30, 30,20)
            self.grid.vert_wall(29, 30,20)
            for x in (29, 30):
                for y in range(30, 30 + 20):
                    self.wallss.add((x, y))
            self.grid.vert_wall(43, 23, 12)
            self.grid.vert_wall(42, 23, 12)
            for x in (42, 43):
                for y in range(23, 23 + 12):
                    self.wallss.add((x, y))
        for i in range(12 * 50):
            x = np.random.randint(50)
            y = np.random.randint(50)
            self.wallss.add((x, y))
            self.grid.horz_wall(x, y, 1)
        
        
        if self._agent_default_pos is not None:
            self.agent_pos = self._agent_default_pos
            self.grid.set(*self._agent_default_pos, None)
            self.agent_dir = self._rand_int(0, 4)  # assuming random start direction
        else:
            flag = False
            for a in range(50):
                if flag:
                    break
                for b in range(50):
                    if (a, b) not in self.wallss:
                        self.place_agent((a, b))
                        flag = True
                        break

        if self._goal_default_pos is not None:
            goal = Goal()
            self.put_obj(goal, *self._goal_default_pos)
            goal.init_pos, goal.cur_pos = self._goal_default_pos
        else:
            self.place_obj(Goal())

        self.mission = 'Reach the goal'

    def step(self, action):
        obs, reward, done, info = MiniGridEnv.step(self, action)
        return obs, reward, done, info

register(
    id='MiniGrid-RandomMazeLarge-v0',
    entry_point='gym_minigrid.envs:RandomMazeLarge'
)
