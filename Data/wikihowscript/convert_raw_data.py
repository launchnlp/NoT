import json
import numpy as np

np.random.seed(0)

with open("./script_en.json", "r") as file:
    data = json.load(file)

data = data["test"]
new_data = []
for x in data:
    if "steps" in x and x["ordered"]==1:
        # We restrict scenarios to those containing up to 20 steps in this study. This filters out 44 scenarios from the raw data which contains 3,035 scenarios in total.
        if len(x["steps"])<=20:
            new_data.append(x)



data = new_data
print(len(data))

count = 0
with open("./test.jsonl", "w") as file:
    for x in data:
        line = {}
        line["scenario"] = x["title"]
        list_array = list(range(len(x["steps"])))
        np.random.shuffle(list_array)
        line["events"] = {i: t for i, t in zip(list_array,x["steps"]) }
        line["gold_edges_for_prediction"] = [f"{list_array[i]}->{list_array[i+1]}" for i in range(len(list_array)-1)]
        assert len(line["gold_edges_for_prediction"]) == len(line["events"])-1
        
        line["events"] = {str(k): line["events"][k] for k in sorted(line["events"])}

        line["flatten_input_for_edge_prediction"] = "; ".join(["step{k}: {v}".format(k=k,v=v) for k,v in line["events"].items()])
        line["flatten_output_for_edge_prediction"] = "; ".join(["step{} -> step{}".format(x.split("->")[0], x.split("->")[1]) for x in line["gold_edges_for_prediction"]])
        json.dump(line, file)
        file.write("\n")
        count += 1


