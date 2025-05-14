import gym
import gym_agario  # Make sure AgarioEnv is registered

env = gym.make("agario-grid-v0")  # or your actual ID
num_episodes = 50
episode_lengths = []
episode_rewards = []

for i in range(num_episodes):
    obs, info = env.reset()
    done = False
    total_reward = 0
    steps = 0

    while not done:
        action = env.action_space.sample()
        obs, reward, terminated, truncated, info = env.step(action)
        done = terminated or truncated
        total_reward += reward
        steps += 1

    episode_lengths.append(steps)
    episode_rewards.append(total_reward)
    print(f"Episode {i+1}: length={steps}, total_reward={total_reward}, info={info}")

print("\n--- Summary ---")
print(f"Average Episode Length: {sum(episode_lengths) / num_episodes}")
print(f"Average Total Reward: {sum(episode_rewards) / num_episodes}")
# import gym
# import gym_agario

# env = gym.make("agario-grid-v0")  # or whatever the registered ID is
# episode_lengths = []
# rewards = []

# for i in range(50):
#     obs = env.reset()
#     done = False
#     steps = 0
#     total_reward = 0
#     while not done:
#         action = env.action_space.sample()
#         obs, reward, done, info = env.step(action)
#         steps += 1
#         total_reward += reward
#     episode_lengths.append(steps)
#     rewards.append(total_reward)
#     print(f"Episode {i+1} — Length: {steps}, Reward: {total_reward}")

# print("\nAverage Length:", sum(episode_lengths)/len(episode_lengths))
# print("Average Reward:", sum(rewards)/len(rewards))