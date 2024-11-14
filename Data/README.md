# Datasets
This section details the necessary steps to process the three datasets used in our work. We convert all datasets into [ProScript](https://aclanthology.org/2021.findings-emnlp.184.pdf) format.

## ProScript
```
wget https://storage.googleapis.com/ai2-mosaic-public/projects/proscript/proscript_v1a.zip
unzip proscript_v1a.zip 
mv proscript_v1a proscript
rm proscript_v1a.zip
```

## Schema-11
To download the raw data, please visit the [original github repo](https://github.com/CogComp/Zero_Shot_Schema_Induction). 

In reference to the original version, we manually re-annotate event temporal graphs for each of the 11 scenarios. The re-annotated version can be found [here](./schema11/test_raw.json).

To process the raw data into desired format, run the following script:
```
cd schema11
python convert_raw_data.py
cd ../
```

## WikiHow Script
Download original data from [here](https://github.com/veronica320/wikihow-GOSC?tab=readme-ov-file). Extract the file **script_en** from the zipped file and put it under [wikihowscript](./wikihowscript).
```
cd wikihowscript
python convert_raw_data.py
cd ../
```

## Data Processing
```
python step0_normalize_data.py 
python step1_shuffle_normalized_data.py 
```

## Dataset statistics

|               | #scenarios | #events | Max #events | #temporal links | Event length | %Non-linear | Domain |
|---------------|------------|---------|-------------|-----------------|--------------|-------------|--------|
| ProScrpt  | 2,077      | 7.46    | 9           | 6.95            | 4.64         | 39%         | Daily   |
| Schema-11      | 11         | 7.91    | 11          | 7.18            | 3.48         | 27%         | News    |
| WikiHow Script  | 2,991        | 8.37    | 20          | 7.37            | 9.63         | 0%          | Daily   |