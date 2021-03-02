def get_fcnn_parameter_count() -> int:
    """
    Calculate the number of parameters used by the fully connected network.
    Hint: Casting the result of fc_net.parameters() to a list may make it 
          easier to work with

    Returns:
        param_count: The number of parameters in the network
    """

    fc_net = FullyConnectedNet()
    fc_net_parameters = list(fc_net.parameters())
    fc_shape = fc_net_parameters[0].shape

    param_count = fc_shape[0] * fc_shape[1]

    return param_count

print(get_fcnn_parameter_count())
