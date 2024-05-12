# Media Framing of Poverty Alleviation in China: A Textual Analysis of "People's Daily"

## Project Description

This research project explores the framing of poverty alleviation in the "People's Daily," the official newspaper of the Communist Party of China. Utilizing a corpus of approximately 5,000 articles from 1979 to 2023 related to poverty reduction, this study identifies and analyzes the underlying development ideas and the frames of poverty alleviation. The project employs deductive content analysis methods to track the continuity and change in poverty alleviation discourse, providing insights into how media frames might influence public perceptions and policy directions in the context of China's evolving economic policies and social dynamics.

## Research Questions

1. What are the underlying development ideas, and how does People’s Daily uphold them in its reports on poverty alleviation?
2. What frames are used to discuss poverty alleviation, and how are they employed by People’s Daily in its reporting?
3. What is the gap between People's Daily's report and the actual data and what might be the cause?

## File Explanation

1. /Data: The full data of People's Daily articles from year 1989, and its word embeddingds downlowded from Dr Jia's social science cluster. In the following study, we will expand this database from year 1989 to the full coverage of study. Since the nature of this repo is to serve a researc proporsal, so we will only attach a sample for demonstratiion purposes.
2. /Results: Visulizations and graphs for results will be saved here.
3. /Scripts: Code.
4. /Model: Model used for this code, which will be explained below.

## Model

1. Grave, E., Bojanowski, P., Gupta, P., Joulin, A., & Mikolov, T. (2018). Learning word vectors for 157 languages. In Proceedings of the International Conference on Language Resources and Evaluation (LREC 2018).

It is a word embedding model for Chinese language. However, it is about 7Gb. So I delete it from local machine and instead you may want to use the following code in the terminal to download it and store it in desired path.

"
wget https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.zh.300.bin.gz
gzip -d cc.zh.300.bin.gz
"


## Findings

To be updated. This part will be done before this Sunday as I sent an email to Dr.Jia indicating the incapability of doing producing actual results during the previous week. For convience, I have attacthed the mocked up result from the previous homework, with signficant revised contents based on Dr. Jia's comments; however, in the final version the content below will laargely be replaced by actual graphs.

**RQ1:**

Graph 1 - Stacked Area Chart: 

Through high frequency word extraction, topic modeling and clustering, and policy analysis from actual accouncement, etc, we have developed different themes for development ideas. Ideally, how different development ideas (e g., economic growth, social equity, environmental sustainability) have been emphasized in People's Daily articles over time can be reflected through this stacked arrea chart. X-axis is the year, Y-axis is the number of articles.

Dr Jia's comment: How do you identify them? 

Reponse: I have manually labelled 100 articles, as mentioned in week 3 assignment. In real research, I will expand the number of labeling to fine-tune the NLP model. Also as I mentioned in the feasibility check, I can use the already labeled news articles to fine-tune an NLP, which ideally would be able to learn the nuances and specific contexts relevant to the themes of poverty reduction such as labor intensiveness and collective efforts, or to identify specific terminology and concepts that are not as common in general datasets that pre-trained models are usually trained on.

**RQ2:**

Graph 2 - Tree Map:

This decisioin tree map should show how NLP taks is used to classify articles by the dominant frame using text analysis and categorize based on frequency. Basically it shows the work flow, shedding lights on the results.

Dr Jia's comment: decision tree map can be hard to identify.

Response: Yes probably my intial thoughts were too ideal and naive. However as I put in the method part in previous weeks, this part was conducted through neural networks. I though that myybe I could use ecision trees from Neural Network output to approximate the complex decision surface of a neural network with more interpretable models. 

Graph 3 - Line Chart

It should be able to calculate the annual frequency of each frame from 1979 to 2023 year by year, and different color should represent different frame. Similar to the next graph, this time gives an overall change pattern. However we should notice the difference between proportion and number: as the number of poverty alleviation articles increase per year, the raw number may not be able to reflect the actual intention of the policy makers, nor will it reflect which frame plays a more important role.

Dr Jia's comment: How to measure frame?

Response: Aas mentioned in the big picture assignment, the frames are extracted from UN sustainable development on poverty reductioin and alleviation. We will apply it here.

Graph 4 - Dual Y-Axis Line Graph:

A line graph with two Y-axes to compare the trajectory of two major themes or frames over
time, highlighting their relative changes or stability. The result, however, need to be based on
some types of rergrression to show that they are related. Or this can come from variables
other than existing frames such as the number of articles related to xxx.

Dr Jia's comment: Hypothesis?

Response: We will cover it in the updates before Sunday.

Graph 5 - Chord Graph:

We can hereby use a chord diagram to illustrate the inter-relationships between different
themes or frames across the entire datase by count co-occurrences of themes in the same
articles. Each theme is a node on the circumference of a circle, and chords connecting the
nodes represent the strength of their co-occurren

**RQ3:**

Graph 6 - Bar Graphs for Comparative Analysis:

We then use side-by-side or stacked bar graphs to compare the frequency and type of themes or frames used in People's Daily articles against actual data on poverty alleviation over the same periods. This visual can effectively show discrepancies and align with trends.

Graph 7 - Scatter Plot with Trend Lines:

Plot People's Daily coverage (e.g., number of articles or intensity of coverage) on one axis against actual poverty alleviation data (like poverty rates or government spending on poverty) on the other axis for each year. Add trend lines for each dataset to visualize divergence or convergence over time.

## Requirements

- **Python Version:** 3.11.5
- **Required Libraries and Packages:** For a complete list of required libraries and their versions, please refer to the `requirements.txt` file in this repository.

## Citation

Anzhi, C. (2024). Media Framing of Poverty Alleviation in China: A Textual Analysis of "People's Daily". Version 1.0. University of Chicago. https://github.com/anzhichen1999/MACS30200_final_project.git

### Installation

To install required Python packages, run the following command in your environment:

```bash
pip install -r requirements.txt



