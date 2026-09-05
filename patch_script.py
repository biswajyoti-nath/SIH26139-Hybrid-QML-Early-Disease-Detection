with open("scripts/run_complexity_benchmark.py", "r") as f:
    text = f.read()

text = text.replace(
'''                    if model_name == "vqc":
                        model = ModelFactory.create(
                            "vqc", 
                            random_state=seed, 
                            n_qubits=vqc_config["n_qubits"],
                            n_layers=vqc_config["n_layers"],
                            loss_fn=vqc_config["loss_fn"],
                            iterations=vqc_config["iterations"],
                            learning_rate=vqc_config["learning_rate"]
                        )
                    else:
                        model = ModelFactory.create(model_name, random_state=seed)''',
'''                    if model_name == "vqc":
                        model = ModelFactory.create_classical_model("vqc", {
                            "random_state": seed,
                            "n_qubits": vqc_config["n_qubits"],
                            "n_layers": vqc_config["n_layers"],
                            "loss_fn": vqc_config["loss_fn"],
                            "iterations": vqc_config["iterations"],
                            "learning_rate": vqc_config["learning_rate"]
                        })
                    else:
                        model = ModelFactory.create_classical_model(model_name, {"random_state": seed})'''
)

with open("scripts/run_complexity_benchmark.py", "w") as f:
    f.write(text)
