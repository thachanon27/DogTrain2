from gym.envs.registration import (
    registry,
    register,
    make,
    spec,
    load_env_plugins as _load_env_plugins,
)

# Hook to load plugins from entry points
_load_env_plugins()


# Classic
# ----------------------------------------

register(
    id="dog-v0",
    entry_point="gym.envs.dog_train_env:DogEnv",
    max_episode_steps=200,
    reward_threshold=195.0,
)


