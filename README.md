# Capstone-Project-Gasturah

Capstone Project Bangkit 2022

Gasturah is a mobile-based app to help tourists recognize historical sites. Gasturah is a mean "Gas To Situs Bersejarah" which a have 3 features such as historical site detection, search location, and take share.



<h3>Machine Learning</h3>

Here is our ML workflow
1. Dataset

We collecting historical site images from google images with web scraping. We got 20000s images with 10 classes or sites with 2000s images in each class. <a href='https://github.com/Echo271/Capstone-Project-Gasturah/blob/main/ML%20Path/Web_Scrapper.py'> here is our web scraping script </a>.<br><img src="https://github.com/Echo271/Capstone-Project-Gasturah/blob/main/ML%20Assets/dataset.PNG" height="180em"><br><br> After getting and cleaning the dataset, we add augmentation to the dataset.<br><img src="https://github.com/Echo271/Capstone-Project-Gasturah/blob/main/ML%20Assets/Augment.PNG" height="180em"><br><br> <a href='https://drive.google.com/drive/folders/19Eq4rbeE2pYo0kwzD9v7bEL93rHCIP8M?usp=sharing'>here is if you want to see our dataset</a>. And then we split the dataset into 3 pieces 85% training data, 10% validation data, and 5% testing data.<br><img src="https://github.com/Echo271/Capstone-Project-Gasturah/blob/main/ML%20Assets/split data.PNG" height="180em">

2. Build Model

We build the model with TensorFlow. We use the Convolutional Neural Network method in our models. With images size 150, batch size 32, and 4 convolution layers like this.<br>
<img src="https://github.com/Echo271/Capstone-Project-Gasturah/blob/main/ML%20Assets/summary.png" alt="Summary" height="400em"><br>
We use adam optimizers with a learning rate of 0.0001 and we got 93% accuracy in the training set. You can look at the accuracy in here.
<img src="https://github.com/Echo271/Capstone-Project-Gasturah/blob/main/ML%20Assets/training.png">
<img src="https://github.com/Echo271/Capstone-Project-Gasturah/blob/main/ML%20Assets/accuracy.png">
<img src="https://github.com/Echo271/Capstone-Project-Gasturah/blob/main/ML%20Assets/loss.png"><br>
So we did the testing set with evaluate method from the testing data and we got an 83% accuracy.<br>
<img src="https://github.com/Echo271/Capstone-Project-Gasturah/blob/main/ML%20Assets/evaluate.png" width="700em"><br>
<a href='https://github.com/Echo271/Capstone-Project-Gasturah/blob/main/ML%20Path/Model_Gasturah.ipynb'>Click here is if you want to see more detail our model</a>

3. Save model

Before we save the model, we did simulation with random images to predict the image.<br>
<img src="https://github.com/Echo271/Capstone-Project-Gasturah/blob/main/ML%20Assets/simulate.png" height="400em"><br>
we create saved model as a folder. <a href="https://github.com/Echo271/Capstone-Project-Gasturah/tree/main/Saved%20Model">Here our saved model.</a>

4. Android Repository
    https://github.com/Lasteinsa/app_package_gasturah
5. Cloud Computing
  - Repository
    https://github.com/FarrelAlfarabi/Gasturah-Cloud
  - Endpoint 1
    https://gasturah.as.r.appspot.com/
  - Endpoint 2
    http://20.89.151.13/
  - Database
    http://20.89.151.13/phpmyadmin/
7. Figma Design
  https://www.figma.com/file/QRNvDrjtPEjN7aZWAMbGSl/Fix-Model?node-id=0%3A1
  
# ML-Path
- Eko   - Universitas Mulawarman 
- Reza  - Universitas Budi Luhur

# MD-Path
- Arman	- Universitas Mulawarman
- Rubi	- Universitas Budi Luhur

# CC-Path
- Daffa	- Universitas Mulawarman
- Farel	- Universitas Indonesia


File save model ML :
<a href="https://drive.google.com/drive/folders/1zTd7XtX2wz_ujjCIKtDqN_0PXUhazUC-?usp=sharing"> Save Model </a>
