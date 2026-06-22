import json
import sys

import numpy as np

err = "who eat my"

if "--help" in sys.argv or "-H" in sys.argv:
    print("""stupid neural

        options:
          -H, --help   show this help message and exit
          --path PATH  Path to .config""")
if "--path" in sys.argv:
    index = sys.argv.index("--path")

    try:
        path = sys.argv[index + 1]
        print(f"Path: {path}")  # do action here, now placeholder of sort

    except IndexError:
        print(f"{err}path")

if "--input_test" in sys.argv:
    index = sys.argv.index("--input_test")

    try:
        input_arr = np.array(json.loads(sys.argv[index + 1]), dtype=float)
        print(input_arr)

    except IndexError:
        print(f"{err}input")


with open(path, "r") as f:
    model = json.load(f)
    if len(input_arr) != model["input"]:
        raise ValueError(
            f"Expected {model['input']} inputs, got {len(input_arr)}"
        )
    for layer in model["layers"]:
            
        layer_name = layer["name"]
        layers_neurons_p = layer["neurons"]
        
        layer_bias_p = layer["bias"]
        layer_bias = np.array(layer_bias_p ,dtype=float)
        
        layer_weights_p = layer["weights"]
        layer_weight = np.array(layer_weights_p, dtype=float)

        print(layer_name, layer_bias, layer_weight)
        output = layer_weight @ input_arr + layer_bias
        output = np.tanh(output)

        input_arr = output
        print(output)
        
