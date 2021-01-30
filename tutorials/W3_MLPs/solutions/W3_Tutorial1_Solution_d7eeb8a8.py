
x = torch.rand((10000, 10000)).to(dev) - 0.5
print("Pytorch : ", end='')
%timeit -n10 -r3 torch.relu(x)
print('-----------------------------------------------')

print("First: ", end='')
%timeit -n10 -r3 torch.max(x, torch.zeros_like(x))
print('-----------------------------------------------')

print("Second: ", end='')
%timeit -n10 -r3 x * (x > 0)
print('-----------------------------------------------')

print("Third: ", end='')
%timeit -n10 -r3 x[x < 0] = 0
print('-----------------------------------------------')

print("Forth: ", end='')
%timeit -n10 -r3 (torch.abs(x) + x) / 2