conda create -n NoT python=3.10
source activate NoT
conda install pytorch==1.13.1 torchvision==0.14.1 torchaudio==0.13.1 pytorch-cuda=11.7 -c pytorch -c nvidia
git clone https://github.com/hiyouga/LLaMA-Factory/tree/v0.5.3
cd LLaMA-Factory
cd ../
# to fix some bugs in LLaMA-Factory by moving files from extra folder. afterwards, extra folder will be deleted.
mv ./extra/metrc.py  ./LLaMA-Factory/src/llmtuner/train/sft/; mv ./extra/packages.py    ./LLaMA-Factory/src/llmtuner/extras/;  mv ./extra/template.py   ./LLaMA-Factory/src/llmtuner/data/;  rm -r extra
mkdir tmp_output outputs_llama data_llama