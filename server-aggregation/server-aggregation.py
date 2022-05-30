import flwr as fl



def get_on_fit_config_fn():
    """Return a function which returns training configurations."""

    def fit_config(rnd: int):
        """Return a configuration with static batch size and (local) epochs."""
        config = {
            "learning_rate": str(0.001),
            "batch_size": str(32),
        }
        return config

    return fit_config

strategy = fl.server.strategy.FedAvg(
    fraction_fit=1,
    fraction_eval=1,
    min_fit_clients=3,
    min_available_clients=3,
    on_fit_config_fn=get_on_fit_config_fn(),
)
fl.server.start_server(server_address="[::]:8080", config={"num_rounds": 3}, strategy=strategy, grpc_max_message_length=895_870_912)

