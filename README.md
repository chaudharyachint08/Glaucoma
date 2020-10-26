# Glaucoma

## Steps to be followed
- [ ] Contrast adjustment e.g. CLACHE
- [ ] Outlier Detection for removal of Non-gradable images (Capturing Novelty and Removing Anamoly)
- [ ] Data Augmentation and Debiasing using VAE/GAN
- [ ] Image Classification Train & Test (10-crop) time augmentation
https://machinelearningmastery.com/best-practices-for-preparing-and-augmenting-image-data-for-convolutional-neural-networks/
- [ ] OpenAI Gradient Checkpointing (20% slow train with sqrt(N) Memory Usage)
- [ ] IMAGENET, Fine-Tuned and Self-supervised Transfer Learning
- [ ] Grad-Cam for Attention Region, and Averaging over Ensembles
- [ ] K-FAC (Second order approximation for DL)
- [ ] Shared convolutions
- [ ] Probabilitic Sampling Algorithm for Better Training
- [ ] Private Aggregation of Teacher Ensembles (PATE) with Sampling over soft labels and sample weights
- [ ] KL-Divergence & other loss functions for learning approximate probability distribution
- [ ] Cyclic Learning rate, for Auto-matic Ensembling during training
- [ ] Attention Mechanism in Architecture Design
- [ ] Trying out input in various color space, e.g. RGB, YUV, HSV and GREY
- [ ] Tensorflow Differentially Privacy
- [ ] Convolutional model shuffling during training with shared fully connected part


## Labeled Dataset Description

### Glaucoma Only Dataset Description

| Dataset Name                       | (  Healthy, Glaucoma) | URL 
|------------------------------------|----------------------|--------------------------------------------
| ACRIMA                             | (      309,      396) | https://figshare.com/articles/CNNs_for_Automatic_Glaucoma_Assessment_using_Fundus_Images_An_Extensive_Validation/7613135
| HRF                                | (       15,       15) | http://www5.cs.fau.de/research/data/fundus-images/
| ORIGA                              | (      482,      168) | https://drive.google.com/drive/folders/1VPCvVsPgrfPNIl932xgU3XC_WFLUsXJR
| Drishti-GS1                        | (       31,       70) | https://cvit.iiit.ac.in/projects/mip/drishti-gs/mip-dataset2/Home.php
| REFUGE-1                           | (     1080,      120) | http://ai.baidu.com/broad/subordinate?dataset=gon ; https://refuge.grand-challenge.org/Download/
| RIM-ONE-v2                         | (      255,      200) | http://medimrg.webs.ull.es/research/retinal-imaging/rim-one/
| RIM-ONE-v3                         | (       85,       74) | http://medimrg.webs.ull.es/research/retinal-imaging/rim-one/
| Kaggle_GlaucomaDataset_HimanshuAgg | (      511,      511) | https://www.kaggle.com/himanshuagarwal1998/glaucomadataset/discussion
| Total                              | (     2768,     1554) | 4322 Labeled Images (link YET-TO-DECLARED)


## Multi-class/label Dataset Description
<pre>
Normal (N), Diabetes (D), Glaucoma (G), Cataract (C), AMD (A), Hypertension (H), Myopia (M), Other diseases/abnormalities (O)
</pre>
| Dataset Name   | (  Train+Valid, Test) | Comments                  | URL 
|----------------|-----------------------|---------------------------|--------------------------------------------
| Kaggle_ODIR-5K | (         7000, 1000) | Test Set labels not given | https://www.kaggle.com/andrewmvd/ocular-disease-recognition-odir5k

## Unlabeled Dataset Description

| Dataset Name    | Count | URL 
|-----------------|-------|------------------------------------------------------------
| RIGA            |   749 | https://deepblue.lib.umich.edu/data/concern/data_sets/3b591905z?locale=en

## Related Literature

| Year | URL
|------|-------------
| 2020 | https://arxiv.org/abs/2005.02258
| 2020 | https://arxiv.org/abs/2002.08013
| 2019 | https://link.springer.com/article/10.1186/s12938-019-0649-y
| 2019 | https://arxiv.org/abs/1910.03667
| 2018 | https://arxiv.org/abs/1810.13376
| 2018 | https://arxiv.org/abs/1809.03239
| 2018 | https://arxiv.org/abs/1805.07549


## TIPS Section
Hoping to get something best out of it :)

## Notes section

https://hzfu.github.io/index.html#Project-page

Note: Above professor mentions about REFUGE2 (REtinal FUndus Glaucoma ChallengE), 2nd version of challenge
Here 1200 images from 2 devices will be released as training data at first. Hence has registered into the same

Kindly look into BIOMASA http://biomisa.org/index.php/downloads/
There request for the dataset is not working, please contact the authors of this website.
They also have their labeled dataset, and we can get much rich dataset from that
