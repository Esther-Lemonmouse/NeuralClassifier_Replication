#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@File       multi_hierar_GEWUQT_TextVDCNN.py
@Author     Shuxin Yao
@Email      yaosx_job@outlook.com
@CreateTime 2023/1/16
@Function   

@Notes      别治了，抬走，表现真的太差了。
"""

from configs.dataset.GEWUwithQuesType_hierar import dataset_name, DATASET_DIR

_base_ = [
    '../dataset/GEWUwithQuesType_hierar.py',
    '../_base_/model.py'
    ]

OUTPUT_ROOT_DIR = "./output_dir"
timing = "230208_1949-"

task_info = dict(
    label_type="multi_label",
    hierarchical=True,
    hierar_taxonomy=DATASET_DIR + "/GEWU.taxonomy"
    )
device = "cuda"
model_name = "TextVDCNN"
output_dir = OUTPUT_ROOT_DIR + "/" + timing + task_info['label_type'] + "-hierar_" + str(task_info['hierarchical']) \
             + "-" + dataset_name + "-" + model_name
checkpoint_dir = output_dir + "/checkpoint_dir"
model_dir = output_dir + "/trained_model"
data = dict(
    dict_dir=output_dir + "/GEWUwithQuesType_hierar_dict",
    generate_dict_using_pretrained_embedding=False
    )
feature = dict(
    token_ngram=0
    )
train = dict(
    batch_size=128,
    num_epochs=100,
    visible_device_list="1"
    )
embedding = dict(
    dimension=300
    )
eval = dict(
    dir=output_dir + "/eval_dir",
    threshold=0.3,
    model_dir=checkpoint_dir + "/{0}_best".format(model_name),
    batch_size=1024,
    is_flat=False,
    top_k=3,
    pred_prefix=output_dir
    )
log = dict(
    logger_file=output_dir + "/log",
    log_level="warn"
    )
