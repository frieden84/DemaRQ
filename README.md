# DemaRQ (Version 1.0) #
DemaRQ: Demarcator for ReQuirements

## Story behind it: ##
Requirements demarcation is a simple but important task during the analysis of a textual requirements specification. The task is essentially to determine which statements in the specification represent requirements. Following suitable writing and markup conventions does not guarantee immediate and unequivocal demarcation, since neither the presence nor a fully accurate enforcement of such conventions can be taken for granted. Resorting to after-the-fact reviews for sifting requirements from other material in a requirements specification is both tedious and time-consuming. 

Motivated by the need for demarcating requirements in requirements specifications irrespective of domain, terminology or style, we present a novel tool, DemaRQ (Demarcator for ReQuirements), for demarcating requirements in free-form requirements specifications. DemaRQ is based on Machine Learning (ML). The ML classifier in DemaRQ is a Random Forest  model with Cost-sensitive Learning. This classifier has been trained over 16161 manually labeled statements from 26 requirements specifications (written in natural language) using different styles and covering diverse domains. 

DemaRQ works by first parsing a requirements specification using Natural Language Processing (NLP). The tool then computes, based on the NLP results, a set of features for each sentence in the requirements specification. The features fall under four categories: token-based features capture the token-level information, syntactic features are derived syntax-related information, semantic features are about the semantic categories of the verbs, and frequency-based features characterize sentences based on document-level information. The computed features are aggregated in a feature matrix. DemaRQ then applies its pre-trained model for classifying each sentence in the input requirements specification as a REQUIREMENT or a NON-REQUIREMENT.

## System requirements: ##
Java 1.7 (or [higher](https://www.oracle.com/java/technologies/javase-jre8-downloads.html))

## Specific details about the tool:
- The tool takes as an input a requirements specification with the extension: ".docx"
- The tool produces the results file: "predictions.res", which contains the predicted class next to each sentence in the input requirements specification. The class can be REQUIREMENT or NONREQUIREMENT.
- By default, the tool uses a pre-trained model that is the best model reported in the paper described below (Abualhaija et al., 2019) corresponding to the random forest classifier with cost-sensitive learning.
- The "gold.txt" is the corresponding ground truth to the input requirements specification and should contain only the requirements as per human annotation, where each requirement is on a separate line. 
  
## Usage instructions: ##

To run the DemaRQ tool, refer to the following instructions:

1. Download and unzip DemaRQ into some location on your local machine. In the remainder, we will refer to the folder containing DemaRQ as *root_dir*.
2. Open a terminal and go to the *root_dir*. For example, in macOS write the following in your terminal: cd {path to *root_dir*}
3. Use the following command to run the tool on the "Demo.docx" requirements specification: 
```java -jar DemaRQ.jar```
4. To run the jar file on a different document, locate the new document in *root_dir* and use the 
following command: 
```java -jar DemaRQ.jar -document newDocument.docx```

### Using the evaluator: ###
To evaluate the results that are produced by the tool in the file "prediction.res", refer the follwing steps:
1. Replace the file "gold.txt" with the ground truth of the corresponding processed requirements specification, for which the results are in the output file "prediction.res".
2. Open a terminal and go to the *root_dir*. 
3. Use the following command: 
```python evaluate.py```

## hh
[![DOI](https://zenodo.org/badge/256534724.svg)](https://zenodo.org/badge/latestdoi/256534724)

## How to cite
- If you wish to use or compare with DemaRQ, please cite the following paper: 

[Abualhaija, S., Arora, C., Sabetzadeh, M., Briand, L. C., & Vaz, E. (2019, September). A Machine Learning-Based Approach for Demarcating Requirements in Textual Specifications. In 2019 IEEE 27th International Requirements Engineering Conference (RE) (pp. 51-62). IEEE.](https://orbilu.uni.lu/bitstream/10993/39889/1/AASBV_RE19_AuthorPreprint.pdf)
