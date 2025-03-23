import flgo
import flgo.algorithm.fedavg as fedavg
import os

import flgo.benchmark.mnist_classification as mnist
import flgo.benchmark.partition as fbp
# task为任务路径，可以自行定义，该目录将被视作一个联邦任务
task = './test_mnist'
# benchmark关键字指定的是数据集，partitioner关键字指定的是联邦学习数据集划分器
flgo.gen_task_by_(benchmark=mnist, partitioner=fbp.IIDPartitioner(num_clients=100), task_path=task)

fedavg_runner = flgo.init(task=task, algorithm=fedavg, option={'num_rounds':5, 'num_epochs':1, 'gpu':0})
fedavg_runner.run()

import flgo.experiment.analyzer as al
analysis_plan = {
    'Selector':{
        'task': task,
        'header':['fedavg']
    },
    'Painter':{
        'Curve':[
            {'args':{'x': 'communication_round', 'y':'val_loss'}, 'fig_option':{'title':'valid loss on MNIST'}},
            {'args':{'x': 'communication_round', 'y':'val_accuracy'},  'fig_option':{'title':'valid accuracy on MNIST'}},
        ]
    }
}
al.show(analysis_plan)