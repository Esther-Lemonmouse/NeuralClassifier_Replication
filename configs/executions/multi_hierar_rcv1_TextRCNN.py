#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@File       multi_hierar_rcv1_TextRCNN.py
@Author     Shuxin Yao
@Email      yaosx_job@outlook.com
@CreateTime 2023/1/16
@Function   
"""

from configs.dataset.rcv1_hierar import dataset_name, DATASET_DIR

_base_ = [
    '../_base_/model.py',
    '../dataset/rcv1_hierar.py'
    ]

OUTPUT_ROOT_DIR = "./output_dir"

task_info = dict(
    label_type="multi_label",
    hierarchical=True,
    hierar_taxonomy=DATASET_DIR+"/rcv1.taxonomy"
    )
device = "cuda"
model_name = "TextRCNN"
output_dir = OUTPUT_ROOT_DIR + "/" + task_info['label_type'] + "-hierar_" + str(task_info['hierarchical']) + "-" \
             + dataset_name + "-" + model_name
checkpoint_dir = output_dir + "/checkpoint_dir"
model_dir = output_dir + "/trained_model"
eval = dict(
    text_file="data/rcv1/rcv1_test.hierar.json",
    dir=output_dir+"/eval_dir",
    threshold=0.5,
    model_dir=checkpoint_dir+"/{0}_best".format(model_name),
    batch_size=1024,
    is_flat=False,
    top_k=5,
    pred_prefix=output_dir
    )
log = dict(
    logger_file=output_dir+"/log",
    log_level="warn"
    )
