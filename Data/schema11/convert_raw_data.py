import json
import numpy as np

np.random.seed(0)

with open("./test_raw.json", "r") as file:
    data = json.load(file)

with open("./test.jsonl", "w") as file:
    for line in data:

        list_array = list(range(len(line["events"])))
        np.random.shuffle(list_array)
        line["events"] = {i: line["events"][t] for i, t in zip(list_array,line["events"]) }
        line["gold_edges_for_prediction"] = [f"{list_array[int(x.split('->')[0])]}->{list_array[int(x.split('->')[1])]}" for x in line["gold_edges_for_prediction"]]

        line["events"] = {str(k): line["events"][k] for k in sorted(line["events"])}

        line["flatten_input_for_edge_prediction"] = "; ".join(["step{k}: {v}".format(k=k,v=v) for k,v in line["events"].items()])
        line["flatten_output_for_edge_prediction"] = "; ".join(["step{} -> step{}".format(x.split("->")[0], x.split("->")[1]) for x in line["gold_edges_for_prediction"]])
        json.dump(line, file)
        file.write("\n")