#!/usr/bin/env bash

# 项目目录，注意切换本地和远程
# PROJECT_DIR='/home/ysx/DeepLearning/Models_and_Demos/NeuralClassifier_Replication'
PROJECT_DIR='/home/linyuyang/Math_Fomula_Detection/NeuralClassifier_Replication'

CFG_FILE=$1

export PYTHONPATH=$PROJECT_DIR
cd $PROJECT_DIR || exit
python tools/train.py $CFG_FILE