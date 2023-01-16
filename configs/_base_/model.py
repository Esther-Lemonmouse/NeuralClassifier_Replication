#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@File       model.py
@Author     Shuxin Yao
@Email      yaosx_job@outlook.com
@CreateTime 2023/1/15
@Function   
"""

TextCNN = dict(
    kernel_sizes=[
        2, 3, 4
        ],
    num_kernels=100,
    top_k_max_pooling=1
    )
TextRNN = dict(
    hidden_dimension=64,
    rnn_type="GRU",
    num_layers=1,
    doc_embedding_type="Attention",
    attention_dimension=16,
    bidirectional=True
    )
DRNN = dict(
    hidden_dimension=5,
    window_size=3,
    rnn_type="GRU",
    bidirectional=True,
    cell_hidden_dropout=0.1
    )
TextVDCNN = dict(
    vdcnn_depth=9,
    top_k_max_pooling=8
    )
DPCNN = dict(
    kernel_size=3,
    pooling_stride=2,
    num_kernels=16,
    blocks=2
    )
TextRCNN = dict(
    kernel_sizes=[
        2, 3, 4
        ],
    num_kernels=100,
    top_k_max_pooling=1,
    hidden_dimension=64,
    rnn_type="GRU",
    num_layers=1,
    bidirectional=True
    )
Transformer = dict(
    d_inner=128,
    d_k=32,
    d_v=32,
    n_head=4,
    n_layers=1,
    dropout=0.1,
    use_star=True
    )
AttentiveConvNet = dict(
    attention_type="bilinear",
    margin_size=3,
    type="advanced",
    hidden_size=64
    )
HMCN = dict(
    hierarchical_depth=[
        0, 384, 384, 384, 384
        ],
    global2local=[
        0, 4, 55, 43, 1
        ]
    )
