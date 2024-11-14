import json
import argparse

from utils import*

HM_PATH = "/data/frederick"  # change this line to your specified path to NoT repository.

# specify command-line options
parser = argparse.ArgumentParser()
parser.add_argument('-dataset', choices=['proscript', 'schema11', "wikihowscript"])
parser.add_argument('-split', choices=['test_normalized_shuffled'], default='test_normalized_shuffled')
parser.add_argument('-n_shot')
parser.add_argument('-seed')
parser.add_argument('-NoT_demonstation', choices=['no', 'CoT', 'NoT',
                                                  'GPT35-NR_alphabet-v0', 'GPT35-NR_alphabet-v1', 'GPT35-SE_alphabet-v0', 'GPT35-SE_alphabet-v1', 'GPT35-RP_alphabet-v0', 'GPT35-RP_alphabet-v1',  'GPT35-SR_alphabet-v0', 'GPT35-SR_alphabet-v1',
                                                  'GPT35-NR_descriptive-v0', 'GPT35-NR_descriptive-v1', 'GPT35-SE_descriptive-v0', 'GPT35-SE_descriptive-v1', 'GPT35-RP_descriptive-v0', 'GPT35-RP_descriptive-v1',  'GPT35-SR_descriptive-v0', 'GPT35-SR_descriptive-v1',
                                                  'GPT4-NR_alphabet-v0', 'GPT4-NR_alphabet-v1', 'GPT4-SE_alphabet-v0', 'GPT4-SE_alphabet-v1', 'GPT4-RP_alphabet-v0', 'GPT4-RP_alphabet-v1',  'GPT4-SR_alphabet-v0', 'GPT4-SR_alphabet-v1',
                                                  'GPT4-NR_descriptive-v0', 'GPT4-NR_descriptive-v1', 'GPT4-SE_descriptive-v0', 'GPT4-SE_descriptive-v1', 'GPT4-RP_descriptive-v0', 'GPT4-RP_descriptive-v1',  'GPT4-SR_descriptive-v0', 'GPT4-SR_descriptive-v1'
                                                   ], default='no')

args = parser.parse_args()

camelCase = False

if 'GPT' in args.NoT_demonstation:
    demonstration_path = HM_PATH+"/script_learning/model/prompts/demonstrations+" + args.NoT_demonstation  + ".txt"

# initialize instructions based on NoT status
if args.NoT_demonstation == "no":
    Instruction = "*** Complete the class \"{scenario}\" by implementing \"get_relations()\" function marked by #TODO. You should *ONLY* implement the function \"get_relations()\" and not generate anything else. Don't generate the entire class \"{scenario}\". Don't generate comments. Your response must end in \"# END\".\n\n"
    demonstration_instruction = "*** You are first given a set of demonstrations of how to implement the \"get_relations()\" function for different classes.\n\n"
else:
    Instruction = "*** Complete the class \"{scenario}\" by implementing \"get_narrative()\" and \"get_relations()\" functions marked by #TODO. \"get_narrative()\" serves as an auxiliary function facilitating the temporal cohesion of events. Essentially, it helps ensure the temporal accuracy of the predicted temporal graph produced in \"get_relations()\", by explicitly constructing a coherent, temporally correct story involving all provided events.\nYou should *ONLY* implement the function \"get_narrative()\" and \"get_relations()\", but not generate anything else. Don't generate the entire class \"{scenario}\". Don't generate comments. Your response must end in \"# END\".\n\n"
    demonstration_instruction = "*** You are first given a set of demonstrations of how to implement the \"get_narrative()\" and \"get_relations()\" functions for different classes.\n\n"

demonstration = read_demonstration(demonstration_path)
demonstration = sample_demonstrations(demonstration, int(args.n_shot))


write_data = []

with open (HM_PATH+"/script_learning/data/{}/{}_{}.jsonl".format(args.dataset, args.split, args.seed), "r") as f:
    data = f.readlines()
    for line in data:
        json_object = json.loads(line)
    
        scenario = json_object["scenario"]
        scenario_CamelCase= "".join([x.capitalize() for x in scenario.split()])
        events = json_object["events"]

        instruction =  Instruction.format(scenario=scenario_CamelCase) + demonstration_instruction
        
        input_ = Instruction.format(scenario=scenario_CamelCase)

        if args.NoT_demonstation == "no":
            input_ += convert_data_to_program(scenario, events, camelCase)
        elif args.NoT_demonstation == "CoT":
            input_ += convert_data_to_program_CoT(scenario, events, camelCase)
        else:
            input_ += convert_data_to_program_NoT(scenario, events, camelCase)

        # gt_edges = [x.strip() for x in json_object["flatten_output_for_edge_prediction"].split(";")]
        gt_edges = json_object["flatten_output_for_edge_prediction"]

        if "train" in args.split:
            gt_edges = "    def get_relations(self):\n        return [\n            \"" + "\",\n            \"".join([x.strip() for x in gt_edges.split(";")]) + "\",\n        ]\n# END"
    
        tmp_data= {"instruction": instruction, "input": input_, "output": gt_edges}
        
        write_data.append(tmp_data)


with open(HM_PATH+"/LLaMA-Factory/data/dataset_info.json", "r") as f:
    dataset_info = json.load(f)

if args.NoT_demonstation == "no":   
    output_name = "{}_{}_{}shots_{}".format(args.dataset, args.split, args.n_shot, args.seed)
else:
    output_name = "{}_{}-{}_{}shots_{}".format(args.dataset, args.split, args.NoT_demonstation, args.n_shot, args.seed)

COLUMN_PATTERN = {
    "prompt": "instruction",
    "query": "input",
    "response": "output",
    "system": "",
    "history": "history"
  }

with open(HM_PATH+"/data_llama/{}.json".format(output_name), "w") as file_write:
    json.dump(write_data, file_write, indent=4)
dataset_info[output_name] = {"file_name":HM_PATH+"/data_llama/{}.json".format(output_name)}

with open(HM_PATH+"/LLaMA-Factory/data/dataset_info.json", "w") as f:
    json.dump(dataset_info, f, indent=4)