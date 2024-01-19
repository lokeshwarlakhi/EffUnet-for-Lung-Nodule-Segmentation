# Lung Nodule Segmentation Using Residual Unet
Lung cancer detection often relies on interpreting subtle nodules in CT scans, a task demanding precise segmentation tools beyond simple image classification models. While existing methods utilizing other architectures might achieve decent accuracy, they often struggle with limited CT scan datasets and scalability, hindering their real-world impact. Our research addresses the imperative need for enhanced lung cancer detection by integrating the Residual U-Net architecture with the Luna16 dataset. . In comparison to a model using a transformer, U-Net, and global average pooling with the LIDR-IDRI dataset achieving training and testing accuracies of 87.90% and 84.62% respectively, our proposed model excels in feature extraction and overcoming vanishing gradients, ensuring sharper and more accurate nodule segmentation in CT scans. The Luna16 dataset, a diverse and annotated benchmark, facilitates comprehensive learning and adaptability to various nodule types and imaging conditions. What sets our model apart is the integration of Visual Explainability Techniques, including overlaying heatmaps on input images, visualizing attention weights, and generating Grad-CAM and Integrated Gradients images. These techniques highlight the regions that influenced the model's predictions, offering users insights into the model's decision-making process. Furthermore, our model provides textual explanations through human-readable summaries and the ability to answer specific user questions about the output, utilizing NLP techniques.

## Table of Contents

- [Lung Nodule Segmentation Using Residual Unet](#lung-nodule-segmentation-using-residual-unet)
  - [Table of Contents](#table-of-contents)
  - [Getting Started ](#getting-started-)
    - [Prerequisites](#prerequisites)
    - [Installing](#installing)
  - [Usage ](#usage-)

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them.

```
Give examples
```

### Installing

A step by step series of examples that tell you how to get a development env running.

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo.

## Usage <a name = "usage"></a>

Add notes about how to use the system.

