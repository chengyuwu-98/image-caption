# Image Captioning including Attention

The product is designed for disabled people, who cannot see the pictures but can listen to the description. We are aiming to enable disabled people to access more information and experience the beauty of the world. Our product can predict the captioning of an image and display to users. A user can upload an image and play the audio of the captioning of the image, so that they can "hear" the image. Our [Website](http://35.202.212.110:8080/) is available!

## Dataset

[Flickr8k dataset from Kaggle](https://www.kaggle.com/datasets/adityajn105/flickr8k)

## Starter code
This repo was originally forked from [here.](https://github.com/bkenan/image_captioning_attention.git)

## Video demo
Watch on [Youtube](https://youtu.be/zO_nXKDzCJI)

## Demo

The default frontend looks like

![image](https://user-images.githubusercontent.com/97444802/163241489-7ab169b6-2865-4668-be47-a5827a145a47.png)

When you upload a image, it looks like:

![test](https://user-images.githubusercontent.com/53462948/164124856-b6a6f3fb-6ee5-48c8-ac14-e7daf7d723e0.png)



## Deployment
![updated diagram](https://user-images.githubusercontent.com/76429734/164073352-1f0cbc3a-dd22-4bfe-9648-01daea1e1e19.png)


### How to trigger Continous Delivery：
Once you update the code for application, run `git tag <tagname>` `git push origin <tagname>` the Cloud Build will automatically begin and the application will update.
Therefore, we can make sure every time there is a new version of our application, it can update automatically.


## Load test
Load test is implemented use Locust for 10000 users at peak :
![183555737d925b834cbd7aacb32d79a](https://user-images.githubusercontent.com/97444802/163694662-286a601d-9259-497d-a372-ed335328a86b.png)


## Getting started in the local machine:

1. Clone this repo
2. Download [my trained model](https://drive.google.com/file/d/1t3QbSauxSnZhXE1DbuGwiT2AokOsqOjA/view?usp=sharing) and put it in a new "models" folder within the repo directory
3. make install
4. Open Python Shell and run:
    import spacy
    
    from spacy.cli.download import download
    download(model="en_core_web_sm")
5. Run flask_app.py


## Getting started in Colab:

[![My Colab notebook](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1z1sI5wVmoflOggLfIuIIj7qQ0xAICtgn?usp=sharing) 

Download the Image folder from the above dataset, zip the "Image" folder and put it in the current Colab working directory.
