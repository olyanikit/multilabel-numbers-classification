# Multi-label classification
Model trained on paired images of digits from MNIST dataset.

# Описание решения
Решалась задача мультиклассовой классификации, в качестве таргетов числа в виде one hot encoded вектора.
На выходе из линейного слоя используется функция активации сигмоида, потому что для каждого класса решается бинарная классификация.

Модель сохранена в формате onnx, квантизирована до точности параметров int8

На данный момент модель обучена на парах чисел, из инференса тоже выбирается два числа, для предсказания любого числа от 0 до 999 нужно использовать порог, по которому отбирается количество классов.

## Usage
From root directory run:

```bash
docker build -t numbers .
docker run -d --name mcontainer -p 80:80 myimage
```

Application will be available on 0.0.0.0:80


