# Models & Experiments
This section documents how to run our repo and reproduce numbers reported in our paper.

## Run
```
bash bash_generate_llama_data.sh
bash NoT_experiment_bash.sh
bash bash_process_llama_outputs.sh
```
By running the script above, you can reproduce our major results (i.e., Table 1).

*We are still checking the executability of this repo!!!

### Figure 3 (the impact of the number of shots)
In order to produce results for Figure 3 (i.e., the impact of the number of shots), comment out the first block in both ```bash_generate_llama_data.sh``` and ```bash_process_llama_outputs.sh```, and uncomment the second block. Then, update the remaining bash file correspondingly.

### About the usage of NoT parameter
In almost all bash and python files, you can see the usage of ```NoT``` parameters (or its equivalence, ```NoT_demonstation```). This argument specifies different inference-time prompting setting (i.e., standard prompting vs. chain-of-thought vs. narrative-of-thought).

For this argument, it supports the following values:
```
'no', 'CoT', 'NoT'
'GPT35-NR_alphabet-v0', 'GPT35-NR_alphabet-v1', 'GPT35-SE_alphabet-v0', 'GPT35-SE_alphabet-v1', 'GPT35-RP_alphabet-v0', 'GPT35-RP_alphabet-v1',  'GPT35-SR_alphabet-v0', 'GPT35-SR_alphabet-v1'
'GPT35-NR_descriptive-v0', 'GPT35-NR_descriptive-v1', 'GPT35-SE_descriptive-v0', 'GPT35-SE_descriptive-v1', 'GPT35-RP_descriptive-v0', 'GPT35-RP_descriptive-v1',  'GPT35-SR_descriptive-v0', 'GPT35-SR_descriptive-v1'
'GPT4-NR_alphabet-v0', 'GPT4-NR_alphabet-v1', 'GPT4-SE_alphabet-v0', 'GPT4-SE_alphabet-v1', 'GPT4-RP_alphabet-v0', 'GPT4-RP_alphabet-v1',  'GPT4-SR_alphabet-v0', 'GPT4-SR_alphabet-v1'
'GPT4-NR_descriptive-v0', 'GPT4-NR_descriptive-v1', 'GPT4-SE_descriptive-v0', 'GPT4-SE_descriptive-v1', 'GPT4-RP_descriptive-v0', 'GPT4-RP_descriptive-v1',  'GPT4-SR_descriptive-v0', 'GPT4-SR_descriptive-v1'
```

*For more details of different demonstrations used in our study, when NoT is enabled, please check out our paper and the [prompts](./prompts) folder.

### Note:
We find that models are sometimes sensitive to the inlcusion/omission of quotes (') in the demonstrations. To keep our results fully transparent, we open-source both prompts. We invite the community to delve into this aspect in their future studies. 

In our paper, due to space limit, we report the better performance between these two.