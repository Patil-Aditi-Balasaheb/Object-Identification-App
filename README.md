# Introduction
This is a Object Identification web app using Django and ResNet50 (CNN) model that takes an image from user and identifies the image by returning 3 predictions along with the accuracy score.

#### What is ResNet-50?
ResNet stands for Residual Network and is a specific type of convolutional neural network (CNN) introduced in the 2015 paper “Deep Residual Learning for Image Recognition” by He Kaiming, Zhang Xiangyu, Ren Shaoqing, and Sun Jian. CNNs are commonly used to power computer vision applications.

ResNet-50 is a 50-layer convolutional neural network (48 convolutional layers, one MaxPool layer, and one average pool layer). Residual neural networks are a type of artificial neural network (ANN) that forms networks by stacking residual blocks.


# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone git@github.com/Patil-Aditi-Balasaheb/Object-Identification-App.git
    $ cd Object-Identification-App
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements.txt
    
You can now run the development server:

    $ python manage.py runserver
