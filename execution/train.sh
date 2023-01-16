#!/usr/bin/env bash

PROJECT_DIR='/home/ysx/DeepLearning/Models_and_Demos/NeuralClassifier_Replication'
CFG_FILE='./configs/executions/multi_hierar_rcv1_TextRCNN.py'

export PYTHONPATH=$PROJECT_DIR
cd $PROJECT_DIR || exit
python tools/train.py $CFG_FILE