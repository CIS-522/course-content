class TaggingRNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size, n_layers=1):
        super(TaggingRNN, self).__init__()
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.n_layers = n_layers
        
        self.embedding = nn.Embedding(input_size, hidden_size)
        self.gru = nn.GRU(hidden_size, hidden_size, n_layers)
        self.linear = nn.Linear(hidden_size, 3)
    
    def forward(self, input, hidden):
        input = self.embedding(input.view(1, -1)) 
        output, hidden = self.gru(input.view(1, 1, -1), hidden)
        out = self.linear(hidden)
        return out, hidden

    def init_hidden(self):
        return torch.zeros(self.n_layers, 1, self.hidden_size)
