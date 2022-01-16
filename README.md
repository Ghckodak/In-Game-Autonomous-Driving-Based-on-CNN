# In-Game-Autonomous-Driving-Based-on-CNN

## Inspiration
Autonomous driving is one of the hottest fields these days. However, learners/beginners may find it difficult to explore it and try out because it needs a modified real car. So why not use driving simulation games to try it?

## What it does
Just like a real autonomous driving car does - It grabs the images of the surrounding environment, in my case it is a screenshot and feed it into a trained CNN. CNN will output the command to control the car.

## How we built it
I use win32 api to grab the screen and record the actions on the keyboard. These information are used as training data for the CNN. The CNN is based on Tensorflow and training on Google Colab using Google Cloud services.

## Challenges we ran into
As there is not enough data for the CNN, overfitting occurs. I add some tranformations on the inout data and some dropout layers to fix it.

## Accomplishments that we're proud of
I manage to build an autonomous driving CNN successfully with only a few hours of data collection. My training data size is about 5GB and it is very small compared to some in-business NNs which usually have training data of PB scale.  Have such a small size of training data means it has to sacrifice accuracy, but I manage to keep the accuracy of 73%

## What we learned
How to collect and transform data. How to tune parameters of NN. Dealing with under/overfitting.

## What's next for In-Game Autonomous Driving Based on CNN
The performace of the model can be improved by training with more datas.
