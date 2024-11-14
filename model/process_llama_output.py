import re
import json
import argparse

from utils import*

# specify command-line options
parser = argparse.ArgumentParser()
parser.add_argument('-output_dir')
args = parser.parse_args()

HM_PATH = "/data/frederick"   # change this line to your specified path to NoT repository.

output_data = []
pattern = r'step([A-Z]) -> step([A-Z])'


with open(HM_PATH+"/script_learning/tmp_output/{}/generated_predictions.jsonl".format(args.output_dir), "r") as f:
    data = f.readlines()
    for line in data:
        json_object = json.loads(line)

        gt_edges = [x.strip() for x in json_object["label"].split(";")]
        response = json_object["predict"]
        response = parse_response(response)

        # further cleaning
        clean_response = []
        for x in response:
            match = re.findall(pattern,x)
            if len(match)==1:
                match = match[0]
                clean_response.append("step{} -> step{}".format(match[0], match[1]))

        output_data.append({"gt": gt_edges, "generation":clean_response})


with open(HM_PATH+"/script_learning/outputs_llama/{}.jsonl".format(args.output_dir.replace("/","_")), "w") as file_write:
    for data in output_data:
        json.dump(data, file_write)
        file_write.write('\n')