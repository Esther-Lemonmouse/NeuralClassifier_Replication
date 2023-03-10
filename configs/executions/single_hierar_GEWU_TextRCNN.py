#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@File       single_hierar_GEWU_TextRCNN.py
@Author     Shuxin Yao
@Email      yaosx_job@outlook.com
@CreateTime 2023/1/16
@Function   
"""

from configs.dataset.GEWU_hierar import dataset_name, DATASET_DIR

_base_ = [
    '../dataset/GEWU_hierar.py',
    '../_base_/model.py'
    ]

OUTPUT_ROOT_DIR = "./output_dir"
localtime = "230204_1048-"

task_info = dict(
    label_type="single_label",
    hierarchical=True,
    hierar_taxonomy=DATASET_DIR+"/GEWU.taxonomy"
    )
device = "cuda"
model_name = "TextRCNN"
output_dir = OUTPUT_ROOT_DIR + "/" + localtime + task_info['label_type'] + "-hierar_" + str(task_info['hierarchical']) \
             + "-" + dataset_name + "-" + model_name
checkpoint_dir = output_dir + "/checkpoint_dir"
model_dir = output_dir + "/trained_model"
data = dict(
    dict_dir=output_dir + "/GEWU_hierar_dict",
    generate_dict_using_pretrained_embedding=False
    )
feature = dict(
    token_ngram=0,
    # token_pretrained_file="./data/Pretrained/Chinese-Word-Vectors/sgns.zhihu.bigram"
    )
train = dict(
    batch_size=256,
    num_epochs=100
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
