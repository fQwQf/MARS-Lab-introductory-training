# 第三周报告

## 一、本周工作总结

上周有点事，这周接上——所以这是第三周。

首先，demo跑通了，nice.

![](https://raw.githubusercontent.com/fQwQf/MARS-Lab-introductory-training/refs/heads/main/FLGo/test_mnist/res.png)

（不知道图片能不能正常显示？）

然后我看了一下组里的通用联邦学习框架，大体上说：

这个框架框架围绕generalization, robustness, and fairness——也就通用性，鲁棒性，公平性——是三大核心目标构建，覆盖横向与纵向联邦学习场景，并针对数据异构性、隐私安全、模型鲁棒性等挑战提出创新方法。

至于feature，大概有以下几个：

Federated Learning Survey：这些专注于解决客户端数据和模型异构性问题。

Robustness Federated Learning：这些专注于防御后门攻击、数据污染等安全问题。

Fairness Federated Learning：这些专注于缓解数据分布偏差导致的模型公平性下降。

除此之外，我还了解了一些联邦学习算法。为了书写排版方便，以下用了markdown内置的latex，为了让邮件支持markdown，我用了markdown here插件。其实我之前的邮件也是用markdown写的——还是挺方便的。：）  

以经典的FedAvg算法为例，其训练流程如下： 

1. **初始化**：服务器生成全局模型 $ w_0 $。 


2. **客户端选择**：每轮随机选择 $ K $ 个客户端（如10%）。 


3. **本地训练**： 


- 客户端下载当前全局模型 $ w_t $。 


- 在本地数据上执行 $ E $ 轮SGD更新，得到 $ w_t^k $。 


4. **参数聚合**：服务器计算加权平均 $ w_{t+1} = \sum_{k=1}^K \frac{n_k}{N} w_t^k $，其中 $ n_k $ 为客户端本地数据量。 


5. **重复迭代**：直至模型收敛。 

当然了，上面这一段对我来说更像是LaTeX练习（笑），因为FedAvg算法本身并不复杂，相关文献也是比较多的。不过我还是觉得这个框架的思路很棒，很值得学习。

## 二、下周工作计划

下周打算继续研究联邦学习。

- 阅读更多文献
- 尝试实现其中的一些算法
- 跑通比demo更复杂的项目

以上是我的第三周工作情况汇报，请老师批阅指导。  
