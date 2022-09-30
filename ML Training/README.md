# ML Training

## Requirements
1. Tensorflow

To set up tensorflow on M1 Mac follow the instructions here
https://caffeinedev.medium.com/how-to-install-tensorflow-on-m1-mac-8e9b91d93706

For x86 machines,
```console
$ python3 -m venv mnist_env
$ source ./mnist_env/bin/activate
$ pip install tensorflow
```
## Step 1: Run CNN model on normal mnist
```console
$ python mnist.py
```
The loss and accuracy values are printed in the console after training, validation and evaluation is done

## Step 3: Run CNN model on extended mnist with augmented images
```console
$ python mnist-rotated.py
```
The loss and accuracy values are printed in the console after training, validation and evaluation is done

## Final Comments
My development laptop is the M1 Macbook Pro which posed alot of issues with downloading tensorflow using pip in a virtual environment. 
The only workaround was using miniforge to download tensorflow and thereby using a conda virtual environment.
However, there is no way to include the conda environment in this folder

