# Capstone-Project-Gasturah

Capstone Project Bangkit 2022

Gasturah is a mobile-based app to help tourists recognize historical sites. Gasturah is a mean "Gas To Situs Bersejarah" which a have 3 features such as historical site detection, search location, and take share.

# ML-Path
- Eko   - Universitas Mulawarman 
- Reza  - Universitas Budi Luhur

#Machine Learning

Here is our ML workflow
1. Dataset

We collecting historical site images from google images with web scraping. We got 20000s images with 10 classes or sites with 2000s images in each class. <a href='https://github.com/Echo271/Capstone-Project-Gasturah/blob/main/ML%20Path/Web_Scrapper.py'> here is our web scraping script </a>. After getting and cleaning the dataset, we add augmentation to the dataset. <a href='https://github.com/Echo271/Capstone-Project-Gasturah/blob/main/ML%20Path/Model_Gasturah.ipynb'>you can see our dataset</a>. And then we split the dataset into 3 pieces 85% training data, 10% validation data, and 5% testing data.

2. Build Model

We build the model with TensorFlow. We use the Convolutional Neural Network method in our models. With images size 150, batch size 32, and 4 convolution layers like this.
<img src="https://github.com/Echo271/Capstone-Project-Gasturah/blob/main/ML%20Assets/summary.png" alt="Summary">
We use adam optimizers with a learning rate of 0.0001 and we got 93% accuracy in the training set. You can look at the accuracy in here.
<img src="https://github.com/Echo271/Capstone-Project-Gasturah/blob/main/ML%20Assets/accuracy.png">
<img src="https://github.com/Echo271/Capstone-Project-Gasturah/blob/main/ML%20Assets/loss.png">
So we did the testing set with evaluate method from the testing data and we got an 83% accuracy.
<img src="https://github.com/Echo271/Capstone-Project-Gasturah/blob/main/ML%20Assets/evaluate.png">

3. Save model

we create saved model as a folder. <a href="">Here our saved model.</a>

# MD-Path
- Arman	- Universitas Mulawarman
- Rubi	- Universitas Budi Luhur

# CC-Path
- Daffa	- Universitas Mulawarman
- Farel	- Universitas Indonesia


File save model ML :
<a href="https://drive.google.com/drive/folders/1zTd7XtX2wz_ujjCIKtDqN_0PXUhazUC-?usp=sharing"> Save Model </a>
