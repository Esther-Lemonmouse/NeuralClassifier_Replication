#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@File       rcv1.py
@Author     Shuxin Yao
@Email      yaosx_job@outlook.com
@CreateTime 2023/1/16
@Function   
"""

_base_ = ['../_base_/task_base_info.py']

DATASET_DIR = "./data/rcv1"

dataset_name = "rcv1"
data = dict(
    train_json_files=[
        DATASET_DIR + "/rcv1_train.json"
        ],
    validate_json_files=[
        DATASET_DIR + "/rcv1_dev.json"
        ],
    test_json_files=[
        DATASET_DIR + "/rcv1_test.json"
        ],
    dict_dir=DATASET_DIR + "/rcv1_dict"
    )
