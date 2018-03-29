import week_03.Neuron as n


class FeedForwardNetwork:
    def __init__(self, list_of_list_of_neurons):
        self.list_of_list_of_neurons = list_of_list_of_neurons

    def generate_output(self, input_x):
        for i in self.list_of_list_of_neurons[0]:
            n.Neuron.cacl_y(i, input_x[self.list_of_list_of_neurons[0].index(i)])

        for layer in self.list_of_list_of_neurons:
            if self.list_of_list_of_neurons.index(layer) == 0:
                continue
            for neuron in self.list_of_list_of_neurons[self.list_of_list_of_neurons.index(layer)-1]:
                prev_y = list()
                prev_y.append(neuron.y)
            for neuron in layer:
                neuron.cacl_y(prev_y)

        output = list()
        for neuron in self.list_of_list_of_neurons[len(self.list_of_list_of_neurons)-1]:
            output.append(neuron.y)

        return output
