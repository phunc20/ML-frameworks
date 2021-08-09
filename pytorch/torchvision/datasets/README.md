## ImageNet
It seems that at first ImageNet could be freely downloaded using `torchvision.datasets` but by the year 2020 or 2021
it is no longer the case. One has to go to ImageNet's official website to request download: <https://www.image-net.org/>

The processing of the request might take an indefinite time.

```python
path_dataset = Path.home() / "datasets/pytorch/"

torchvision.datasets.ImageNet(
    root=path_dataset,
    split="train",
    download=True,
)
```
```
RuntimeError: The dataset is no longer publicly accessible. You need to download the archives externally and place them in the root directory.
```

**Rmk.**<br>
As suggested on [ImageNet's website](https://www.image-net.org/download.php),
if you just need a portion of the ImageNet images, Kaggle does kindly provides
[one of such subsets (`154.64GB`)](https://www.kaggle.com/c/imagenet-object-localization-challenge/data)




