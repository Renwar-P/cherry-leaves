![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## Codeanywhere Template Instructions

Welcome,

This is the Code Institute student template for Codeanywhere. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions. Click the `Use this template` button above to get started.

You can safely delete the Codeanywhere Template Instructions section of this README.md file,  and modify the remaining paragraphs for your own project. Please do read the Codeanywhere Template Instructions at least once, though! It contains some important information about the IDE and the extensions we use. 

## How to use this repo

1. Use this template to create your GitHub project repo

1. Log into <a href="https://app.codeanywhere.com/" target="_blank" rel="noreferrer">CodeAnywhere</a> with your GitHub account.

1. On your Dashboard, click on the New Workspace button

1. Paste in the URL you copied from GitHub earlier

1. Click Create

1. Wait for the workspace to open. This can take a few minutes.

1. Open a new terminal and <code>pip3 install -r requirements.txt</code>

1. In the terminal type <code>pip3 install jupyter</code>

1. In the terminal type <code>jupyter notebook --NotebookApp.token='' --NotebookApp.password=''</code> to start the jupyter server.

1. Open port 8888 preview or browser

1. Open the jupyter_notebooks directory in the jupyter webpage that has opened and click on the notebook you want to open.

1. Click the button Not Trusted and choose Trust.

Note that the kernel says Python 3. It inherits from the workspace so it will be Python-3.8.12 as installed by our template. To confirm this you can use <code>! python --version</code> in a notebook code cell.


## Cloud IDE Reminders

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you, so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.


## Dataset Content
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
* The dataset contains +4 thousand images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.



## Business Requirements
The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute.  The company has thousands of cherry trees, located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.


* 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
* 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.


## Hypothesis and how to validate?

### Hypothesis
* Cherry leaves affected by powdery mildew exhibit distinguishable visual patterns compared to healthy cherry leaves.
  
### Validation

* **Dataset Analysis**: Validate the hypothesis by conducting exploratory data analysis (EDA) on the dataset. Visualize samples of healthy and affected cherry leaves to identify any noticeable patterns or differences.
* **Model Development**: Train a machine learning model using Convolutional Neural Networks (CNNs) to differentiate between healthy and powdery mildew-affected cherry leaves. Validate the model's accuracy and performance metrics using appropriate validation techniques.
* **Evaluation**: Evaluate the model's performance on a separate test set to ensure its generalization ability. Calculate metrics such as accuracy to measure its effectiveness in identifying powdery mildew.  


## The rationale to map the business requirements to the Data Visualisations and ML tasks
### Business requirements
* **Visual Differentiation**: Visualize cherry leaf images to differentiate healthy leaves from those affected by powdery mildew. This aids in understanding the distinct features, if any, present in affected leaves.
* **Prediction**: Develop an ML model to predict whether a cherry leaf is healthy or has powdery mildew based on visual cues extracted from the images.
### Rationale

* **Data Visualization**: Visual exploration of the dataset helps in understanding the characteristics and variations present in healthy and affected cherry leaves. This aids in feature selection and extraction for model development.
* **ML Tasks**: Using CNNs leverages the capability of deep learning to automatically learn and identify intricate patterns in images, enabling accurate classification between healthy and affected leaves.

## ML Business Case

* **Efficiency Improvement**: Implementing an ML system for instant detection of powdery mildew on cherry leaves reduces manual inspection time significantly, making the process more efficient.
* **Scalability and Replicability**: Success in this project can pave the way for implementing similar ML-based detection systems for other crops, enhancing scalability and replicability across different agricultural scenarios.


## Dashboard Design
* ### **Project Summary**:
* Provides a detailed overview of powdery mildew, a fungal disease affecting cherry trees, including its characteristics, impact, and management strategies.
* Describes powdery mildew as a fungal disease affecting various plants, particularly cherry trees, thriving in warm, humid conditions.
* Explains its appearance as a powdery, white growth on leaves, shoots, and occasionally on the fruit.
* Specifies that the dataset is sourced from Kaggle.
* Indicates that the dataset showcases both healthy cherry leaves and leaves affected by powdery mildew.
* Encourages readers to visit and read the Project README file for further information.
* Highlights the project's two primary business requirements:
* 1. Conducting a study to visually differentiate between healthy cherry leaves and those infected with powdery mildew.
* 2. Developing a predictive capability to determine if a cherry leaf is healthy or infected with powdery mildew.

* #### **Dataset Information**:
* Sourced from Kaggle.
* Contains over 4,000 images captured from the client's crop fields.
* Displays both healthy cherry leaves and leaves affected by powdery mildew.
* Encourages users to explore and read the README file for a deeper understanding.

* #### **Business Requirements:**
* 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
* 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.
* ### **Project Hypothesis:**
* Cherry leaves affected by powdery mildew exhibit distinguishable visual patterns, especially along the leaf edges, setting them apart from healthy leaves.
* Emphasizes the identification of these distinct patterns on the leaf edges.
* Proposes the validation process through exploratory data analysis (EDA) on the dataset.
* Aims to visualize samples of healthy and affected cherry leaves to discern any noticeable patterns or differences.


* ### **Leaf Visualizer**: 
* This page computes healthy and mildew infected leaves. This helps the user to easier visualize the shape and differences between the leaves. It also computes a montage of leaves for the user to view.
* ####  **Visual Comparison:**
* Noticeable differences between average and variability images are observed.
* Shapes are recognizable in both mildew-infected and healthy leaves.
* Distinct color differences between healthy and mildew-infected leaves are noticeable.
* Healthy leaves exhibit a greener appearance.
* Users can refresh the montage by clicking the 'Create Montage' button.
* Allows selection of labels for viewing different subsets of images.
* Displays a grid of randomly selected images based on the chosen label.
* Adjusts the number of rows and columns to create montages with specific sizes.


* ### **Mildew Detection**:
* The client's objective is to determine whether a given leaf is infected with mildew.

* #### **Live Prediction and Data Download:**
* Allows users to upload mildew-infected leaf samples for live prediction.
* Provides the option to download a set of mildew-infected and healthy leaf images from Kaggle.

* #### **Live Prediction Functionality:**
* Users can upload one or multiple leaf images for analysis.
* Displays details about the uploaded image(s) like name and size.
* Resizes the uploaded image(s) for input into the prediction model (resize_input_image function).
* Uses a pre-trained model to predict the probability and class of mildew infection (load_model_and_predict function).
* Visualizes predictions and their probabilities (plot_predictions_probabilities function).

* #### **Analysis Report:**
* Generates an analysis report table displaying the uploaded image names and their corresponding prediction results.
* Provides an option to download the analysis report as a CSV file.


* ### **ML Performance**

* #### **Train, Validation, and Test Set Labels Frequencies:**
* Displays an image depicting the distribution of labels across train, validation, and test sets.
* #### **Model History:**
* Visualizes the model's training accuracy and losses over time.
* Includes separate images for the model's training accuracy (model_training_acc.png) and training losses (model_training_losses.png).
* #### **Generalized Performance on Test Set:**
* Presents a tabulated view of the model's evaluation metrics on the test set.
* Loads and displays the evaluation results for loss and accuracy obtained from the load_test_evaluation function. 

## Unfixed Bugs
* You will need to mention unfixed bugs and why they were unfixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable for consideration, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.


## Deployment
### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file. 


## Main Data Analysis and Machine Learning Libraries
* **Streamlit**: Streamlit is a Python library used for creating web applications for data science and machine learning projects. It simplifies the process of turning data scripts into shareable web apps. In this project it was used as a dashboard.
* **Jupyter**: Jupyter is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations, and narrative text. In this project it was used during the data collection and ML steps as a open IDE to better visualize the process.
* **NumPy**: NumPy is a fundamental package for scientific computing in Python. It provides support for arrays, matrices, and a collection of mathematical functions to operate on these arrays, making it essential for numerical operations in Python. In this project it was used frequently during data preparation for example.
* **Pandas**: Essential for data manipulation, cleaning, and analysis. Pandas facilitated tasks like loading datasets, cleaning data, performing exploratory data analysis (EDA), and organizing data for modeling.
* **Seaborn**: Seaborn is used for creating visually appealing statistical visualizations. Seaborn aided in generating various plots and statistical graphics to visualize patterns or relationships within the data.
* **Matplotlib**: Is used alongside Seaborn for creating customizable and publication-quality plots and visualizations, providing fine-grained control over visual elements in graphical representations.
* **PIL (Python Imaging Library)**: Is used for handling image data within the project, including tasks such as image preprocessing, loading, saving, or basic image manipulation in the mildew detector page on streamlit.
* **base64**: Is used for encoding and decoding binary image data in data_management.py file.
* **joblib**: Is used for caching or parallel execution of specific functions, especially in machine learning tasks that involve repeated computations or grid searches for hyperparameter tuning. The joblib library is being used for loading Pickle (.pkl) files via the load_pkl_file function.
* **datetime**: Is used for managing timestamps, handling date-related computations, or parsing dates and times especially in scenarios involving time-series data or logging. In this project it was used to generate a timestamp in a specific format, which is then incorporated into the filename while creating a downloadable report.
* **itertools**:itertools is a module in Python's standard library that provides various tools for creating and working with iterators efficiently. The itertools library is used within the image_montage function to generate the combinations of row and column indices for plotting images in a grid-like layout.
* **TensorFlow**: Tensroflow is an open-source machine learning framework developed by Google that is widely used for building and training machine learning models. It was used in this project in the ML process when training the model.
* **random**: The random library is utilized within the image_montage function to randomly sample images when the number of images in a directory exceeds the available grid spaces for the montage.
* **os**: Is used for handling file paths. 


## Credits 

* In this section, you need to reference where you got your content, media and from where you got extra help. It is common practice to use code from other repositories and tutorials. However, it is necessary to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A.
- Instructions on how to implement form validation on the Sign-Up page were taken from [Specific YouTube Tutorial](https://www.youtube.com/).
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/).

### Media

- The photos used on the home and sign-up page are from This Open-Source site.
- The images used for the gallery page were taken from this other open-source site.



## Acknowledgements (optional)
* Thank the people that provided support throughout this project.
