import week_03.Neuron as n, week_03.FeedForwardNetwork as ffn, numpy as np

init_list = list()
for i in range(0, 10):
    init_list.append(list())
    for j in range(0, 5):
        init_list[i].append(n.Neuron(np.random.rand(), [np.random.rand() for _ in range(5)]))

net = ffn.FeedForwardNetwork(init_list)

result = net.generate_output([np.random.rand() for _ in range(5)])

print(result)
