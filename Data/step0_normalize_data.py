import json

# map number to alphabet
def num_to_alpha(num):
    return chr(num+65)


for dataset_name in ["proscript", "schema11", "wikihowscript"]:
    with open ("./{}/test.jsonl".format(dataset_name), "r") as file, open ("./{}/test_normalized.jsonl".format(dataset_name), "w") as file_write:
        datas = [json.loads(line) for line in file]
        for data in datas:
            data["events"] = {num_to_alpha(int(k)): v for k,v in data["events"].items()}
            for x in data["events"]:
                if data["events"][x] == "NONE":
                    data["events"][x] = "decide to " +  data["scenario"]
            data["gold_edges_for_prediction"] = [f"{num_to_alpha(int(x.split('->')[0]))}->{num_to_alpha(int(x.split('->')[1]))}" for x in data["gold_edges_for_prediction"]]
            data["flatten_input_for_edge_prediction"] = "; ".join(["step{k}: {v}".format(k=k,v=v) for k,v in data["events"].items()])
            data["flatten_output_for_edge_prediction"] = "; ".join(["step{} -> step{}".format(x.split("->")[0], x.split("->")[1]) for x in data["gold_edges_for_prediction"]])

            json.dump(data, file_write)
            file_write.write("\n")