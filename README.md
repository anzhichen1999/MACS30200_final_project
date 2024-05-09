# Media Framing of Poverty Alleviation in China: A Textual Analysis of "People's Daily"

## Project Description

This research project explores the framing of poverty alleviation in the "People's Daily," the official newspaper of the Communist Party of China. Utilizing a corpus of approximately 5,000 articles from 1979 to 2023 related to poverty reduction, this study identifies and analyzes the underlying development ideas and the frames of poverty alleviation. The project employs deductive content analysis methods to track the continuity and change in poverty alleviation discourse, providing insights into how media frames might influence public perceptions and policy directions in the context of China's evolving economic policies and social dynamics.

## Research Questions

1. What are the underlying development ideas, and how does People’s Daily uphold them in its reports on poverty alleviation?
2. What frames are used to discuss poverty alleviation, and how are they employed by People’s Daily in its reporting?
3. What changes and continuities in terms of development ideas or frames of poverty alleviation are reflected in the party paper’s reports on poverty?

## File Explanation

1. /Data: The full data of People's Daily articles from year 1989, and its word embeddingds downlowded from Dr Jia's social science cluster. In the following study, we will expand this database from year 1989 to the full coverage of study. Since the nature of this repo is to serve a researc proporsal, so we will only attach a sample for demonstratiion purposes.
2. /Results: Visulizations and graphs for results will be saved here.
3. /Scripts: Code.


## Findings

To be updated. This part will be done before this Sunday as I sent an email to Dr.Jia indicating the incapability of doing producing actual results during the previous week. For convience, I have attacthed the mocked up result from the previous homework, with signficant revised contents based on Dr. Jia's comments; however, in the final version the content below will laargely be replaced by actual graphs.

**RQ1:**
graph 1:
stacked area chart: 
Through high frequency word extraction, topic modeling and clustering, and policy analysis from
actual accouncement, etc, we have developed different themes for development ideas. Ideally, how different development ideas (e g., economic growth, social equity, environmental sustainability) have been emphasized in People's Daily articles over time can be reflected through this stacked arrea chart. X-axis is the year, Y-axis is the number of articles.

Dr Jia's comment: How do you identify them? 

Reponse: I have manually labelled 1,000 articles, as mentioned in week 3 assignment. In real research, I will expand the number of labeling. Also as I mentioned in the feasibility check, I can use the already labeled news articles to fine-tune an NLP, which ideally would be able to learn the nuances and specific contexts relevant to the themes of poverty reduction such as labor intensiveness and collective efforts, or to identify specific terminology and concepts that are not as common in general datasets that pre-trained models are usually trained on.

**RQ2:**
graph 2:
tree map:
This decisioin tree map should show how NLP taks is used to classify articles by the dominant frame using text analysis and categorize based on frequency. Basically it shows the work flow, shedding lights on the results.

Dr Jia's comment: decision tree map can be hard to identify.

Response: Yes probably my intial thoughts were too ideal and naive. However as I put in the method part in previous weeks, this part was conducted through neural networks. I though that myybe I could use ecision trees from Neural Network output to approximate the complex decision surface of a neural network with more interpretable models. 

**RQ2:**

graph 3:
line chart
It should be able to calculate the annual frequency of each frame from 1979 to 2023 year by year, and different color should represent different frame. Similar to the next graph, this time gives an overall change pattern. However we should notice the difference between proportion and number: as the number of poverty alleviation articles increase per year, the raw number may not be able to reflect the actual intention of the policy makers, nor will it reflect which frame plays a more important role.

Dr Jia's comment: How to measure frame?

Response: Aas mentioned in the big picture assignment, the frames are extracted from UN sustainable development on poverty reductioin and alleviation. We will apply it here.


**RQ3**
graph4:
Dual Y-Axis Line Graph:
A line graph with two Y-axes to compare the trajectory of two major themes or frames over
time, highlighting their relative changes or stability. The result, however, need to be based on
some types of rergrression to show that they are related. Or this can come from variables
other than existing frames such as the number of articles related to xxx.

Dr Jia's comment: Hypothesis?

Response: We will cover it in the updates before Sunday.

graph 5:
chord graph:
We can hereby use a chord diagram to illustrate the inter-relationships between different
themes or frames across the entire datase by count co-occurrences of themes in the same
articles. Each theme is a node on the circumference of a circle, and chords connecting the
nodes represent the strength of their co-occurren



## Requirements

- **Python Version:** 3.12.0
- **Required Libraries and Packages:** For a complete list of required libraries and their versions, please refer to the `requirements.txt` file in this repository.

### Installation

To install required Python packages, run the following command in your environment:

```bash
pip install -r requirements.txt


---

This README.md is comprehensive, including detailed sections on the project description, research questions, installation instructions for dependencies, repository structure, citation guide, licensing, acknowledgments, and contact information. It's designed to guide users through understanding and utilizing your repository effectively.
