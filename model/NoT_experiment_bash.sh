export TRANSFORMERS_CACHE=/data/shared_model/huggingface
export CUDA_DEVICE_ORDER=PCI_BUS_ID
cd ../LLaMA-Factory

declare -A lookup_dict

lookup_dict["google/gemma-7b-it"]="gemma"
lookup_dict["mistralai/Mistral-7B-Instruct-v0.2"]="mistral"
lookup_dict["meta-llama/Meta-Llama-3-8B-Instruct"]="llama3"

for model in google/gemma-7b-it mistralai/Mistral-7B-Instruct-v0.2  meta-llama/Meta-Llama-3-8B-Instruct  
do
    for seed in 1 2 3 
    do
        for NoT in 'CoT' 'NoT'  'GPT4-SR_alphabet-v0' 'GPT4-SR_alphabet-v1'  'GPT4-SR_descriptive-v0' 'GPT4-SR_descriptive-v1'
        # Meanwhile, for NoT arguments, we also support the following values. Yet, in order to achieve this, make sure you make changes to bash_generate_llama_data.sh accordingly
        # for NoT in 'GPT35-NR_alphabet-v0' 'GPT35-NR_alphabet-v1' 'GPT35-SE_alphabet-v0' 'GPT35-SE_alphabet-v1' 'GPT35-RP_alphabet-v0' 'GPT35-RP_alphabet-v1'  'GPT35-SR_alphabet-v0' 'GPT35-SR_alphabet-v1'
        # for NoT in 'GPT35-NR_descriptive-v0' 'GPT35-NR_descriptive-v1' 'GPT35-SE_descriptive-v0' 'GPT35-SE_descriptive-v1' 'GPT35-RP_descriptive-v0' 'GPT35-RP_descriptive-v1'  'GPT35-SR_descriptive-v0' 'GPT35-SR_descriptive-v1'
        # for NoT in 'GPT4-NR_alphabet-v0' 'GPT4-NR_alphabet-v1' 'GPT4-SE_alphabet-v0' 'GPT4-SE_alphabet-v1' 'GPT4-RP_alphabet-v0' 'GPT4-RP_alphabet-v1'  'GPT4-SR_alphabet-v0' 'GPT4-SR_alphabet-v1'
        # for NoT in 'GPT4-NR_descriptive-v0' 'GPT4-NR_descriptive-v1' 'GPT4-SE_descriptive-v0' 'GPT4-SE_descriptive-v1' 'GPT4-RP_descriptive-v0' 'GPT4-RP_descriptive-v1'  'GPT4-SR_descriptive-v0' 'GPT4-SR_descriptive-v1'
        do 
            for dataset in  schema11_test_normalized_shuffled-${NoT}_5shots  proscript_test_normalized_shuffled-${NoT}_5shots  wikihowscript_test_normalized_shuffled-${NoT}_5shots
            do 
                CUDA_VISIBLE_DEVICES=2 python src/train_bash.py \
                    --stage sft \
                    --do_predict \
                    --model_name_or_path  ${model} \
                    --dataset ${dataset}_${seed} \
                    --template ${my_dict[${model}]} \
                    --output_dir ../tmp_output/${model}/${dataset}_${seed} \
                    --predict_with_generate \
                    --per_device_eval_batch_size 1 \
                    --dataloader_num_workers 2 \
                    --no_do_sample \
                    --bf16 \
                    --cutoff_len 8192 \
                    --max_new_tokens 1024
            done
        done
    done
done



# run models out-of-the-box (i.e., no CoT or NoT)
for model in google/gemma-7b-it mistralai/Mistral-7B-Instruct-v0.2  meta-llama/Meta-Llama-3-8B-Instruct  
do
    for seed in 1 2 3 
    do
        for dataset in  schema11_test_normalized_shuffled_5shots  proscript_test_normalized_shuffled_5shots  wikihowscript_test_normalized_shuffled_5shots
        do 
            CUDA_VISIBLE_DEVICES=2 python src/train_bash.py \
                --stage sft \
                --do_predict \
                --model_name_or_path  ${model} \
                --dataset ${dataset}_${seed} \
                --template ${my_dict[${model}]} \
                --output_dir ../tmp_output/${model}/${dataset}_${seed} \
                --predict_with_generate \
                --per_device_eval_batch_size 1 \
                --dataloader_num_workers 2 \
                --no_do_sample \
                --bf16 \
                --cutoff_len 8192 \
                --max_new_tokens 1024
        done
    done
done