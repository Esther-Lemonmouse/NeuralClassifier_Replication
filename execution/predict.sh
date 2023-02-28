#!/usr/bin/env bash

# 外部配置文件所在目录参数接收
CKPT_NAME_DIR=$1
PREDICT_JSON_PTH=$2

# 项目目录，注意切换本地和远程
# PROJECT_DIR='/home/ysx/DeepLearning/Models_and_Demos/NeuralClassifier_Replication'
PROJECT_DIR='/home/linyuyang/Math_Fomula_Detection/NeuralClassifier_Replication'

CFG_FILE=$CKPT_NAME_DIR'/config.py'

export PYTHONPATH=$PROJECT_DIR
cd $PROJECT_DIR || exit
python tools/predict.py "$CFG_FILE" "$PREDICT_JSON_PTH"
