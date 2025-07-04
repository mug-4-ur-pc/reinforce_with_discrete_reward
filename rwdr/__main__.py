import sys

import fire
from omegaconf import DictConfig

from rwdr.setup import setup_data
from rwdr.utils import load_hydra_config


def setup_wrapper(config_dir: DictConfig = "../config"):
    """Download and prepare data using Hydra configuration.

    Args:
        config_dir (str): Configuration directory path (default: '../conf').
    """
    cfg = load_hydra_config(config_dir)
    setup_data(cfg)


def main():
    """CLI for training.

    Commands:
        setup : Download and prepare data.
    """
    commands = {
        "setup": setup_wrapper,
    }
    try:
        fire.Fire(commands)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
        sys.exit(1)


if __name__ == "__main__":
    main()
