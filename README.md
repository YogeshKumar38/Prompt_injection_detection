Prompt Injection Detection in Hinglish Chatbot

A security framework for Hinglish chatbots that detects and prevents prompt injection attacks using rule-based and machine learning techniques. It preprocesses code-mixed text, identifies malicious inputs, and ensures safe, reliable, and real-time AI interactions in bilingual environments.

Overview

This project focuses on developing a secure Hinglish chatbot capable of detecting and mitigating prompt injection attacks. Such attacks occur when malicious users embed hidden commands within normal inputs to manipulate chatbot behavior or extract confidential data. The system introduces a two-layer detection mechanism combining rule-based filtering and machine learning classification to identify and block malicious inputs in real time.

Objectives

To analyze and detect prompt injection attacks in Hinglish chatbots.

To develop a hybrid detection system combining rule-based and ML-based techniques.

To preprocess Hinglish text effectively for consistent analysis.

To integrate a fast and secure detection module within chatbot frameworks.

System Architecture

Input Preprocessing: Normalizes Hinglish text, handles transliteration, and removes unnecessary characters.

Rule-Based Detection: Uses keyword patterns and regular expressions to flag known attack phrases.

Machine Learning Classification: Applies supervised learning algorithms such as Logistic Regression and Decision Tree to classify text as safe or malicious.

Response Handling: Determines final chatbot behavior—safe inputs are processed normally, while malicious ones are blocked or flagged.

Tech Stack

Programming Language: Python

Libraries: NLTK, Scikit-learn, Pandas, Flask

Machine Learning Models: Logistic Regression, Decision Tree

Dataset: Custom Hinglish dataset containing normal and injected prompts

Results

Achieved approximately 92% accuracy in detecting injected prompts.

Reduced false positives and maintained real-time response speed.

Easily deployable as a modular security layer for chatbots.

Future Enhancements

Expand the dataset to include more Hinglish and multilingual samples.

Implement deep learning models such as transformers for improved detection.

Extend detection to voice-based Hinglish chatbot systems.

References

Ganguli et al. (2022); Greshake et al. (2023); Jain et al. (2018); Khanuja et al. (2020); Liu et al. (2023); Mandal et al. (2020); Perez & Ribeiro (2022); Solorio et al. (2014); Zhuo et al. (2023).

Keywords

Prompt Injection, Hinglish Chatbot, NLP Security, Machine Learning, Code-Mixed Language, Integrated Detection
