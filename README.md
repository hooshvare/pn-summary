# Leveraging ParsBERT and Pretrained mT5 for Persian Abstractive Text Summarization


Paper presenting: arXiv:2012.11204

Paper link: https://arxiv.org/pdf/2012.11204.pdf


## Introduction
Natural Language Processing (NLP) is a field of AI that focuses on processing textual information in order to make them comprehendable to computers. With the emergence of Deep Learning (DL), numerous DL-based models and architectures have been proposed for different NLP tasks such as Named Entity Recognition (NER), Sentiment Analysis (SA) and Question/Answering (QA). One of the most recent and most popular approaches towards these tasks is to use pre-trained language models. Pre-trained language models used for NLP tasks are essentially huge neural networks employing Long Short-Term Memory (LSTM) architcture that are trained on enormous text corpus. A few examples include BERT and T5 models.  BERT is an encoder-only model that uses Masked Language Model (MLM) to create joint conditioning on left and right context. T5 is a sequence-to-sequnce (seq2seq) framework that creates a text-to-text format to address NLP tasks. However, regardless of the architecture, any pre-trained model has to be fine-tuned towards any of the NLP tasks using an appropriate dataset.

There are numerous NLP datasets available for different tasks, especially for the English language. Some tasks, however, have had a lesser fortune regarding the amount of textual data available. This lack of available data is more tangible in languages other than English. One of the NLP tasks that could highly benefit from more comprehensive and well structured datasets, is text summarization. Text summarization is a text generation problem that could be viewed as a seq2seq mapping. Decoder-only or encoder-decoder models can be utilized to address this task, if the necessary dataset is available to either train or fine-tune them.

In this repository, a novel and well structured dataset for Persian text summarization (pn-summary) is presented. In the next few sections, first we introduce the statistical features of this dataset. Then, we present the evaluation metrics that could be used to measure the performance of any model trained on this dataset. The results obtained from two different models in terms of said metrics are also presented.

## Dataset Information
The pn-summary dataset is composed of numerous articles of various categories that have been crawled from six news agency websites. The number of articles per news agency is depicted in figure 1. The total number of articles is 93,207.

<img src='/assets/news_agencies.png' width="50%" height="50%" display="block" margin_left="auto" margin_right="auto"/>


## Evaluation
...

## Citation
...

## Contributors
...


## License
[MIT License](LICENSE)
