import torch
#开根号后取倒数
t = torch.rsqrt(torch.tensor(4.0))
print(t)

# 相应维度全为1的矩阵
t2 = torch.ones(3,4)
print(t2)