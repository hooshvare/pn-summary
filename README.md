# Leveraging ParsBERT and Pretrained mT5 for Persian Abstractive Text Summarization


Paper presenting: arXiv:2012.11204

Paper link: https://arxiv.org/pdf/2012.11204.pdf


## Introduction
Natural Language Processing (NLP) is a field of AI that focuses on processing textual information in order to make them comprehendable to computers. With the emergence of Deep Learning (DL), numerous DL-based models and architectures have been proposed for different NLP tasks such as Named Entity Recognition (NER), Sentiment Analysis (SA) and Question/Answering (QA). One of the most recent and most popular approaches towards these tasks is to use pre-trained language models. Pre-trained language models used for NLP tasks are essentially huge neural networks employing Long Short-Term Memory (LSTM) architcture that are trained on enormous text corpus. A few examples include <a href="https://arxiv.org/abs/1810.04805">BERT</a> and <a href="https://arxiv.org/abs/1910.10683">T5</a> models.  <a href="https://arxiv.org/abs/1810.04805">BERT</a> is an encoder-only model that uses Masked Language Model (MLM) to create joint conditioning on left and right context. <a href="https://arxiv.org/abs/1910.10683">T5</a> is a sequence-to-sequnce (seq2seq) framework that creates a text-to-text format to address NLP tasks. However, regardless of the architecture, any pre-trained model has to be fine-tuned towards any of the NLP tasks using an appropriate dataset.

There are numerous NLP datasets available for different tasks, especially for the English language. Some tasks, however, have had a lesser fortune regarding the amount of textual data available. This lack of available data is more tangible in languages other than English. One of the NLP tasks that could highly benefit from more comprehensive and well structured datasets, is text summarization. Text summarization is a text generation problem that could be viewed as a seq2seq mapping. The most challenging issue in text summarization, is to retain as much information as possible while compressing the original text into a very compact format. Decoder-only or encoder-decoder models can be utilized to address this task, if the necessary dataset is available to either train or fine-tune them.

In this repository, a novel and well structured dataset for Persian text summarization (pn-summary) is presented. In the next few sections, first we introduce the statistical features of this dataset. Then, we present the evaluation metrics that could be used to measure the performance of any model trained on this dataset. The results obtained from two different models in terms of said metrics are also presented.

## Dataset Information
The pn-summary dataset is composed of numerous articles of various categories that have been crawled from six news agency websites. Each document (article) includes the long original text as well as a human generated summary. The number of articles per news agency is depicted in below figure. The total number of articles is 93,207.

<img src='/assets/news_agencies.png' width="50%" height="50%"/>

This dataset includes 18 different article categories from economy to tourism. The distribution of these categories are shown below. The category with highest and lowest number of articles are oil-energy and tourism, respectively. The top five categories are oil-energy, local, economy, international and society.

<img src='/assets/categories_dist.png' width="50%" height="50%"/>

Summaries included in each article have variable lengths. As shown in the next figure, most articles have summaries with around 27 tokens. Rarely it happens that a summary has 75 tokens and almost none have 100 or more tokens. This shows that summaries included in this dataset are sufficiently short.

<img src='/assets/summary_tokens.png' width="50%" height="50%"/>

## Evaluation
To evaluate the performance of any model trained on pn-summary dataset, we suggest <a href="https://www.aclweb.org/anthology/W04-1013/">Google's ROUGE</a> (Recall-Oriented Understudy for Gisting Evaluation) metric package. ROUGE metric package is widely used automatic text summarization and machine translation evaluation. The metrics compare the generated summary with the original summary included in the article (document). Therefore, to establish the performance of any text summarization model, one can calculate the F-1 score for these metrics.

In our most recent work ###, which is the first work to address Persian text summarization from an abstractive point-of-view, we have reported the results of fine-tuning two models on the current dataset in terms of three ROUGE metrics:

1. __ROUGE-1 (unigram) scoring__: which computes the unigrams' overlap between the generated and the original summary.
2. __ROUGE-2 (bigram) scoring__: which computes the bigrams' overlap between the generated and the original summary.
3. __ROUGE-L scoring__: which computes the Longest Common Subsequence (LCS) between the the generated and the original summary. In this metrics scores are sentence-level and new lines are neglected.

ROUGE by default does not support the PErsian language. Therefore, we have also created an extension to these metrics to further support the Persian language. This extension is available <a href="#">here</a>.

The models proposed to be used for Persian summary generation in our work are <a href="https://arxiv.org/abs/2010.11934">mT5</a> (a multilingual version of the T5 model) and a <a href="https://arxiv.org/pdf/1907.12461.pdf">BERT2BERT</a> structure warm-started with <a href="https://arxiv.org/abs/2012.11204">ParsBERT</a> model's weights. This is the very first work ever that have used the pn-summary dataset. Therefore, results reported in this work can be used as a baseline for any future work in this field that uses the pn-summary dataset. The results obtained by these models on the pn-summary dataset are presented in the table below:

|                   |  ROUGE-1  |  ROUGE-2  | ROUGE-L   |
|:-----------------:|:---------:|:---------:|-----------|
| B2B with ParsBERT | __44.01__ | __25.07__ | __37.76__ |
|        mT5        |   42.25   |   24.36   | 35.94     |

As it can be seen from the table above, the ParsBERT-based BERT2BERT outperforms the mT5 model. This may be due to the fact that ParsBERT, unlike mT5, is a monolingual BERT model that has exclusively been trained over a very large Persian text corpus, thus, capable of absorbing the Persian textual information in a more efficient way.

## Summarization Strategy
After the models are fine-tuned on the pn-summary dataset, a summarization strategy should be deployed to put the model into use to actually generate summaries. There are different decoding techniques such as _greedy searcg_ and _beam search_. In our work we have used the beam search method to generate summaries after fine tuning our models. 

Beam search method tries to maximize the word sequence probability by considering multiple possible sequences (beams) and choosing the one that results in greater conditional next word probability product. This is to avoid highly probable words being neglected only because they are stuck behind a low probability word. To prevent beam search from generating the sequences with repetitive words, we have used n-grams penalties. The overall beam search configuration used in our work is outlined in the table below. In this table the early stopping indicates whether the beam search algorithm should stop when when all beams rach EOS token.

|                        | BERT2BERT |   mT5  |
|:----------------------:|:---------:|:------:|
|     Number of Beams    |     3     |    4   |
| Repetitive N-gram Size |     2     |    3   |
|     Length Penalty     |     2     |    1   |
|     Early Stopping     |   ACTIVE  | ACTIVE |

## A Few Examples
In this section, we have included a few examples from the results of the models presented in our paper. To make these examples more comprehendable, we have included both Persian and English versions of the example texts in the table below.

<table class="tg">
<thead>
  <tr>
    <th class="tg-c3ow"></th>
    <th class="tg-c3ow">English</th>
    <th class="tg-c3ow">Persian</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-c3ow"># Example</td>
    <td class="tg-c3ow" colspan="2">1</td>
  </tr>
  <tr>
    <td class="tg-c3ow">Article Text</td>
    <td class="tg-c3ow">Example 1 text</td>
    <td class="tg-c3ow">متن خبر اول</td>
  </tr>
  <tr>
    <td class="tg-c3ow">Original Summary</td>
    <td class="tg-c3ow">Example 1 original summary</td>
    <td class="tg-c3ow">خلاصه اصلی</td>
  </tr>
  <tr>
    <td class="tg-c3ow">B2B Summary</td>
    <td class="tg-c3ow">Example 1 B2B Summary</td>
    <td class="tg-c3ow">خلاصه B2B</td>
  </tr>
  <tr>
    <td class="tg-lduz">mT5 Summary</td>
    <td class="tg-lduz">Example 1 mT5 Summary</td>
    <td class="tg-lduz">خلاصه mT5</td>
  </tr>
  <tr>
    <td class="tg-lduz"># Example</td>
    <td class="tg-lduz" colspan="2">2</td>
  </tr>
  <tr>
    <td class="tg-lduz">Article Text</td>
    <td class="tg-lduz">Example 2 text</td>
    <td class="tg-lduz">متن خبر دوم</td>
  </tr>
  <tr>
    <td class="tg-lduz">Original Summary</td>
    <td class="tg-lduz">Example 2 Original Summary</td>
    <td class="tg-lduz">خلاصه اصلی</td>
  </tr>
  <tr>
    <td class="tg-lduz">B2B Summary</td>
    <td class="tg-lduz">Example 2 B2B Summary</td>
    <td class="tg-d8bh">خلاصه B2B</td>
  </tr>
  <tr>
    <td class="tg-lduz">mT5 Summary</td>
    <td class="tg-lduz">Example 2 mT5 Summary</td>
    <td class="tg-lduz">خلاصه mT5</td>
  </tr>
</tbody>
</table>

As it can be seen from the table above, the summaries given by ParsBERT driven BERT2BERT model are quite closer to the actual summary in terms of both in meaning and lexical choices
 
## Citation
...

## Contributors
...


## License
[MIT License](LICENSE)
