### Check whether GPU is being used
```python
# tf2 (deprecated)
tf.test.is_gpu_available()

# tf2 (as of 2021/09)
tf.config.list_physical_devices('GPU')
```


### GPU worked for `tf2.2` but not for `tf.24`
It seems that

- `tf2.4` is using `libcudart.so.11.0`
- `tf2.2` is using `libcudart.so.10.1`
