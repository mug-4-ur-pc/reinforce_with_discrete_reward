import hydra


def load_hydra_config(config_dir: str):
    """Load Hydra configuration from a YAML file.

    Args:
        config_dir (str): Path to the directory containing `main.yaml`.
    """
    with hydra.initialize(version_base=None, config_path=config_dir):
        return hydra.compose("main.yaml")
