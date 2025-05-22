
import gym
import numpy as np
import gym_agario  # ensure environment is registered

# Configurable parameters
env_id = "agario-grid-v0"
num_episodes = 10
max_steps = 1000

env = gym.make(env_id)

# only uncomment to use discrete action space instead of continuous
# from discretized_agario_env_fixed import DiscretizedAgarioEnv
# env = DiscretizedAgarioEnv()

episode_lengths = []
episode_rewards = []

for ep in range(num_episodes):
    obs = env.reset()
    done = False
    total_reward = 0
    steps = 0

    while not done and steps < max_steps:
        # continuous action sampling for learning
        move = np.random.uniform(-1, 1, size=(2,)).astype(np.float32)
        action = np.random.choice(3)
        obs, reward, done, info = env.step((move, 0)) # if hardcoded to zero, then it's always do nothing, i.e. no split or feed; can change 0 to action
        
        # uncomment chunk to use discrete action space instead of continuous
        # discretize move --> totally discrete action space, defined in discretized_agario_env_fixed.py
        # action = env.action_space.sample()
        # obs, reward, done, info = env.step(action) 

        total_reward += reward
        steps += 1

    episode_lengths.append(steps)
    episode_rewards.append(total_reward)
    print(f"Episode {ep+1}: Steps = {steps}, Total Reward = {total_reward:.2f}")

env.close()

print("\nSummary over", num_episodes, "episodes:")
print("Avg steps:", np.mean(episode_lengths))
print("Avg reward:", np.mean(episode_rewards))