# README

## 1.环境配置

注意：与原作不同，本工作代码需要使用openai 0.27.0版本

```
python==3.8.10
huggingface-hub
numpy==1.23.2
openai==0.27.0
pandas==1.4.3
transformers==4.21.1
requests==2.28.1
```

## 2.OpenAI API Key

如若需要使用OpenAI API 需要在model.py代码中添加OpenAI API Key。

如若需要使用其他的大语言模型，需要在utilities.py中添加针对其他大语言模型的调用方法。

## 3.Google Search API Key

如若需要使用Google Search API 需要在model.py代码中添加Google Search API Key

## 4.ScienceQA实验

以gpt4作为基础大语言模型时

```
cd run_scienceqa

python run.py \
--model chameleon \
--label chameleon_gpt4 \
--policy_engine gpt-4 \
--kr_engine gpt-4 \
--qg_engine gpt-4 \
--sg_engine gpt-4 \
--test_split test \
--test_number -1
```

以gpt3.5作为基础大语言模型时

```
python run.py \
--model chameleon \
--label chameleon_gpt4 \
--policy_engine gpt-3.5-turbo \
--kr_engine gpt-3.5-turbo \
--qg_engine gpt-3.5-turbo \
--sg_engine gpt-3.5-turbo \
--test_split test \
--test_number -1
```

获取准确率评估时

```
python evaluate.py \
--data_file ../data/scienceqa/problems.json \
--result_root ../my_results/scienceqa \
--result_files chameleon_chatgpt_test_cache.jsonl
```

## 5.TabMWP实验

以gpt4作为基础大语言模型时

```
cd run_tabmwp

python run.py \
--model chameleon \
--label chameleon_gpt4 \
--test_split test \
--policy_engine gpt-4 \
--rl_engine gpt-4 \
--cl_engine gpt-4 \
--tv_engine gpt-4 \
--kr_engine gpt-4 \
--sg_engine gpt-4 \
--pg_engine gpt-4 \
--test_number -1 \
--rl_cell_threshold 18 \
--cl_cell_threshold 18
```

以gpt3.5作为基础大语言模型时

```
python run.py \
--model chameleon \
--label chameleon_chatgpt \
--test_split test \
--policy_engine gpt-3.5-turbo \
--rl_engine gpt-3.5-turbo \
--cl_engine gpt-3.5-turbo \
--tv_engine gpt-3.5-turbo \
--kr_engine gpt-3.5-turbo \
--sg_engine gpt-3.5-turbo \
--pg_engine gpt-3.5-turbo \
--test_number -1 \
--rl_cell_threshold 18 \
--cl_cell_threshold 18
```

获取准确率评估时

```
python evaluate.py \
--data_file ../data/tabmwp/problems_test.json \
--result_root ../my_results/tabmwp \
--result_files chameleon_chatgpt_test_cache.jsonl
```

