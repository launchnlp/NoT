import json
import random

for dataset_name in ["proscript", "schema11", "wikihowscript"]:
    for SEED in range(1, 4):
        random.seed(SEED)

        with open ("./{}/test_normalized.jsonl".format(dataset_name), "r") as file, open ("./{}/test_normalized_shuffled_{}.jsonl".format(dataset_name, SEED), "w") as file_write:
            datas = [json.loads(line) for line in file]
            for data in datas:
                # shuffle data["events"]
                tmp = list(data["events"].items())
                random.shuffle(tmp)
                data["events"] = dict(tmp)

                json.dump(data, file_write)
                file_write.write("\n")