# ML Group Project

## Full Assignment Brief
### **ML Group project**

ML Group Project provides a practical avenue for applying theoretical knowledge, allowing us to actively engage in the model development process. Through these exercises, we will hone our skills in crafting tailored solutions to detect malware and identify malicious network traffic, bridging the gap between theory and practice. 

Students will work with their assigned group to collaboratively identify a dataset (our dataset is NSL-KDD). Each student should be able to showcase the progress of EDA and model development code in their code editor of choice weekly in class.

**Assignment Instructions**

This is your opportunity to tell a data story using ML models in a presentation. Be sure to incorporate all of the following elements:

- Introduce the real-world problem that can be solved with big data and ML techniques
- The dataset selected, including a reason for selecting the data
- The EDA and ML methodology and algorithms used to analyze the data
- Results of the EDA analysis and Advanced Analytics using ML techniques
- Conclusion, answers, or recommendations based on the analysis- Report
- Presentation in class room

Submission guidelines.  This is a group presentation. One submission per group, please include 

 

-  Data Set (NSL-KDD)
-  Combined Code script from all group members 
-  In-class presentation slide deck (add code snippets and group members), include business problem being solved, EDA, Predictive Prescriptive Analytics, ML algos used, metrics, conclusion, answers, or recommendations based on the project 

# Malware and Network Intrusion Detection and Analysis

Over the years, malware has evolved significantly, emerging as a pervasive global threat to our digital existence. The daily influx of malware has surged exponentially, posing a formidable challenge to security companies. These companies are tasked with scrutinizing hundreds of thousands of malicious samples daily, a workload that undeniably impacts their operational efficiency. This volume sometimes exceeds 1 million distinct files per day. Simultaneously, the classification of malware has attained heightened significance. New malware strains incorporate increasingly sophisticated techniques designed to outsmart signature-based detectors and operate discreetly for extended periods. As a result, security analysts find themselves in a race against time to detect malware, whether by scrutinizing the infected host or by monitoring the network through which the malware transmits data.

On top of that, malware designed to exploit network vulnerabilities operates stealthily, often eluding traditional security measures. These programs leverage intricate techniques, such as zero-day exploits and polymorphic code, to avoid detection by conventional signature-based defenses. As security companies grapple with the relentless onslaught of such network-exploiting malware, the stakes are higher than ever, necessitating continuous advancements in cybersecurity protocols.

AI introduces a novel perspective on malware detection, transitioning from delivering a binary verdict to providing intricate explanations. Its proficiency in discerning malicious scripts, especially those that have been obfuscated, surpasses the detection rates achieved by conventional methods in isolation. Notably, AI demonstrates greater efficacy in identifying malware and network intrusions, thereby improving exploit detection compared to relying solely on traditional tools.

# Datasets

Many datasets exist for training and testing malware classification and network intrusion detection algorithms. The following compilation offers a thorough and diverse list of such datasets to aid researchers and practitioners. You can use these or any other datasets to train your AI models.

## Malware analysis

Let’s first see some datasets that can be used for malware analysis:

- The NSL-KDD dataset: Recognized as a prominent resource for intrusion detection, the NSL-KDD dataset encompasses both normal and attack traffic. Though not exclusively tailored to malware, it serves broader cybersecurity objectives.

## Network intrusion detection

As for malware analysis, there exist datasets for network intrusion detection. Those datasets have been used in plenty of research papers and scientific projects. Here are some listed:

- NSL-KDD: As an updated iteration of the original KDD Cup 1999 dataset, the NSL-KDD dataset rectifies several shortcomings of its predecessor. It furnishes a more authentic depiction of network traffic, encompassing both normal and attack instances.

## **Phase I**

##### **Overview and Rationale**

In ML, it is important to extract meaningful insights from data that may not be obvious with traditional probability methods. This is due to the immense, dimensional, complex, heterogeneous, and distributed nature of the data. Data mining provides models and methods that generate insights from this data, which can influence business decisions.

This final project is an opportunity for you to build machine learning algorithms and data-mine such a dataset to identify key insights that answer key business questions and provide recommendations based on those insights. The file below provides the specific details on deliverables throughout this course.

Once your project dataset has been approved, work as a group to pre-process the data and complete an EDA. These steps will prepare you to build machine learning algorithms on the data. Explore the variables, data types, values, etc Calculate appropriate summary statistics and create appropriate graphs that will give you insights into the data. Include the answers to the following questions:

- What did you do with the data in the context of exploration?
- How many entries are in the dataset?
- Was there missing data? Duplications? How clean was the data?
- Were there outliers or suspicious data?
- What did you do to clean the data?
- What did you find? What intrigued you about the data? Why does that matter?
- What would your proposed next steps be?
- What business questions do you plan to answer with your ML algorithms?

*Place all code segments, tables, and graph output in appendices. Only include those referenced in the report and of interest in the next stages of data mining. ****Please be prepared to share your code on your computer in the classroom, individually.***

 

## **Phase II**

**Overview and Rationale**

ML is used to reveal hard-to-see and hidden patterns and relationships in Big Data datasets. ML algorithms helps to classify data for further examination or create models to predict outcomes for a different set of data. As ML experts, you should be able to explain how the code used to mine the data works and analyze and interpret the mining results. This allows you to summarize and clarify the results for stakeholders.

Include the answers to the following questions:

- What ML algorithms did you use and why? 
- What metrics did you use to measure the model

- Code walk-through: in this section provide a step-by-step explanation of how the code is interacting with and/or transforming the data. Provide examples from the output to support your explanations.
- Analysis: Based on the output, analyze the data and the relationships revealed about the variables of interest. Explains the insights provided by the output. Use visualizations to support your analysis.
- Interpretation and Recommendations: Interpret the results of your results of the machine learning analysis and explain what the results mean for the data owner. Provide recommendations for actions to be taken based on your interpretation. Support those with the data. Explain why and what explicit variables you suggest incorporating. 

Deliverables

- Write a 3-4 page report that summarizes your key findings.
- Prepare a slide deck to share the weekly iterative development progress with individual code snippets.
- Weekly code walkthrough to share your findings and iterative code development in the class room

Final Project - Group Presentation
[](https://northeastern.instructure.com/courses/210227/rubrics/336058?rubric_association_id=653877) [](https://northeastern.instructure.com/search/rubrics?q=) [](https://northeastern.instructure.com/courses/210227/rubric_associations/653877)

Final Project - Group Presentation

| 
Criteria | 
Ratings | 
Pts | 

| 

This criterion is linked to a Learning OutcomePresentations

 | 

30 to >27.9 ptsAbove StandardsGoes above the requirements of the assignment to provide tell a compelling story about the data that answers the questions posed in the written report.

27.9 to >21.0 ptsMeets StandardsProvides a summary of the report, highlighting main points about the data and the answer to the question(s) posed in the written report.

21 to >18.0 ptsApproaching StandardsProvides a summary of the written report, highlighting general themes about the data. Gives general answers to question(s) posed in the written report.

18 to >0 ptsBelow StandardsEither reads the report, providing too much detail, or does not focus on the data and methods to provide answers to questions.

 | 

30 pts

 | 

| 

This criterion is linked to a Learning OutcomeDesign

 | 

30 to >27.9 ptsAbove StandardsGoes beyond the requirements of the assignment to provide an innovative and engaging design.

27.9 to >21.0 ptsMeets StandardsIncorporates all required elements of content in a concise, organized and visually appealing design.

21 to >18.0 ptsApproaching StandardsIncorporates all required elements of content in an organized and pleasing design.

18 to >0 ptsBelow StandardsDoes not incorporate all the required elements of content or the design disorganized or unattractive.

 | 

30 pts

 | 

| 

This criterion is linked to a Learning OutcomeData Visualization

 | 

30 to >27.9 ptsAbove StandardsGoes beyond the requirements of the assignment to seamlessly integrate graphs, figures, charts and tables at critical stages of the presentation to tell a story.

27.9 to >21.0 ptsMeets StandardsIncorporates graphs, figures, charts and tables to help audience focus on main points and summarize the results of the report.

21 to >18.0 ptsApproaching StandardsIncorporates graphs, figures, charts and tables, but important points are lost in the data or visualizations. Is able to highlight the main results of the report.

18 to >0 ptsBelow StandardsDoes not incorporate graphs, figures, charts and tables or incorporates visualizations that are irrelevant to main points.

 | 

30 pts

 | 

| 

This criterion is linked to a Learning OutcomeMechanics

 | 

10 to >9.3 ptsAbove StandardsCompletely free of errors in grammar, spelling, and punctuation; and completely correct usage of title page, citations, and references.

9.3 to >7.0 ptsMeets StandardsThere are no noticeable errors in grammar, spelling, and punctuation; and completely correct usage of citations, and references.

7 to >6.0 ptsApproaching StandardsThere are very few errors in grammar, spelling, and punctuation; and completely correct usage of citations, and references.

6 to >0 ptsBelow StandardsThere are more than five errors in grammar, spelling, and punctuation; or the usage of citations, and references are incomplete.

 | 

10 pts

 | 

Total Points: 100

## Due Date
2026-04-04T03:59:59Z

## Retrieved Course Context
See `COURSE_CONTEXT.md` for supporting excerpts from course reference material.
