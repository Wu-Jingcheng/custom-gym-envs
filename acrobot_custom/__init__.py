# import acrobot_custom
from gym.envs.registration import make, register, registry, spec

register(
    id='AcrobotCustom-v0',
    entry_point='acrobot_custom.envs:AcrobotCustomEnv',
    max_episode_steps=500
)