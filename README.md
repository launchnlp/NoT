# Narrative-of-Thought (NoT)
Codebase for "NARRATIVE-OF-THOUGHT: Improving Temporal Reasoning of Large Language Models via Recounted Narratives"

## Introduction
This repository contains codes and datasets for paper ["Narrative-of-Thought: Improving Temporal Reasoning of Large Language Models via Recounted Narratives"](https://aclanthology.org/2024.findings-emnlp.963/) (In <em>Findings of the Association for Computational Linguistics: EMNLP 2024</em>).


## Set up
Run the following commands to clone the repository.
```shell script
$ git clone https://github.com/launchnlp/NoT.git
```

Before running our codes, please run the following script to have all dependencies set up.
```shell script
$ bash requirements.sh
```

*Our codebased is built on top of Llama-Factory. However, you are welcome to reproduce our work without relying on Llama-Factory, as the core methodology lies in the **Narrative-of-Thought**, which can be implemented by creating an inference loop using Huggingface alone.

## Data 
See [Data directory](./Data/) for more information about how to download and process datasets.

## Experiments
See [model directory](./model/) for more information about how to run this repo.

For the usgae of propriertary LLMs (e.g., GPT-3.5/4), you may set up by yourselves.

## Citation
Please cite our paper if you use our **codes** and/or processed data:
```
@inproceedings{zhang-etal-2024-narrative,
    title = "Narrative-of-Thought: Improving Temporal Reasoning of Large Language Models via Recounted Narratives",
    author = "Zhang, Xinliang Frederick  and
      Beauchamp, Nicholas  and
      Wang, Lu",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2024",
    month = nov,
    year = "2024",
    address = "Miami, Florida, USA",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2024.findings-emnlp.963",
    pages = "16507--16530",
}
```