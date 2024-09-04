# URL-Based Web Phishing Detection Model

## Introduction

In today's digital landscape, phishing attacks pose a significant threat to individuals and organizations worldwide. Phishing URLs are crafted to deceive users into divulging sensitive information or downloading malicious software. To combat this threat, this project leverages machine learning algorithms to detect phishing URLs effectively.

## Project Description

This project focuses on the detection of phishing URLs using various machine learning algorithms trained on a curated dataset. The dataset includes both legitimate and phishing URLs, ensuring diversity and representation of various attack types. Key features extracted from the URLs play a crucial role in distinguishing between legitimate and phishing URLs.

## Problem Statement

Phishing attacks continue to evolve in sophistication, making it challenging to detect malicious URLs using traditional methods. Manual identification of phishing URLs is time-consuming and prone to errors, necessitating automated solutions that can accurately distinguish between legitimate and phishing URLs.

## Objectives

- Develop a robust machine learning-based system capable of accurately detecting phishing URLs.
- Curate a diverse dataset comprising legitimate and phishing URLs to train and evaluate the detection models.
- Extract relevant features from URLs to facilitate effective classification by machine learning algorithms.
- Evaluate the performance of different machine learning models and identify the most effective approach for phishing detection.
- Provide guidelines and resources for deploying the trained models in real-world applications to proactively mitigate phishing attacks.

## Data Preprocessing and Feature Extraction

The dataset is preprocessed by removing unnecessary columns and extracting key features from the URLs. The following features are extracted using Python libraries:

- **IP Address**: Identifies whether the URL includes an IP address.
- **LongURL**: Checks if the URL is long.
- **ShortURL**: Detects if the URL is shortened.
- **Symbol@**: Detects the presence of symbols like '@' in the URL.
- **Redirecting//**: Detects if the URL has redirecting characters.
- **PrefixSuffix-**: Checks for prefix and suffix characters in the URL.
- **SubDomains**: Counts the number of subdomains in the URL.
- **HTTPS**: Indicates whether the URL uses HTTPS.
- **DomainRegLen**: Calculates the length of the domain registration.
- **Favicon**: Checks for the presence of a favicon.
- **NonStdPort**: Detects non-standard ports in the URL.
- **AgeofDomain**: Calculates the age of the domain.
- **DNSRecording**: Checks for DNS recording.
- **WebsiteTraffic**: Estimates website traffic.
- **GoogleIndex**: Checks if the URL is indexed by Google.
- And more...

## Model Training and Evaluation

The data is split into training and testing sets using a 70-30 split ratio. Various machine learning models are trained on the extracted features. The table below summarizes the accuracy of each model:

| Model                     | Accuracy |
|---------------------------|----------|
| K-Nearest Neighbors (KNN) | 95%      |
| Logistic Regression       | 92%      |
| Decision Tree Classifier  | 96%      |
| Random Forest Classifier  | 97%      |

Each model's performance is evaluated based on metrics such as accuracy, precision, recall, and F1-score. The Random Forest Classifier achieved the highest accuracy, making it the most effective model for phishing detection in this study.

## Results

The trained models are evaluated based on their performance metrics:

- **Random Forest Classifier** emerged as the most accurate model with 97% accuracy.
- **Decision Tree Classifier** showed strong performance with 96% accuracy.
- **K-Nearest Neighbors (KNN)** achieved 95% accuracy.
- **Logistic Regression** achieved 92% accuracy.

## Getting Started

To get started with the project, clone the repository and install the necessary dependencies listed in `requirements.txt`. Run the Jupyter Notebook (`Model.ipynb`) to preprocess data, train the models, and evaluate their performance.

1. Clone the repository:

```bash
git clone https://github.com/PriyanshuLathi/URL-Based-Web-Phishing-Detection-Model
```

2. Navigate to the project directory:

```bash
cd URL-Based-Web-Phishing-Detection-Model
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the Jupyter Notebook:

```bash
jupyter notebook Model.ipynb
```

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/PriyanshuLathi/URL-Based-Web-Phishing-Detection-Model/blob/main/LICENSE) file for details.

## Contact

For questions or feedback:

- LinkedIn: [Priyanshu Lathi](https://www.linkedin.com/in/priyanshu-lathi)
- GitHub: [Priyanshu Lathi](https://github.com/PriyanshuLathi)

## Authors

- Priyanshu Lathi
