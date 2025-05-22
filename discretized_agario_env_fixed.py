
import gym
import numpy as np
import itertools
from gym import spaces

class DiscretizedAgarioEnv(gym.Env):
    def __init__(self):
        super().__init__()
        self.base_env = gym.make("agario-grid-v0")

        # Discretize x and y in [-5, ..., 5] and combine with action_type ∈ {0, 1, 2}
        self.motion_vals = list(range(-5, 6))  # 11 values
        self.action_types = [0, 1, 2]  # do nothing, split, feed
        self.actions = list(itertools.product(self.motion_vals, self.motion_vals, self.action_types))
        self.action_space = spaces.Discrete(len(self.actions))  # how large the action space is: 11*11*3 = 363

        # CNN-compatible observation
        obs = self.reset()
        shape = obs.shape
        self.observation_space = spaces.Box(low=0.0, high=1.0, shape=shape, dtype=np.float32)

    def reset(self):
        obs = self.base_env.reset()
        return self._scale_obs(obs)

    def step(self, action_idx):
        dx, dy, act = self.actions[action_idx]
        direction = np.array([dx, dy], dtype=np.float32)
        norm = np.linalg.norm(direction)
        if norm > 1:
            direction = direction / norm
        obs, reward, done, info = self.base_env.step((direction, act))
        return self._scale_obs(obs), reward, done, info

    def _scale_obs(self, obs):
        return obs.astype(np.float32) / 255.0 # not sure what value to scale by, assume RBG numbers

    def render(self, mode="human"):
        self.base_env.render(mode=mode)

    def close(self):
        self.base_env.close()
