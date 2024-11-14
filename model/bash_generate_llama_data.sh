#  data generation for main results (i.e., Table 1)
for n_shot in 5
do
    for dataset in   proscript schema11  wikihowscript
    do
        for seed in 1 2 3
        do 
            for NoT in 'no' 'CoT'  'NoT' 'GPT4-SR_alphabet-v0' 'GPT4-SR_alphabet-v1' 'GPT4-SR_descriptive-v0' 'GPT4-SR_descriptive-v1'
            do
                python generate_llama_data.py -dataset $dataset -split test_normalized_shuffled  -n_shot ${n_shot} -seed ${seed}  -NoT_demonstation ${NoT}
            done
        done
    done
done


# #  data generation for ablation study: # of shots  (i.e., Figure 3)
# for n_shot in  1 3 10 15
# do
#     for dataset in   proscript schema11  wikihowscript
#     do
#         for seed in 1 2 3
#         do 
#             for NoT in 'no' 'CoT' 'GPT4-SR_descriptive-v0' 'GPT4-SR_descriptive-v1'
#             do
#                 python generate_llama_data.py -dataset $dataset -split test_normalized_shuffled -n_shot ${n_shot} -seed ${seed}  -NoT_demonstation ${NoT}
#             done
#         done
#     done
# done




