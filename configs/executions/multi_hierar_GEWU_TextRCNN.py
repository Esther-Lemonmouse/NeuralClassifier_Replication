#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@File       multi_hierar_GEWU_TextRCNN.py
@Author     Shuxin Yao
@Email      yaosx_job@outlook.com
@CreateTime 2023/1/16
@Function   
"""

from configs.dataset.GEWU_hierar import dataset_name, DATASET_DIR

_base_ = [
    '../_base_/model.py',
    '../dataset/GEWU_hierar.py'
    ]

OUTPUT_ROOT_DIR = "./output_dir"

task_info = dict(
    label_type="multi_label",
    hierarchical=True,
    hierar_taxonomy=DATASET_DIR+"/GEWU.taxonomy"
    )
device = "cuda"
model_name = "TextRCNN"
output_dir = OUTPUT_ROOT_DIR + "/" + task_info['label_type'] + "-hierar_" + str(task_info['hierarchical']) + "-" \
             + dataset_name + "-" + model_name
checkpoint_dir = output_dir + "/checkpoint_dir"
model_dir = output_dir + "/trained_model"
# data = dict(
#     generate_dict_using_pretrained_embedding=True
# )
feature = dict(
    token_ngram=2
    # token_pretrained_file="./data/Pretrained/Chinese-Word-Vectors/sgns.zhihu.bigram"
)
train = dict(
    batch_size=256
)
embedding = dict(
    dimension=300
)
eval = dict(
    text_file="data/eval_eg/test.txt",
    dir=output_dir+"/eval_dir",
    threshold=0.4,
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
