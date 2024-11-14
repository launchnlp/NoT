
# for main results  (i.e., Table 1)
for output in  schema11 proscript  wikihowscript
do
    for seed in 1 2 3
    do
        for model in    google/gemma-7b-it meta-llama/Meta-Llama-3-8B-Instruct mistralai/Mistral-7B-Instruct-v0.2 
        do
            for NoT in 'CoT'  'NoT' 'GPT4-SR_alphabet-v0' 'GPT4-SR_alphabet-v1' 'GPT4-SR_descriptive-v0' 'GPT4-SR_descriptive-v1'
            do 
                for output_dir in  ${model}/${output}_test_normalized_shuffled-${NoT}_5shots_${seed} 
                do
                    python process_llama_output.py -output_dir ${output_dir} 
                done
            done
            # for standard prompting (the next line)
            python process_llama_output.py -output_dir ${model}/${output}_test_normalized_shuffled_5shots_${seed}
        done
    done
done


# for ablation 1: number of shots  (i.e., Figure 3)
for output in schema11 proscript  wikihowscript
do
    for seed in 1 2 3
    do
        for model in   meta-llama/Meta-Llama-3-8B-Instruct 
        do
            for NoT in 'CoT'  'NoT'  'GPT4-SR_descriptive-v0' 'GPT4-SR_descriptive-v1'
            do 
                for n_shot in 1 3 10 15
                do
                    for output_dir in  ${model}/${output}_test_normalized_shuffled-${NoT}_${n_shot}shots_${seed} 
                    do
                        python process_llama_output.py -output_dir ${output_dir} 
                    done
                    # for standard prompting (the next line)
                    python process_llama_output.py -output_dir ${model}/${output}_test_normalized_shuffled_${n_shot}shots_${seed}
                done
            done
        done
    done
done
