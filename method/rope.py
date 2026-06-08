import torch

# x = torch.tensor([1,2,3,4,5,6,1])
# y = torch.tensor([7,8,9,10,11,12,1.2])
# condition = x > 4
# # 将x中不满足condition的部分由y中对应的位置量替换，xy必须维度相同
# result = torch.where(condition, x, y)
# print(result) #output: tensor([ 7.0000,  8.0000,  9.0000, 10.0000,  5.0000,  6.0000,  1.2000])

# 生成一个范围内的张量
# t1 = torch.arange(0 ,10, 2)
# t2 = torch.arange(0 ,-8, -2)
# print(t1)   #tensor([0, 2, 4, 6, 8])
# print(t2)   #tensor([ 0, -2, -4, -6])

# #外积
# t3 = torch.tensor([1,2,3])
# t4 = torch.tensor([4,5,6])
# print(torch.outer(t3,t4))   # tensor([[ 4,  5,  6],[ 8, 10, 12],[12, 15, 18]])

# #按照指定维度拼接 cat
# t5 = torch.tensor([[[1,2,3], [4,5,6]],[[7,8,9], [10,11,12]]])
# print(t5.shape)
# t6 = torch.tensor([[[13,14,15],[16,17,18]], [[19,20,21], [22,23,24]]])
# t7 = torch.cat((t5,t6), dim=-1)
# print(t7)
# print(t7.shape) #torch.Size([2, 2, 6])

# #在下标处增加一个维度 unsqueeze
# t8 = torch.tensor([1,2,3])
# t9 = torch.unsqueeze(t8,0)
# print(t9)
# print(t9.shape)

t10 = torch.tensor([[0.1,0.2,0.3],[0.4,0.5,0.6]])

t11 = torch.cat([torch.cos(t10), torch.cos(t10)], dim=-1)
print(t11)
print(t11.shape)




