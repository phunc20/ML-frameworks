The following example is elaborated from [https://pytorch.org/docs/stable/generated/torch.nn.LSTM.html](https://pytorch.org/docs/stable/generated/torch.nn.LSTM.html).
- (simplified) signature `nn.LSTM(input_size, hidden_size, num_layers)`
```python
In [1]: import torch; from torch import nn

In [2]: rnn = nn.LSTM(10, 20, 2)
   ...: # a batch of 5 sequences,
   ...: # each with 3 time steps and num_features = 10
   ...: input_ = torch.randn(5, 3, 10)
   ...: h0 = torch.randn(2, 3, 20)
   ...: c0 = torch.randn(2, 3, 20)
   ...: output, (hn, cn) = rnn(input_, (h0, c0))
   ...: print(f"output.shape = {output.shape}")
output.shape = torch.Size([5, 3, 20])

In [3]: hn.shape, cn.shape
Out[3]: (torch.Size([2, 3, 20]), torch.Size([2, 3, 20]))

In [4]: # Wrong
   ...: rnn = nn.LSTM(10, 20)
   ...: input_ = torch.randn(5, 3, 10)
   ...: h0 = torch.randn(2, 3, 20)
   ...: c0 = torch.randn(2, 3, 20)
   ...: output, (hn, cn) = rnn(input_, (h0, c0))
   ...:
RuntimeError: Expected hidden[0] size (1, 3, 20), got [2, 3, 20]

In [5]: rnn = nn.LSTM(10, 20)
   ...: input_ = torch.randn(5, 3, 10)
   ...: h0 = torch.randn(1, 3, 20)
   ...: c0 = torch.randn(1, 3, 20)
   ...: output, (hn, cn) = rnn(input_, (h0, c0))
   ...: output.shape, hn.shape, cn.shape
Out[5]: (torch.Size([5, 3, 20]), torch.Size([1, 3, 20]), torch.Size([1, 3, 20]))

In [6]: # Wrong
   ...: rnn = nn.LSTM(10, 20)
   ...: input_ = torch.randn(5, 3, 10)
   ...: h0 = torch.randn(3, 20)
   ...: c0 = torch.randn(3, 20)
   ...: output, (hn, cn) = rnn(input_, (h0, c0))
   ...: output.shape, hn.shape, cn.shape
RuntimeError: Expected hidden[0] size (1, 3, 20), got [3, 20]
```
From the example, we can see
- The RNN input should be of shape `(n_batches, n_timesteps, n_features)`
- `h0`, `c0`
  - for `nn.LSTM(input_size, hidden_size, num_layers=k)` with `k` greater than 1, `h0` and `c0` should be both of shape `(k, n_timesteps, hidden_size)`
  - for `nn.LSTM(input_size, hidden_size, num_layers=1)` (equiv. `nn.LSTM(input_size, hidden_size)`) , `h0` and `c0` should be both of shape `(1, n_timesteps, hidden_size)`
  - `hn` and `cn` will be of the same shape as `h0` and `c0`
