# beans-dataset-classification
beans dataset classification

In this project, I am running two transfer learning models to classify images.  
The models I used are EfficientNetB6 and ViT.
## The dataset
![alt text](helper_scripts/samples.png)  
The beans dataset consists of leaf images taken in the field from different districts in Uganda by the Makerere AI lab.  
It is a well-known dataset for learning machine learning.  

The goal is to build a robust machine learning models that is able to distinguish between diseases in the Bean plants  

[Link to Dataset beans](https://github.com/AI-Lab-Makerere/ibean)

## The models
[EfficientNetB6](https://www.tensorflow.org/api_docs/python/tf/keras/applications/EfficientNetB6)   

[ViT-base-patch16-224](https://huggingface.co/google/vit-base-patch16-224)

## The process

I run the models with different parameters and selected the best results.  
In order to examine the models more thoroughly and compare them, i took the dataset and divided it into smaller random subsets.  

I used subsets of 150 images, 500 images, 750 images, and the entire dataset (approximately 1,000 images).
(The script for splitting the mock dataset into random image subsets is included in the scripts folder.)

Afterward, I run both models on each subset of images.

Note: The test and validation images remained unchanged across all subsets.



## The result

| Model                        | Accuracy | Precision | Recall | F1 Score | Running Time | Epochs 
|------------------------------|----------|-----------|--------|----------|--------------|---------|
| EfficientNetB6 (150)          | 0.90     | 91%       | 90%    | 90%      | 72m          |  46
| EfficientNetB6 (500)         | 0.91     | 92%       | 91%    | 91%      | 109m          | 29
| EfficientNetB6 (750)         | 0.94     | 94%       | 94%    | 94%      | 130m         | 28
| EfficientNetB6 (1000)        | 0.94     | 94%       | 94%    | 94%      | 175m         | 25
| ViT (google/vit-base)150     | 0.91     | 91%       | 91%    | 91%      | 8m           | 7
| ViT (google/vit-base)500     | 0.95     | 95%       | 95%    | 95%      | 12m          | 4
| ViT (google/vit-base)750     | 0.95     | 97%       | 97%    | 97%      | 19m          | 6
| ViT (google/vit-base)1000    | 0.98     | 99%       | 98%    | 98%      | 58m          | 18



![line plot result](helper_scripts/line_plot_with_labels.png)

### Number of Epochs  
The number of epochs was determined based on the best-performing metric,  
which in this case is the loss function.  
The final model selected is the one that achieved the best result in the loss function on the validation set. 

![epochs num result](helper_scripts/number_of_epochs.png)


## conclusions 
It can be observed that the results improve as the number of images increases.  

Additionally, the ViT-base-patch16-224 model demonstrates better performance overall.  
An important point is that the transformer model requires significantly fewer resources,  
which allows for more iterations and model improvement.  
  
In the transfer model, I didn’t add augmentation to the images because it reduced the performance of the results.  
Since the images were taken in field conditions with different backgrounds and from various angles, I believe it’s not necessary.  

However, for future use of the model, it’s recommended to ensure that overfitting doesn’t occur.