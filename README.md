# Multi-label classification
Model trained on paired images of digits from MNIST dataset.
There are still 10 classes, and two indices of max logits is taken to predict number


## Usage
From root directory run:

```bash
docker build -t numbers .
docker run -d --name mcontainer -p 80:80 myimage
```

Application will be available on 0.0.0.0:80


