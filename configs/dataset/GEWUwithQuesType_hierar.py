#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@File       GEWUwithQuesType_hierar.py
@Author     Shuxin Yao
@Email      yaosx_job@outlook.com
@CreateTime 2023/1/16
@Function   
"""

_base_ = ['../_base_/task_base_info.py']

DATASET_DIR = "./data/GEWUwithQuestionType"

dataset_name = "GEWUQT"
data = dict(
    train_json_files=[
        DATASET_DIR + "/GEWU_training.json"
        ],
    validate_json_files=[
        DATASET_DIR + "/GEWU_validation.json"
        ],
    test_json_files=[
        DATASET_DIR + "/GEWU_testing.json"
        ],
    dict_dir=DATASET_DIR + "/GEWU_hierar_dict"
    )
