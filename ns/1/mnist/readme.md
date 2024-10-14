# MNIST CNN 99%

возьмем стандартный [MNIST CNN ipynb](https://colab.research.google.com/github/kirenz/deep-learning/blob/main/docs/mnist-tensorflow.ipynb)

установим 5 эпох

добавим сверточный слой на 128 признаков

установим на всех сверточных слоях padding='same'. если оставить 'valid', то flatten выдаст всего 128 признаков (а так 1152). тогда надо например убрать MaxPool после 1 сверточного слоя чтобы достичь 99% за 3 эпохи

установим после всех сверточных слоев MaxPool2D(). иначе будет переобучение после 1 эпохи

установим Dropout после сверточных и полносвязного слоев равным 0.3, потому что я боюсь сбрасывать 0.5

этой конфигурации соответсвует файл [MNIST_Tensorflow.ipynb](MNIST_Tensorflow.ipynb). видно что точность на тестовой выборке растет все 5 эпох, а на валидационной только 4

есть еще вариант получения почти 99%, используя более простую модель, но увеличенный датасет за счет аугментации - [augmentation.ipynb](augmentation.ipynb)