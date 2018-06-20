config = {
    'train_data_file': './data/train.conll',  # 训练集文件
    'dev_data_file': './data/dev.conll',  # 开发集文件
    'test_data_file': './data/dev.conll',  # 测试集文件
    'iterator': 20,  # 最大迭代次数
    'batchsize': 1,  # 批次大小
    'shuffle': False,  # 每次迭代是否打乱数据
    'regulization': False,  # 是否正则化
    'step_opt': False,  # 是否步长优化
    'eta': 0.5,  # 初始步长,step_eta为False时无效
    'C': 0.0001  # 正则化系数,regulization为False时无效
}
