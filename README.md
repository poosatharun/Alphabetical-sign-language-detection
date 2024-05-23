# Alphabetical Sign Language Detection

The Alphabetical Sign Language Detection project aims to create a system capable of recognizing and interpreting alphabetical signs in sign language using the Python programming language. Sign language is a visual language that relies on gestures, hand movements, and facial expressions to convey meaning.

## Frameworks Used

This project utilizes the following frameworks:

- **TensorFlow**: TensorFlow is an open-source machine learning framework developed by Google.
- **OpenCV**: OpenCV is an open-source computer vision and machine learning software library.
- **Scikit-learn**: Scikit-learn is a simple and efficient tools for predictive data analysis.

Make sure to install these frameworks 

## Getting Started

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/poosatharun/Alphabetical-sign-language-detection.git
cd Alphabetical-sign-language-detection
```

### 2. Install Dependencies

This project requires certain dependencies. It's typically good practice to use a virtual environment for Python projects. Here’s how to set it up:

#### a. Create a Virtual Environment

```bash
python3 -m venv env
```

#### b. Activate the Virtual Environment

On Windows:

```bash
.\env\Scripts\activate
```

On macOS/Linux:

```bash
source env/bin/activate
```

#### c. Install Required Packages

```bash
pip install -r requirements.txt
```

### 3. Data Collection

Run the `Collection_of_images.py` script to collect all the necessary data from the user and store it in different folders.

### 4. Model Training

Next, run the `Train_the_Model.py` script. It will train a model and save the model in the designated path.

### 5. Testing

Run the `testing.py` script to test the trained model.


NOTE : After collecting the data separate the 20% data for the testing the model accuracy

# sample data images

### A
![Image_1681659560 7469316](https://github.com/poosatharun/Alphabetical-sign-language-detection/assets/107975821/26f1a280-612a-4d3b-97ab-9e360209422e)
### B
![Image_1681660340 6050572](https://github.com/poosatharun/Alphabetical-sign-language-detection/assets/107975821/8dc9f052-ce0d-4f03-bd78-89f9cb087f24)
### C
![Image_1681660469 7720032](https://github.com/poosatharun/Alphabetical-sign-language-detection/assets/107975821/dc69942b-5445-4bdc-b1bb-9f901630128b)
