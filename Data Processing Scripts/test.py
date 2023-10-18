import torch
print(torch.cuda.is_available())
x = torch.cuda.get_device_properties(0).name
print(x)