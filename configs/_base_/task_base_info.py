#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@File       task_base_info.py
@Author     Shuxin Yao
@Email      yaosx_job@outlook.com
@CreateTime 2023/1/15
@Function   基础设置。包含如下部分
    task_info: 层级标签
@Attention
"""

OUTPUT_ROOT_DIR = "./output_dir"

task_info = dict(
    label_type="single_ or multi_label",
    hierarchical=True,
    hierar_taxonomy="xxx.taxonomy",
    hierar_penalty=1e-5
    )
device = "cuda or cpu"
model_name = "Model_Name"
dataset_name = "Dataset_Name"
output_dir = OUTPUT_ROOT_DIR + "/" + task_info['label_type'] + "-hierar_" + str(task_info['hierarchical']) + "-" \
             + dataset_name + "-" + model_name
checkpoint_dir = output_dir + "/checkpoint_dir"
model_dir = output_dir + "/trained_model"
data = dict(
    train_json_files=[
        "TRAIN.json"
        ],
    validate_json_files=[
        "VALIDATE.json"
        ],
    test_json_files=[
        "TEST.json"
        ],
    dict_dir="dict_dir",
    generate_dict_using_json_files=True,
    generate_dict_using_all_json_files=True,
    generate_dict_using_pretrained_embedding=False,
    generate_hierarchy_label=True,
    num_worker=4
    )
feature = dict(
    feature_names=[
        "token"
        ],
    min_token_count=2,
    min_char_count=2,
    token_ngram=0,
    min_token_ngram_count=0,
    min_keyword_count=0,
    min_topic_count=2,
    max_token_dict_size=1000000,
    max_char_dict_size=150000,
    max_token_ngram_dict_size=10000000,
    max_keyword_dict_size=100,
    max_topic_dict_size=100,
    max_token_len=256,
    max_char_len=1024,
    max_char_len_per_token=4,
    token_pretrained_file="",
    keyword_pretrained_file=""
    )
train = dict(
    batch_size=64,
    start_epoch=1,
    num_epochs=50,
    num_epochs_static_embedding=0,
    decay_steps=1000,
    decay_rate=1.0,
    clip_gradients=100.0,
    l2_lambda=0.0,
    loss_type="BCEWithLogitsLoss",
    sampler="fixed",
    num_sampled=5,
    visible_device_list="0",
    hidden_layer_dropout=0.5
    )
embedding = dict(
    type="embedding",
    dimension=64,
    region_embedding_type="context_word",
    region_size=5,
    initializer="uniform",
    fan_mode="FAN_IN",
    uniform_bound=0.25,
    random_stddev=0.01,
    dropout=0.0
    )
optimizer = dict(
    optimizer_type="Adam",
    learning_rate=0.008,
    adadelta_decay_rate=0.95,
    adadelta_epsilon=1e-08
    )
eval = dict(
    text_file="Textxxx.json",
    dir=output_dir+"/eval_dir",
    threshold=0.5,
    model_dir=checkpoint_dir+"/{0}_best".format(model_name),
    batch_size=1024,
    is_flat=False,
    top_k=20,
    pred_prefix=output_dir
    )
log = dict(
    logger_file=output_dir+"/log",
    log_level="warn"
    )
