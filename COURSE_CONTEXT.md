# Course Context

This file contains relevant excerpts retrieved from course reference material.

## Match 1: 4.6 Assignment: Knowledge Representation System
- Source: Canvas Module: Module 4: Reasoning in AI
- Distance: 0.0050

Module: Module 4: Reasoning in AI

Item: 4.6 Assignment: Knowledge Representation System

Type: Assignment

## Module 4
 4.6 Assignment: Knowledge Representation System

### Overview

You will design, implement, and evaluate a knowledge representation system for a domain of your choosing. This assignment integrates the theoretical concepts of knowledge representation, ontologies, and reasoning covered in Modules 3 and 4, requiring you to apply predicate logic, develop formal ontologies, and implement rule-based reasoning systems.

Note that this discussion is required/graded.

This assignment should demonstrate that you can:

- Apply predicate logic to formally represent domain knowledge
- Design and implement ontologies using appropriate tools and methodologies
- Develop rule-based reasoning systems with forward and backward chaining
- Evaluate the expressiveness and limitations of different knowledge representation approaches
- Demonstrate competency in ontology development tools and/or semantic reasoning libraries

###  Instructions

#### Assignment brief

Select each title to view information on the assignment requirements. Open all sections simultaneously by selecting the Expand All Panels button     .  

#### 1. Domain selection and scope definition

Select a specific domain area that interests you (e.g., healthcare diagnostics, financial risk assessment, cybersecurity threat analysis, supply chain management, environmental monitoring, etc.).

Your chosen domain should be:

- Sufficiently complex to demonstrate meaningful knowledge representation concepts (i.e., not too simple a domain)
- Well-bounded to allow comprehensive coverage within the scope of this assignment (i.e., not too complex a domain)
- Rich in relationships between entities, properties, and rules
- Amenable to rule-based reasoning with clear inference patterns

#### 2. Technical implementation

Choose one of the following implementation approaches:

- 
**Option A: Protégé-based implementation**

Develop your ontology using Protégé 5.x
- Define classes, properties, individuals, and axioms
- Implement SWRL rules for reasoning
- Use a reasoner (HermiT, Pellet, or FaCT++) for inference
- Demonstrate query answering using SPARQL or DL queries

- 
**Option B: Python with pykg2vec**

Implement knowledge graph embeddings for your domain
- Create entity and relation embeddings
- Demonstrate link prediction or knowledge completion tasks
- Evaluate embedding quality using appropriate metrics

- 
**Option C: Python with semantic libraries**

owlready2: Manipulate OWL ontologies programmatically
- pronto: Work with OBO format ontologies
- OAK: Use the Ontology Access Kit for ontology operations

#### Note

- Alternative tools or libraries require instructor approval. Check with your instructor prior to using a tool not listed above.
- 
If you wish to gain experience and get instructor feedback on multiple approaches, you may choose multiple options above. 

You should specify one to be your primary implementation, which will be used to determine the bulk of your grade. 
- The secondary implementation will be mainly for additional feedback for you.

#### 3. System components

Your implementation must include:

3.1 Formal ontology structure

- Classes and hierarchies: Organize domain concepts using subsumption relationships
- Properties: Define object properties (relationships) and data properties (attributes)
- Axioms and constraints: Specify domain and range restrictions, cardinality constraints, and disjointness
- Individuals: Populate your ontology with representative instances

3.2 Rule-based reasoning system

- Production rules: Implement at least five meaningful inference rules using your chosen framework.
- Reasoning strategy: Demonstrate both forward chaining (data-driven) and backward chaining (goal-driven) inference where applicable.
- Consistency checking: Ensure your ontology is logically consistent.

3.3 Query and inference capabilities

- Competency questions: Define and answer at least eight domain-specific queries that demonstrate your system's capabilities.
- Reasoning examples: Show how new knowledge is inferred from existing facts and rules.
- Classification: Demonstrate automatic classification of new instances.

#### 4. System demonstration

Provide a comprehensive demonstration that includes:

- Knowledge base population: Show how domain knowledge is represented.
- Rule execution: Demonstrate inference processes with step-by-step reasoning traces.
- Query processing: Execute various types of queries (simple lookup, complex reasoning, classification).
- Edge cases: Show how your system handles incomplete information or conflicting data.

#### Deliverables

Select each title to view information on the assignment deliverables. Open all sections simultaneously by selecting the Expand All Panels button     .  

#### 1. Technical artifacts

- For **Protégé implementation**, submit the following:

.owl ontology file(s)
- .swrl rules file (if separate)
- Screenshots of key ontology views (class hierarchy, property definitions, individuals)
- Query results and reasoning traces

- 
For **Python implementation**, submit the following:

Complete Python code with clear documentation
- Requirements file (requirements.txt or equivalent)
- Sample data files
- Output demonstrations (visualizations, query results, reasoning traces)

#### 2. Technical report (APA Style)

Submit a report (2,500-3,500 words) structured following APA style:

- 
**Abstract (150-200 words)**

Provide a concise summary of your domain, approach, key findings, and contributions.

- ** Introduction**

- Explain your problem motivation and domain significance
- Define the scope and boundaries of your knowledge representation system
- Outline the research questions or competency requirements you addressed

- ** Background and literature review**

- If any previous models of this domain exist, provide a brief review of those approaches
- Justify your chosen representation methodology

- ** Methodology and system design**

- Domain analysis: Provide a detailed description of your chosen domain
- Conceptual model: Present a high-level overview of key concepts and relationships
- Knowledge representation framework: Justify your chosen tools/libraries
- Ontology design patterns: Describe the patterns and principles you applied

- ** Implementation**

- Ontology structure: Provide a detailed description of your classes, properties, and axioms with rationale
- Rule design: Explain your inference rules with logical formulations
- Technical architecture: Describe your system components and their interactions
- Include UML diagrams, ontology visualizations, or system architecture diagrams

- ** Evaluation and results**

- Reasoning performance: Present examples of successful inferences with explanations
- Consistency and completeness: Analyze the logical consistency and coverage of your system
- Limitations identified: Discuss what your system cannot represent or infer

- ** Critical analysis**

- Expressiveness vs. computational complexity: Analyze your representation choices
- Alternative approaches: Briefly discuss other possible representations you considered, discuss how those alternatives might have changed your results.
- Scalability considerations: Discuss performance implications with larger knowledge bases

- ** Conclusion**

- Summarize your results, highlight key takeaways
- Reflect on what your system reveals or suggests about your domain (did you discover any new knowledge about your domain)
- Suggest future work and potential extensions
- Your conclusions should be written as a report to a superior at a place of employment. You want to highlight what was learned about the domain that would help them. The conclusions should not be about what you learned about python, protégé, or any of the libraries.

- 
**References**

Cite any sources in APA format, this includes where you got information about your domain, such as Wikipedia. If you consulted Claude or Copilot to aid in any portion of your work, cite the AI as well. If Gemini aided you in debugging code, include that in your references. Also include any relevant papers on knowledge representation, ontologies, and domain-specific applications that you consulted.

- 
**Code documentation and comments**

All code must be thoroughly documented with:

Clear function/method documentation
- Inline comments explaining complex logic
- README file with setup and execution instructions
- Example usage demonstrations

#### Evaluation

Select each tab to learn how your assignment will be evaluated.

### Technical implementation

Technical implementation (40 points) criteria:

- Correctness: System functions as designed without errors
- Completeness: All required components are implemented
- Code quality: Clean, well-structured, and documented code
- Tool proficiency: Effective use of chosen development tools

Select the next tab to learn more.

### Knowledge representation quality

Knowledge representation quality (25 points) criteria:

- Domain modeling: Accurate and comprehensive representation of domain concepts
- Ontology design: Proper use of classes, properties, axioms, and design patterns
- Rule formulation: Logically sound and meaningful inference rules
- Expressiveness: Ability to represent complex domain relationships

Select the next tab to learn more.

### Reasoning and inference

Reasoning and inference (20 points) criteria:

- Rule execution: Correct implementation of forward/backward chaining
- Query answering: Successful resolution of competency questions
- Consistency: Logically consistent knowledge base
- Explanation: Clear demonstration of reasoning processes

Select the next tab to learn more.

### Report quality

Report quality (15 points) criteria:

- Technical writing: Clear, professional, and well-structured presentation
- Analysis depth: Thoughtful discussion of design choices and limitations
- APA compliance: Proper formatting, citations, and references
- Visual documentation: Effective use of diagrams and figures

#### Submission guidelines

- Report: PDF format, APA style, 12pt Times New Roman, double-spaced
- Code: Python 3.8+ with virtual environment specifications (if Python was used)
- Ontologies: OWL format compatible with Protégé 5 (if Protégé was used)

#### Additional resources

Recommended tools and libraries:

- [Protégé](https://protege.stanford.edu/)
- [owlready2](https://pypi.org/project/Owlready2/)
- [pronto](https://pypi.org/project/pronto/)
- [pykg2vec](https://pypi.org/project/pykg2vec/)
- [OAK](https://incatools.github.io/ontology-access-kit/)

Ontology design resources:

- [OBO Foundry Principles](http://obofoundry.org/principles/)
- [Ontology Design 101](https://protege.stanford.edu/publications/ontology_development/ontology101.pdf)
- [FAIR Data Principles](https://www.nature.com/articles/sdata201618) 

#### Academic integrity

This is an individual assignment. While you may discuss general concepts with classmates, all implementation work and written analysis must be your own. Proper attribution is required for any external resources, datasets, or code libraries used; this includes generative AI and large language models. See the course syllabus for clarification.

Once you have completed this assignment, select Next to explore the module summary.

Icon Progress Bar (browser only)

## Match 2: 2. 6 Decision Trees, Linear Discriminant Analysis, and Naive Bayes Classification
- Source: Canvas Module: Module 2: Machine Learning 1: Learning from Observations; Learning Decision Trees.
- Distance: 0.0054

Module: Module 2: Machine Learning 1: Learning from Observations; Learning Decision Trees.

Item: 2. 6 Decision Trees, Linear Discriminant Analysis, and Naive Bayes Classification

Type: Page

## Module 9
 9.6 Decision Trees, Linear Discriminant Analysis, and Naive Bayes Classification

### The decision process

A decision tree makes predictions by following a series of binary decisions from the root to a leaf.

- Start at root: Ask the first question about the data
- Follow branches: Based on the answer, move to left or right child
- Continue recursively: Ask subsequent questions at each internal node
- Reach leaf: Make prediction based on the leaf node's label

#### Example: Should I play tennis?

Consider deciding whether to play tennis based on weather conditions:

```
Root: Is Outlook = Sunny?

├─ No: Is Outlook = Overcast?

│  ├─ Yes: Play Tennis ✓

│  └─ No: Is Wind = Strong?

│     ├─ Yes: Don't Play ✗

│     └─ No: Play Tennis ✓

└─ Yes: Is Humidity = High?

   ├─ Yes: Don't Play ✗

   └─ No: Play Tennis ✓

```

For a new day with Outlook=Sunny, Humidity=Normal, you follow: Root → Sunny branch → Humidity=Normal branch → Play Tennis

#### Learning decision trees: The ID3 algorithm

At each node, which feature should we ask about to best split the data?****

Information theory provides the answer. The goal is to pick the feature whose value will give us the most information. You have feature vectors representing different properties of all your examples, and you want to find a question that will remove close to half the data with each question. You may think that you would want a question that will remove most of the data, or, at the most extreme, all but one of the examples. That is great if you get the response that is consistent with the one/small set. But much of the time, you will get the response that will mean you look at the bigger set, and you have only removed one example from consideration. The best questions will remove roughly half of the options regardless of the answer to that question.****

#### Information theory foundation

Information theory provides tools for measuring uncertainty and making better decisions when classifying data. Two key concepts are entropy, which quantifies uncertainty in a dataset, and information gain, which shows how much that uncertainty is reduced when splitting the data based on a feature. These measures form the foundation of algorithms such as decision trees.

Select each tab to learn about entropy and information gain.

### Entropy

Entropy measures the uncertainty in a set of examples. If all the examples in the set are from the same class, there is no uncertainty about the category of an example. In that case, the entropy is 0. On the other hand, maximum uncertainty happens when all the sets of examples are spread evenly across all categories. If one category has more examples than another, there is an intermediate amount of entropy. Intuitively, this is saying that you have a weak guess for which class a random example will be from, because you know that one category is more likely than the others.

Formula for entropy: 
![LaTeX: H(S) = -\sum p(c) \log_2 p(c)](https://northeastern.instructure.com/equation_images/H(S)%2520%253D%2520-%255Csum%2520p(c)%2520%255Clog_2%2520p(c)?scale=1)
  H
  (
  S
  )
  =
  &#x2212;
  &#x2211;
  p
  (
  c
  )
  
    log
    2
  
  &#x2061;
  p
  (
  c
  )
">
for each class c

Select the next tab to learn more.

### Information gain 

Information gain measures how much entropy is reduced when the set of examples is split based on a specific feature. If one possibility was removed from consideration, very little information has been gained. If many possibilities are removed, there is a lot of information gained. You want to pick the feature that will split the set to yield the highest expected information gain.

Information gain = ![LaTeX: H(parent) - \sum (|S_i|/|S|) × H(S_i)](https://northeastern.instructure.com/equation_images/H(parent)%2520-%2520%255Csum%2520(%257CS_i%257C%252F%257CS%257C)%2520%25C3%2597%2520H(S_i)?scale=1)
  H
  (
  p
  a
  r
  e
  n
  t
  )
  &#x2212;
  &#x2211;
  (
  
    |
  
  
    S
    i
  
  
    |
  
  
    /
  
  
    |
  
  S
  
    |
  
  )
  &#xD7;
  H
  (
  
    S
    i
  
  )
"> 

#### Tree construction process

Decision tree construction is a step-by-step process that uses entropy and information gain to choose the best feature splits. The goal is to create branches that reduce uncertainty at each step until the data is organized into pure or nearly pure subsets.

- Start with all training data at root.
- Calculate information gain for each possible feature split.
- Choose feature with highest information gain.
- Split data based on chosen feature.
- Recursively build subtrees for each subset.
- Stop when: Pure node (all same class), no more features, or minimum examples reached.

#### Advantages and disadvantages of decision trees

###### Advantages

- **Interpretability: **Easy to understand and explain decisions. Many other machine learning models, such as deep learning, do not give insight into why a choice was made. There are many cases where the justification for a choice must be explained. Explainability is valuable in medical, legal, and financial applications.
- **No assumptions: **Works with any type of data, both categorical and numeric features. No assumptions are made about the distribution of the data. For example, a decision tree does not assume that the data follows a normal distribution.
- **Feature selection: **Decision trees show which features matter most for predictions. Irrelevant features can be ignored from consideration.

###### Disadvantages

- **Overfitting: **Decision trees have a tendency to create overly complex trees. They can memorize the properties of the training data rather than learning general patterns.

Solution: Pruning techniques

- **Instability:** Decision trees can have high variance; small changes in the data can create very different trees.

Solution: Ensemble methods – a more advanced AI method uses multiple trees

### Linear discriminant analysis

Linear discriminant analysis (LDA) finds the best linear boundaries to separate different classes in the data. If you encounter new data that needs to be categorized, if the point is on one side of the line, it will be one category, but if it is on the other side of the line, it is called the other category. 

**Geometric intuition:** Imagine data points plotted in space, where different classes form clusters. LDA finds the straight line (or hyperplane in higher dimensions) that best separates these clusters.

In the simplest example, imagine data generated from two normal distributions. The best solution is to find the point halfway between the two distributions.

![](https://northeastern.instructure.com/courses/245820/files/39363680/download?verifier=zjy71YqwwKq2yocKCRYGCD51ryb0Fl6Y54MKPlzW)
Diagram of a neural network with labeled input, hidden, and output layers connected by weighted links and activation functions.

### Image description: Structure of a Neural Network

The image illustrates the architecture of a neural network, showing an input layer, one or more hidden layers, and an output layer. Each layer contains nodes (neurons) connected by weighted links. Activation functions are applied at each node to introduce non-linearity. The input layer receives feature values, hidden layers process intermediate representations, and the output layer produces final predictions.

In two dimensions, the problem will look something like this:

![](https://northeastern.instructure.com/courses/245820/files/39363662/download?verifier=mj8ik11fLHonWH4ND4e39dedMpZUxskUuP3tlX4t)
2D plot showing two classes of data points separated by a straight decision boundary.

### Image description: Visualizing Linear Separability in Two Dimensions

The image shows a 2D plot illustrating the concept of linear separability. Data points from two different classes are plotted in a Cartesian plane, with a straight line (decision boundary) separating them. This visual supports the idea that if such a line exists, the perceptron can converge to a solution.

This helps you understand what the classification boundary looks like. Understanding how to compute the best line or hyperplane requires more complex mathematics. First, try to get an intuitive explanation for what the mathematics are trying to determine. Imagine that you are rotating all the data so that the line that separates the two classes is parallel to the y-axis, and the new x-axis is perpendicular to the y-axis. In this new space, the y-dimension is irrelevant because the decision boundary identifies a point on the new x-axis. Now, imagine collapsing the data so you have a histogram, similar to the density functions in the first example. This is the approach LDA is taking; it is finding a direction that the data can be transformed into, which makes the categories distinguishable. In addition to rotating the data, it can stretch and shear the data. 

#### Example

Imagine taking a piece of stretchy fabric with a grid of arrows drawn on one side. As you stretch the fabric or tug on one portion while holding the others fixed, the direction of some arrows will change. But there are a few that will stay pointing in the same direction. In mathematics, these special arrows are called eigenvectors. The amount they are stretched is the eigenvalue. In the example problem, the goal is to find a way to stretch the space that gives the most separation between the classes.

#### Mathematical foundation

Fisher's linear discriminant: The optimal direction for projection maximizes the ratio: *J(w)* = (between-class scatter) / (within-class scatter).

- Between-class scatter: How far apart are the class means?
- Within-class scatter: How spread out are points within each class?

The LDA solution: The optimal projection direction is found by solving an eigenvalue problem. The eigenvector corresponding to the largest eigenvalue gives the best linear discriminant.

The eigenvalue problem LDA solves is:

![LaTeX: SW−1​SB​w=λw](https://northeastern.instructure.com/equation_images/SW%25E2%2588%25921%25E2%2580%258BSB%25E2%2580%258Bw%253D%25CE%25BBw?scale=1)
  S
  W
  &#x2212;
  1
  &#x200B;
  S
  B
  &#x200B;
  w
  =
  
    &#x3BB;
  
  w
">

Here:

- *S**W*​ is the **within-class scatter matrix**
- *S**B*​ is the **between-class scatter matrix**
- **w** is the direction we’re solving for – the eigenvector

![LaTeX: λ](https://northeastern.instructure.com/equation_images/%25CE%25BB?scale=1)
  
    &#x3BB;
  
"> is the eigenvalue — it tells us how “good” that direction is at separating the classes

Select the tabs to learn more about LDA.

### Assumptions of LDA

- Gaussian distribution: Each class follows a normal distribution
- Equal covariance: All classes have the same variance structure
- Linear separability: Classes can be separated by linear boundaries

Select the next tab to learn more.

### Advantages of LDA

- Computational efficiency: The problem can be solved by the above equation, no iterative optimization is needed.
- Dimensionality reduction: Can project high-dimensional data to lower dimensions, removing redundancy
- Probabilistic interpretation:– Provides probability estimates that represent the confidence of an example’s categorization

Select the next tab to learn more.

### Disadvantages of LDA

- Linear boundaries only: Cannot handle nonlinear patterns, curved boundaries
- Assumption violations: Performance degrades with non-Gaussian data, or categories with unequal variances
- Requires sufficient data: Needs enough examples to estimate covariance matrices and as the dimensionality increases the necessary sample size greatly increases

Select the next tab to learn more.

### Applications of LDA

- Face recognition: Project face images to lower-dimensional space where faces are easier to distinguish
- Text classification: Reduces high-dimensional word vectors to manageable size while preserving document categories
- Quality control: Separate defective from non-defective products based on manufacturing measurements

### Naive Bayes classification

Naive Bayes applies Bayes' theorem with a strong independence assumption to create simple yet powerful classifiers.

Recall Bayes' Theorem from Module 5. For a classification problem, you are given a set of features for an example and want to determine the class. In probabilistic terms, you want to pick the category that has the highest probability given those features. This maps nicely onto Bayes’ Theorem:

![LaTeX: P(class | features) = P(features | class) × P(class) / P(features)](https://northeastern.instructure.com/equation_images/P(class%2520%257C%2520features)%2520%253D%2520P(features%2520%257C%2520class)%2520%25C3%2597%2520P(class)%2520%252F%2520P(features)?scale=1)
  P
  (
  c
  l
  a
  s
  s
  
    |
  
  f
  e
  a
  t
  u
  r
  e
  s
  )
  =
  P
  (
  f
  e
  a
  t
  u
  r
  e
  s
  
    |
  
  c
  l
  a
  s
  s
  )
  &#xD7;
  P
  (
  c
  l
  a
  s
  s
  )
  
    /
  
  P
  (
  f
  e
  a
  t
  u
  r
  e
  s
  )
">

The "Naive" Assumption is that all features are conditionally independent given the class:

![LaTeX: P(f₁, f₂, ..., fₙ | class) = P(f₁ | class) × P(f₂ | class) × ... × P(fₙ | class)](https://northeastern.instructure.com/equation_images/P(f%25E2%2582%2581%252C%2520f%25E2%2582%2582%252C%2520...%252C%2520f%25E2%2582%2599%2520%257C%2520class)%2520%253D%2520P(f%25E2%2582%2581%2520%257C%2520class)%2520%25C3%2597%2520P(f%25E2%2582%2582%2520%257C%2520class)%2520%25C3%2597%2520...%2520%25C3%2597%2520P(f%25E2%2582%2599%2520%257C%2520class)?scale=1)
  P
  (
  f
  
    &#x2081;
  
  ,
  f
  
    &#x2082;
  
  ,
  .
  .
  .
  ,
  f
  
    &#x2099;
  
  
    |
  
  c
  l
  a
  s
  s
  )
  =
  P
  (
  f
  
    &#x2081;
  
  
    |
  
  c
  l
  a
  s
  s
  )
  &#xD7;
  P
  (
  f
  
    &#x2082;
  
  
    |
  
  c
  l
  a
  s
  s
  )
  &#xD7;
  .
  .
  .
  &#xD7;
  P
  (
  f
  
    &#x2099;
  
  
    |
  
  c
  l
  a
  s
  s
  )
">

Where *f**n* is the feature from the *n*-th dimension of the feature vector. 

In reality, features are often correlated, which is why this assumption is called naive. For example, in email spam detection, the words "free" and "money" often appear together. In weather, temperature and humidity are correlated. Medical symptoms often co-occur. So, while the independence assumption is often not true, it makes computation. In practice, the Naïve Bayes classifier works well even when the independence assumption is moderately violated, and it requires fewer training examples than many other techniques. 

#### Learning process

Parameter estimation: For each class *c* and feature *f*:

- P(class = *c*): Count frequency of class c in training data
- P(feature = *f* | class = *c*): Count frequency of feature value *f* in examples of class *c*

#### Example: Email spam detection

Training data:

- 1000 spam emails, 4000 legitimate emails
- Track word frequencies in each category

Learning:

- P(Spam) = 1000/5000 = 0.2
- P("free" | Spam) = 800/1000 = 0.8 (800 spam emails contain "free")
- P("free" | Legitimate) = 100/4000 = 0.025

Prediction for new email containing "free": P(Spam | "free") ∝ P("free" | Spam) × P(Spam) = 0.8 × 0.2 = 0.16 P(Legitimate | "free") ∝ P("free" | Legitimate) × P(Legitimate) = 0.025 × 0.8 = 0.02

Conclusion: Much more likely to be spam (0.16 vs 0.02)

#### Handling different data types

- **Categorical features:** The above example used nominal data. In that case, you simply use frequency counts, as in:
P(Color = Red | Class = Car) = (# red cars) / (# total cars)
- **Continuous features:** When features are continuous, as in interval or ratio data, you will use probability density functions. The probabilities are defined by the estimated probability densities. 

#### Smoothing techniques

What if a feature value never appears with a certain class in training data?

- P(word | class) = 0 would make the entire probability 0
- One unseen word would override all other evidence

To handle this problem, you can use Laplace Smoothing. Laplace smoothing adds small counts to all feature-class combinations:

![LaTeX: P(feature = f | class = c) = (count(f, c) + α) / (count(c) + α × |vocabulary|)](https://northeastern.instructure.com/equation_images/P(feature%2520%253D%2520f%2520%257C%2520class%2520%253D%2520c)%2520%253D%2520(count(f%252C%2520c)%2520%252B%2520%25CE%25B1)%2520%252F%2520(count(c)%2520%252B%2520%25CE%25B1%2520%25C3%2597%2520%257Cvocabulary%257C)?scale=1)
  P
  (
  f
  e
  a
  t
  u
  r
  e
  =
  f
  
    |
  
  c
  l
  a
  s
  s
  =
  c
  )
  =
  (
  c
  o
  u
  n
  t
  (
  f
  ,
  c
  )
  +
  
    &#x3B1;
  
  )
  
    /
  
  (
  c
  o
  u
  n
  t
  (
  c
  )
  +
  
    &#x3B1;
  
  &#xD7;
  
    |
  
  v
  o
  c
  a
  b
  u
  l
  a
  r
  y
  
    |
  
  )
">

A common choice for α is 1. This is referred to as add-one smoothing. 

Laplace smoothing ensures that there are no zero probabilities. As the size of your dataset increases, the effect of adding 1 count becomes negligible.

Select the tabs to learn more about Naive Bayes.

### Advantages of Naive Bayes

- **Simplicity: **The classifier is easy to understand and implement. There are few parameters, and the decision process is explainable. 
- **Speed:** Very fast training and prediction. Training time is linear in the number of features and examples. This allows for real-time applications.
- **Data efficiency:** Naive Bayes works well with small datasets because it has fewer parameters to estimate than more complex models. Good performance can be achieved even with small datasets.
- **Handles multiple classes naturally:** The classifier easily handles multi-class problems, while many other algorithms are designed for binary classification.

Select the next tab to learn more.

### Disadvantages of Naive Bayes

- **Independence assumption:** Assuming independence means that important feature interactions will be missed. In text classification, phrase meanings depend on word combinations. “Bank” means something different when it occurs with the work “River” than when it occurs with the word “Money”.  In medical diagnosis, symptom combinations provide crucial information. Fever and stiff neck together may be a sign of meningitis, but when they occur alone, the probability of meningitis is much less.
- **Limited expressiveness:** The classifier cannot learn complex decision boundaries. On messier, real-world problems, performance may be lower than using more advanced methods.

Select the next tab to learn more.

### Applications of Naive Bayes

- **Text classification:** Document categorization and sentiment analysis often work well despite word dependencies. Naïve Bayes often servers as a baseline for text classification tasks. 
- **Medical diagnosis:** Its strength in medical diagnoses comes from the natural incorporation of the prior probability of a disease. 
- **Real-time filtering:** It is fast enough for real-time spam detection and fraud detection. When new data is obtained, the model is simple to update.

Select Next to learn more about advanced algorithms and deep learning.

Icon Progress Bar (browser only)

## Match 3: 1.6 The Foundational Era to Present Day
- Source: Canvas Module: Module 1: Introduction to Artificial Intelligence: History, Trends and Future Directions
- Distance: 0.0057

Module: Module 1: Introduction to Artificial Intelligence: History, Trends and Future Directions

Item: 1.6 The Foundational Era to Present Day

Type: Page

## Module 1
 1.6 The Foundational Era to Present Day

The journey of AI began long before the term became mainstream. The 1940s and 1950s laid the groundwork for what would become a transformative field in science and technology. This era, often referred to as the “foundational era,” saw the emergence of key concepts and pioneering experiments that shaped the trajectory of AI research. From the first artificial neurons to early game-playing programs, these developments set the stage for the innovations that followed.

Select each heading to learn more about the history of AI from the foundational era (1940s-1950s) to the present day.

### 1. The foundational era (1940s-1950s)

In 1943, not long after the Turing machine was proposed, Warren McCulloch and Walter Pitts took inspiration from neuroscience and proposed a mathematical model of a network of logical elements. These logical elements later became known as artificial neurons or McCulloch-Pitts neurons (MPN). This started the subfield of AI, known as neural networks. This means neural nets were proposed before the first programmable computer!

In 1950, Alan Turing proposed the Imitation Game. Using an approach quite different from neural networks, in 1951 researchers started programming AI for games. Christopher Strachey wrote a program to play checkers, and Dietrich Prinz created one for chess. Prinz’s program involved exhaustive search, and Strachey’s program involved a tree search algorithm. These types of algorithms are covered in Module 2. As a sidenote, in 1951, Strachey recorded the first music that a computer could play.

Inspired by MPNs, Marvin Minsky began research on neural networks. In 1952, Minsky, along with Dean Edmonds, created the stochastic neural analog reinforcement calculator (SNARC). SNARC was not a programmable computer used to train a neural network; it was the entire machine itself. The machine was able to learn the path of a maze through experience. SNARC contained 40 artificial neurons and learned by strengthening the connection between neurons based on the performance of the network on the previous attempt at the maze.

In 1956, the Dartmouth Summer Research Project on Artificial Intelligence was held. It was organized by John McCarthy and Marvin Minsky. Nathaniel Rochester and Claude Shannon co-organized. Herbert Simon and Allen Newell attended; they would become influential in both AI and cognitive science. The proposal for the conference was where McCarthy coined the term “artificial intelligence.” The conference was like a brainstorming session, and led to ideas and collaborations that have a long-term influence on AI.

Select the next tab to learn more.

### 2. Early success (late 1950s through 1960s)

In 1957, Frank Rosenblatt simulated a neural network on an IBM computer. In this work, Rosenblatt coined the term “perceptron.” The perceptron was an important advancement in neural networks because it described a learning algorithm that could be run on a computer. The perceptron was conceived as a way for an artificial system to perceive and categorize patterns. The system would learn associations between patterns. This could be thought of as the start of the fields of computer vision and pattern recognition.

In 1958, Rosenblatt continued work on perceptrons and created the Mark I Perceptron, a machine to classify images. This used Rosenblatt’s idea of a multiple-layer neural network.

In 1959, Arthur Samuel coined the term “machine learning,” by which he meant the “field of study that gives computers the ability to learn without being explicitly programmed.” He created an AI to play checkers and improve with experience.

In 1966, Joseph Weizenbaum released ELIZA. Influential in both natural language processing (NLP) and human-computer interaction, ELIZA was the first “chatterbot,” which you now know as a chatbot.

Select the next tab to learn more.

### 3. The AI winter (1969-early 1990s)

Work on neural networks fell out of fashion in 1969, after Marvin Minsky and Seymour Papert published their book *Perceptrons*.

This example is a simplified explanation of the problem they identified. A perceptron can classify a day as a “nice day” if the temperature and wind speed are both below threshold values. It is nice when the temperature isn't too hot and there is no wind.

A perceptron can classify a day as a nice day if either the cloud cover is below a threshold and the temperature is above a threshold. It is a nice day if there are no clouds or if it is warm.

However, a single-layer perceptron cannot classify a day as nice if it is warm and dry, or if it is cold and humid, but not if it is warm and humid or cold and dry. The perception cannot create a single threshold value for each dimension.

This is the XOR problem. XOR means exclusive OR; it is true when only one dimension is true, but is false when both are true. The OR example above can be true if either threshold is met, and the AND problem is true only if both thresholds are met.

This stopped neural network research in its tracks. There are many classification problems where an XOR decision is needed, so this limitation was too much for the field.

But Minsky and Papert only considered single-layer perceptrons. If an internal, hidden layer were added, neural networks would be able to solve the XOR classification problem. But the damage was already done. AI research continued, but largely in symbolic AI.

Excitement around AI waned, and funding agencies began to stop funding as many AI projects, feeling that the promises of AI had not been met. In the United States, the Advanced Research Project Agency (ARPA, today DARPA) changed its funding requirements so that projects needed a clear application. In the UK, a paper submitted to the Science Research Council, now called the “Lighthill Report,” was written by James Lighthill in 1973. It concluded that AI research did not have a positive impact, and funding of AI research in the UK declined.

In the 1980s, expert systems brought renewed interest and excitement around AI. These systems have carefully crafted knowledge representations for their specific domain, and they reason through decisions using that knowledge. This flavor of AI is the topic of Modules 3 and 4.

While symbolic AI research continued through the 1970s and 80s, there were severe limitations. These systems were not machine learning systems. They were unable to cope with changes in the environment. While symbolic AI systems were good at solving small and specific problems, as the size of the problem grew, the complexity of rules and symbols required to solve the problem grew faster, making it intractable to solve large problems.

In 1986, Geoffrey Hinton, David Rumelhart and Ronald Williams published their paper “Learning Representations by Back-Propagating Errors.” This paper described a way to update the weights of a multilayer neural network. Think of the weights as the strength of the connection between two artificial neurons, or as the influence one neuron has on the computation of a later neuron. After repeated updates, the network becomes more accurate, and the required updates become smaller. You will see the name “Geoffrey Hinton” again later on this timeline.

Another name you will see again later is Yann LeCun. In 1990, Yann LeCun contributed to the development of a neural network that could recognize handwritten digits. This was the sort of real-world application companies and funding agencies were looking for.

This success led to renewed investment in AI. However, as the economy hit a recession, funding dried up, and businesses and the general population became wary of AI.

Select the next tab to learn more.

### 4. The machine learning era (Late 1990s and 2000s)

Machine learning became the popular flavour of AI. Datasets and computing power grew. Previously, machine learning algorithms were applied to low-dimensional problems that required a smaller training dataset. As computing power and datasets grew, machine learning found success.

In 1995, Corinna Cortes and Vladimir Vapnik made use of a statistical learning technique from the 1960s, called support vector machines (SVMs), and applied “the kernel trick.” The kernel trick, proposed by Bernard Boser, Isabelle Guyon, and Vladimir Vapnik (1992), combined with the SVM, marked a significant advancement in machine learning. The SVM continued to be one of the most popular machine learning techniques until the deep learning revolution.

Also in 1995, Yoav Freund and Robert E. Schapire published their classification algorithm, AdaBoost. The key finding was that you could use many weak classifiers, ones that classify only slightly better than guessing randomly, and combine their answers to classify input very accurately.

In 1997, Deep Blue, a chess-playing AI supercomputer, beat the chess grandmaster Garry Kasparov. 

The Viola-Jones face detector was released in 2001. The face-detector was commercially used in cameras worldwide. It could detect faces with 95% accuracy, using AdaBoost to combine many simple classifiers. Because of its simplicity, it could run on very basic hardware.

Select the next tab to learn more.

### 5. Deep learning (2010s)

Datasets continued to grow in size. In work led by Fei-Fei Li, ImageNet was first presented in 2009. ImageNet contained 14 million labeled images. Computer vision researchers could now train machine learning models with millions of examples.

The ImageNet dataset led to the ImageNet Large Scale Visual Recognition Challenge (ILSVRC). The challenge was to train an AI model to assign labels to the images that match the human-assigned labels. Accuracy is often measured by the “top-5” accuracy. The classification of an image is considered correct if the correct label is among the five most likely labels in the model's list. In 2010, the winner used an SVM and achieved 71.8% top-5 accuracy.

In 2012, Alex Krihevsky, Ilya Sutskever and Geoffrey Hinton submitted AlexNet to the ImageNet challenge. AlexNet was a type of neural network known as a deep learning model, a neural network with multiple hidden layers. AlexNet achieved 84.7% top-5 accuracy. This was a groundbreaking advancement. In the following years, deep learning became the dominant force in machine learning.

In 2018, Geoffrey Hinton, Yoshua Bengio and Yann LeCun were recipients of the Turing Award for their work in deep learning. In 2024, John Hopfield and Geoffrey Hinton were awarded the Nobel Prize in Physics for their work on artificial neural networks.

Many previous AI models were explainable, meaning the reasons behind the AI’s actions could be understood and interpreted, often in plain English. The hidden layers of deep neural networks are difficult to understand; there is no easy way to explain what features led an image classifier to categorize an image as a dog instead of a cat. This led to work on finding ways to visualize or better understand how the hidden layers were representing and transforming their input.

The representations of the hidden layers have a very high dimensionality. The preceding layers of the network take an input image and transform it into that high-dimensional space. Researchers began to imagine navigating this space and determining which inputs would result in a representation at a specific point within it. This led to the creation of networks that transform a point from that high-dimensional space into an image. This is the idea behind generative AI; leveraging the power of deep learning to generate new images, new text or new speech.

Select the next tab to learn more.

### 6. Generative AI (2020s)

Generative AI was not just applied to computer vision. Deep learning had become the dominant force in almost all areas of AI, and generative AI came along with it. In the field of NLP, deep learning models have evolved into large language models (LLMs). These models are referred to as large because they contain billions of neurons or more. 

On November 30, 2022, OpenAI released ChatGPT for public use. This chatbot was leagues ahead of the original chatbot ELIZA. ChatGPT allowed people to have a very human-like text conversation. Unlike the very specific and targeted domains of the AI models of old, you could talk to ChatGPT about anything.

Since then, many LLMs have been released and have extended beyond chatbots. An LLM can now generate text responses, images, audio responses that sound human, video and computer code.

On March 31, 2025, Cameron R. Jones and Benjamin K. Bergen published their article describing the administration of the Turing test. GPT-4.5 was identified as the human 73% of the time.

The 2020s have marked a transformative period in the evolution of AI, with generative models like ChatGPT redefining how machines interact with humans. These advancements have not only surpassed early expectations but have also sparked widespread discussions about the role of AI in society, ethics, and the future of work. As we continue to explore the capabilities and implications of generative AI, it becomes clear that we are only at the beginning of a new era in AI.

Select Next to complete the quiz.

Icon Progress Bar (browser only)

## Match 4: 10.8 Solving MDPs: Value and Policy Iteration
- Source: Canvas Module: Module 10: Decision-Making
- Distance: 0.0058

Module: Module 10: Decision-Making

Item: 10.8 Solving MDPs: Value and Policy Iteration

Type: Page

## Module 10
 10.8 Solving MDPs: Value and Policy Iteration

With the elements of an MDP in place, the question becomes: how do we find the best possible strategy for an agent? Value iteration and policy iteration provide systematic ways to compute optimal policies, even in complex environments.

Think back to the first example with the 4x4 grid. To compute the value at each state, the computation started at the goal state. In real-world problems, there can be many goals, and each goal can have different values. This means you can’t easily start the computation at the right place and work from there. Remember what happened to the values when the number of states increased? At some point, moving to the obstacle would be the best choice. In that case, would you start the computation from that point? What happens when you get to a point where the best path would take you to a different goal. If you haven’t computed the value in that direction yet, because you started from a different goal, you would not know the future values of those states.

### Value iteration

Value iteration finds the state values by iteratively updating the value of every state until the estimates converge (i.e. reach a point where they no longer change). It's based on the principle that optimal values must satisfy the Bellman equation. It is related to the value of a policy, because the best policy for each state is to choose the action that gives the highest value from the Bellman equation (the value of the action plus the discounted value of the next state).

The algorithm:

- Initialize: ![LaTeX: V₀(s) = 0](https://northeastern.instructure.com/equation_images/V%25E2%2582%2580(s)%2520%253D%25200?scale=1)
  V
  
    &#x2080;
  
  (
  s
  )
  =
  0
"> for all states
- Update: For each iteration k: ![LaTeX: V_{k+1}(s) = \max_a \sum P(s'|s,a)[R(s,a,s') + γV_k(s')]](https://northeastern.instructure.com/equation_images/V_%257Bk%252B1%257D(s)%2520%253D%2520%255Cmax_a%2520%255Csum%2520P(s'%257Cs%252Ca)%255BR(s%252Ca%252Cs')%2520%252B%2520%25CE%25B3V_k(s')%255D?scale=1)
  
    V
    
      k
      +
      1
    
  
  (
  s
  )
  =
  
    max
    a
  
  &#x2211;
  P
  (
  
    s
    &#x2032;
  
  
    |
  
  s
  ,
  a
  )
  [
  R
  (
  s
  ,
  a
  ,
  
    s
    &#x2032;
  
  )
  +
  
    &#x3B3;
  
  
    V
    k
  
  (
  
    s
    &#x2032;
  
  )
  ]
">
- Converge: Stop when ![LaTeX: |V_{k+1}(s) - V_k(s)| 
    |
  
  
    V
    
      k
      +
      1
    
  
  (
  s
  )
  &#x2212;
  
    V
    k
  
  (
  s
  )
  
    |
  
  &lt;
  &#x03F5;
  
  
    for all states
  
">
- Extract policy: ![LaTeX: π^*(s) = \arg\max_a \sum P(s'|s,a)[R(s,a,s') + γV^*(s')]](https://northeastern.instructure.com/equation_images/%25CF%2580%255E*(s)%2520%253D%2520%255Carg%255Cmax_a%2520%255Csum%2520P(s'%257Cs%252Ca)%255BR(s%252Ca%252Cs')%2520%252B%2520%25CE%25B3V%255E*(s')%255D?scale=1)
  
    
      &#x3C0;
    
    &#x2217;
  
  (
  s
  )
  =
  arg
  &#x2061;
  
    max
    a
  
  &#x2211;
  P
  (
  
    s
    &#x2032;
  
  
    |
  
  s
  ,
  a
  )
  [
  R
  (
  s
  ,
  a
  ,
  
    s
    &#x2032;
  
  )
  +
  
    &#x3B3;
  
  
    V
    &#x2217;
  
  (
  
    s
    &#x2032;
  
  )
  ]
">

#### Example: Value iteration in a simple grid

Consider a 2×2 grid with:

- Start at (1,1), goal at (2,2)
- Actions: {Right, Up}
- Rewards: +10 at goal, -1 per step
- γ = 0.9

Iteration 0: V₀(s) = 0 for all states

Select each tab to view Iterations 1 and 2.

### Iteration 1

- V₁(1,1) = max(reward for going right, reward for going up) = max(-1, -1) = -1
- V₁(2,2) = 10 (goal state)

Select the next tab to learn more.

### Panel 2

- V₁(1,1) = max(-1 + 0.9×V₁(2,1), -1 + 0.9×V₁(1,2))
- Continue until convergence...

#### Convergence properties

Convergence in value iteration ensures that repeated updates will eventually lead to the optimal state values, though the speed of convergence depends on the chosen discount factor γ.

- Value iteration is guaranteed to converge to optimal values
- Convergence rate depends on the discount factor γ
- Lower γ means faster convergence but less consideration of future rewards

Here is an illustration of applying this to the 4x4 grid.

![](https://northeastern.instructure.com/courses/245820/files/39363669/download?verifier=5ibaDkci2CRor97EwQFsOQJyYHouzvpV9gRlo03C)
Sequence of 4x4 grid diagrams showing how state values evolve over multiple iterations using the Bellman equation in a value iteration process.

### Image description: Value Iteration in a 4x4 Grid World

The image illustrates the step-by-step convergence of value iteration in a 4x4 grid world using the Bellman equation.

Iteration 0: All states initialized to zero.
Iteration 1: Terminal states (Goal: +10, Obstacle: -10) are assigned their rewards.
Iteration 2: Values begin to propagate from the goal.
Final (Iteration 8): The grid shows the fully converged value function, with optimal values assigned to each state.

Bellman Equation:

![LaTeX: V(s)=\max_a[R(s,a)+γ⋅V(s′)]V(s) = \max_a [R(s,a) + \gamma \cdot V(s')]V(s)=\max_a​[R(s,a)+γ⋅V(s′)]](https://northeastern.instructure.com/equation_images/V(s)%253D%255Cmax_a%255BR(s%252Ca)%252B%25CE%25B3%25E2%258B%2585V(s%25E2%2580%25B2)%255DV(s)%2520%253D%2520%255Cmax_a%2520%255BR(s%252Ca)%2520%252B%2520%255Cgamma%2520%255Ccdot%2520V(s')%255DV(s)%253D%255Cmax_a%25E2%2580%258B%255BR(s%252Ca)%252B%25CE%25B3%25E2%258B%2585V(s%25E2%2580%25B2)%255D?scale=1)
  V
  (
  s
  )
  =
  
    max
    a
  
  [
  R
  (
  s
  ,
  a
  )
  +
  
    &#x3B3;
  
  &#x22C5;
  V
  (
  s
  
    &#x2032;
  
  )
  ]
  V
  (
  s
  )
  =
  
    max
    a
  
  [
  R
  (
  s
  ,
  a
  )
  +
  &#x03B3;
  &#x22C5;
  V
  (
  
    s
    &#x2032;
  
  )
  ]
  V
  (
  s
  )
  =
  
    max
    a
  
  &#x200B;
  [
  R
  (
  s
  ,
  a
  )
  +
  
    &#x3B3;
  
  &#x22C5;
  V
  (
  s
  
    &#x2032;
  
  )
  ]
">
Process Summary:

Initialize all non-terminal states to 0.
Assign rewards to terminal states.
Apply the Bellman update across all states.
Values spread outward from terminals.
Repeat until values stabilize.

Key Insight:
The discount factor γ=0.9 ensures convergence and reduces the influence of distant rewards.

### Policy iteration

**Policy iteration** alternates between policy evaluation (computing values for a fixed policy) and policy improvement (updating the policy based on current values).

The algorithm:

- Initialize: Start with arbitrary policy ![LaTeX: π_0](https://northeastern.instructure.com/equation_images/%25CF%2580_0?scale=1)
  
    
      &#x3C0;
    
    0
  
">
- Policy evaluation: Compute ![LaTeX: V^π](https://northeastern.instructure.com/equation_images/V%255E%25CF%2580?scale=1)
  
    V
    
      &#x3C0;
    
  
"> for current policy
- Policy improvement: Update policy: ![LaTeX: π'(s) = \arg\max_a \sum P(s'|s,a)[R(s,a,s') + γV^π(s')]](https://northeastern.instructure.com/equation_images/%25CF%2580'(s)%2520%253D%2520%255Carg%255Cmax_a%2520%255Csum%2520P(s'%257Cs%252Ca)%255BR(s%252Ca%252Cs')%2520%252B%2520%25CE%25B3V%255E%25CF%2580(s')%255D?scale=1)
  
    
      &#x3C0;
    
    &#x2032;
  
  (
  s
  )
  =
  arg
  &#x2061;
  
    max
    a
  
  &#x2211;
  P
  (
  
    s
    &#x2032;
  
  
    |
  
  s
  ,
  a
  )
  [
  R
  (
  s
  ,
  a
  ,
  
    s
    &#x2032;
  
  )
  +
  
    &#x3B3;
  
  
    V
    
      &#x3C0;
    
  
  (
  
    s
    &#x2032;
  
  )
  ]
">
- Repeat: Until policy doesn't change

#### Policy evaluation step

For a fixed policy π, solve the system of linear equations: ![LaTeX: V^π(s) = \sum_a π(a|s) Σ P(s'|s,a)[R(s,a,s') + γV^π(s')]](https://northeastern.instructure.com/equation_images/V%255E%25CF%2580(s)%2520%253D%2520%255Csum_a%2520%25CF%2580(a%257Cs)%2520%25CE%25A3%2520P(s'%257Cs%252Ca)%255BR(s%252Ca%252Cs')%2520%252B%2520%25CE%25B3V%255E%25CF%2580(s')%255D?scale=1)
  
    V
    
      &#x3C0;
    
  
  (
  s
  )
  =
  
    &#x2211;
    a
  
  
    &#x3C0;
  
  (
  a
  
    |
  
  s
  )
  
    &#x3A3;
  
  P
  (
  
    s
    &#x2032;
  
  
    |
  
  s
  ,
  a
  )
  [
  R
  (
  s
  ,
  a
  ,
  
    s
    &#x2032;
  
  )
  +
  
    &#x3B3;
  
  
    V
    
      &#x3C0;
    
  
  (
  
    s
    &#x2032;
  
  )
  ]
">

To compute the values you don’t need to do a complete value iteration because the policy dictates the next state. The process is called iterative policy evaluation. 

#### Example: Policy iteration in a 4x4 grid

Using the 4x4 example again, imagine that the initial policy for each state is to go north. When computing values for each state, only the states that are south of the goal will have an increased value, the others will never reach the goal, and so have low value. 

When you update the policy, every state in the third column will update its policy to take the action that will lead to the current highest value, and so all will pick the east action. The only other state to change policy is the state south of the obstacle. It will update to either east or west. They have equal value and so neither direction is preferred over the other. 

With the new policies in place, recompute the value functions. Now the third column will have increased values, as does the state south of the obstacle if it was updated to the east action. 

As the policies change there may be cases where the values of actions are equal. For example, at 3,3 the policy of going north or going east are equally good. Whether the policy remains unchanged when this happens, or if the policy is chosen randomly from the set of good options, is an implementation choice.

![](https://northeastern.instructure.com/courses/245820/files/39363667/download?verifier=skdoOOZrKQ17tvA7elTAwBCbalTcHCSyombNZ8Uy)
Diagram showing four stages of policy iteration in a 4x4 grid world, with arrows indicating actions, colored cells for state values, and a legend explaining the process.

### Image description: Policy Iteration Process – 4x4 Grid World

The image illustrates the policy iteration process in a 4x4 grid world environment, commonly used in reinforcement learning. It shows four stages of policy evolution:

Policy 0 (Initial): Random actions.
Policy 1 & 2: Gradual improvement with more EAST-directed actions.
Final Policy: Converged optimal policy with mostly EAST actions.

Each grid cell displays a value representing the expected utility of that state.

Green cells: Good states.
Red cells: Bad states.
Orange cells: Obstacles.
Arrows indicate the chosen action per state, and a legend explains color coding and value types.

Transcript:
Policy Iteration Algorithm:
1. Policy Evaluation: Compute V(s) under current policy π until convergence.
2. Policy Improvement: Update π using Qπ(s,a) = R(s,a) + γ Σ P(s'|s,a)Vπ(s').

Legend:
- Green: Good state
- Red: Bad state
- Orange: Obstacle
- Arrows: Policy actions
- Green text: Positive values
- Red text: Negative values

###  Use case: Autonomous vehicle routing

An autonomous vehicle choosing routes through a city:

- **States:** Road intersections 
- **Actions:** Turn directions at each intersection 
- **Rewards:** Based on travel time, fuel efficiency, safety

Policy iteration process:

- Start with a simple policy (e.g., always head toward destination)
- Evaluate this policy's value at each intersection
- Improve policy by choosing actions that lead to higher-value intersections
- Repeat until the policy stabilizes

### Comparison: Value vs. policy iteration

Select each flip card to compare the advantages and disadvantages of value iteration and policy iteration.

##### Value iteration

- Simpler implementation
- No need to solve linear systems
- May require more iterations

##### Policy iteration

- Often converges in fewer iterations
- Each step improves the policy
- Requires solving linear systems (policy evaluation)

When to use each:

- Value iteration: When states/actions are numerous or transition probabilities are uncertain
- Policy iteration: When fast convergence is needed and linear system solving is feasible

### Partially observable Markov decision processes (POMDPs)

Real-world AI systems often lack complete information about their environment. **partially observable Markov decision processes (POMDPs)** extend MDPs to handle situations where the agent cannot fully observe the current state. A POMDP is to an MDP what an HMM is to a Markov model. 

#### POMDP components

POMDPs consist of all MDP components plus:

- Observations (Ω): What the agent can actually perceive
- Observation Model: P(o|s,a) - probability of observing o after taking action a in states

#### The belief state

In partially observable environments, an agent uses a belief state — a probability distribution over possible states — to reason under uncertainty. This internal model is updated with each action and observation, guiding decisions without direct access to the true state. Since the agent can't observe the true state, it maintains a belief state - a probability distribution over possible states:

b(s) = P(state = s | observation history)

The agent makes decisions based on this belief state rather than the true (unknown) state.

After taking action *a* and observing *o*, the belief state updates using Bayes' theorem:

![LaTeX: b'(s') = η P(o|s',a) \sum P(s'|s,a) b(s)](https://northeastern.instructure.com/equation_images/b'(s')%2520%253D%2520%25CE%25B7%2520P(o%257Cs'%252Ca)%2520%255Csum%2520P(s'%257Cs%252Ca)%2520b(s)?scale=1)
  
    b
    &#x2032;
  
  (
  
    s
    &#x2032;
  
  )
  =
  
    &#x3B7;
  
  P
  (
  o
  
    |
  
  
    s
    &#x2032;
  
  ,
  a
  )
  &#x2211;
  P
  (
  
    s
    &#x2032;
  
  
    |
  
  s
  ,
  a
  )
  b
  (
  s
  )
">

where η is a normalization constant.

###  Use case: Robot navigation with noisy sensors

A robot navigating through rooms:

- True states: Actual room locations
- Observations: Noisy sensor readings (WiFi signals, camera images)
- Challenge: Sensors provide ambiguous information about location

The robot maintains beliefs about which room it's in and updates these beliefs as it moves and gathers sensor data.

#### POMDP complexity

POMDPs are significantly more complex than MDPs.

- The belief space is continuous and high-dimensional.
- Optimal policies map belief states to actions.
- Exact solutions are often computationally intractable.

Approximate solutions include:

- Point-based methods: Sample representative belief points
- Particle filters: Approximate beliefs with weighted samples
- Monte Carlo planning: Use simulation for lookahead search

#### Applications

POMDPs are widely used in real-world settings where agents must make decisions with incomplete information, including medical, transportation, and financial domains.

- Medical diagnosis: Symptoms provide partial information about underlying conditions
- Autonomous driving: Sensors provide incomplete information about traffic situations
- Financial trading: Market observations provide partial information about underlying economic states

### Reinforcement learning

To make use of the Bellman equation, value iteration, and policy iteration, you need to know the transition probabilities associated with each action and the rewards for each state-action pair. In many cases, you may not know either. 

Reinforcement learning (RL) addresses the challenge of finding optimal policies when the MDP model (transition probabilities and rewards) is unknown. Instead of having a complete model, the agent learns through trial-and-error interaction with the environment.

The RL setting:

- Agent takes actions in an environment
- Environment provides rewards and new states
- Agent's goal: maximize cumulative reward
- Challenge: balance exploration (trying new actions) vs. exploitation (using known good actions)

#### Model-free vs. model-based RL

Reinforcement learning strategies can be broadly categorized into model-free and model-based approaches. While model-free methods learn directly from experience, model-based techniques build an internal model of the environment to plan ahead and improve decision-making.

Select the flip cards to learn the differences between model-free vs. model-based RL.

##### Model-free RL

- Learn optimal actions directly from experience
- No attempt to learn transition probabilities
- Examples: Q-learning, SARSA, Policy Gradient methods

##### Model-based RL

- First, learn a model of the environment
- Then use planning algorithms (like value iteration) on the learned model
- Examples: Dyna-Q, MCTS-based methods

### Temporal difference (TD) learning

In TD learning, the agent takes actions in the environment and observes what happens. It learns the values of each state on the fly. It doesn’t need to learn the unknown transition probabilities or the reward function, and instead just updates the value estimates directly. 

Each time you take an action, you update the value of that state:

![LaTeX: V(s) ← V(s) + α[r + γV(s') - V(s)]](https://northeastern.instructure.com/equation_images/V(s)%2520%25E2%2586%2590%2520V(s)%2520%252B%2520%25CE%25B1%255Br%2520%252B%2520%25CE%25B3V(s')%2520-%2520V(s)%255D?scale=1)
  V
  (
  s
  )
  &#x2190;
  V
  (
  s
  )
  +
  
    &#x3B1;
  
  [
  r
  +
  
    &#x3B3;
  
  V
  (
  
    s
    &#x2032;
  
  )
  &#x2212;
  V
  (
  s
  )
  ]
">

The new V(s) will be used in future planning or when further updating values. While the reward in the environment does depend upon the action of the agent, this doesn’t need to be explicitly represented because you are learning the state values directly. 

The term temporal difference learning comes from the equations comparing what actually happened to what it expected to happen. 

r + γV(s') represents what actually happened. The term *r* is the actual reward received, and γV(s') is the discounted reward from V(s’). 

The term ![LaTeX: [r + γV(s') - V(s)]](https://northeastern.instructure.com/equation_images/%255Br%2520%252B%2520%25CE%25B3V(s')%2520-%2520V(s)%255D?scale=1)
  [
  r
  +
  
    &#x3B3;
  
  V
  (
  
    s
    &#x2032;
  
  )
  &#x2212;
  V
  (
  s
  )
  ]
"> is referred to as the **TD error**. You subtract V(s), which is the current estimation of the value of state *s*. If the difference is 0, it means the estimate was accurate. If there was an error, that error is multiplied by the learning rate, α, and added to the previous estimate of the value of the state. This is the new estimate. 

A learning rate of 1 means the entire error is applied to the estimate. Values closer to 0 result in slower learning. The learning rate is often set to a value that balances the speed of learning with the possibility that applying the full error would cause the estimate to pass over the true value. As more experience is gained, the value estimates for each state will get closer to the true value.

An example is given following the description of the next two learning algorithms.

### Q-learning: The foundation of modern RL

TD learning allows the agent to learn the values of the environment. It is space efficient, because the agent does not need to keep track of which state-action pairs led to which rewards. It isn’t trying to model the reward function, as it is a model-free RL algorithm. However, there are cases where it helps to know which actions tend to have high rewards. 

Q-learning learns optimal action values (Q-values) through experience without requiring a model of the environment. The TD learning algorithm covered above is a way to learn which states are good,  Q-learning is a way to learn which actions are good. While that comparison is useful for understanding the difference of the above method and Q-learning, it is isn’t technically correct, because Q-learning is a temporal difference method.

Q-learning update rule: ![LaTeX: Q(s,a) ← Q(s,a) + α[r + γ \max_a' Q(s',a') - Q(s,a)]](https://northeastern.instructure.com/equation_images/Q(s%252Ca)%2520%25E2%2586%2590%2520Q(s%252Ca)%2520%252B%2520%25CE%25B1%255Br%2520%252B%2520%25CE%25B3%2520%255Cmax_a'%2520Q(s'%252Ca')%2520-%2520Q(s%252Ca)%255D?scale=1)
  Q
  (
  s
  ,
  a
  )
  &#x2190;
  Q
  (
  s
  ,
  a
  )
  +
  
    &#x3B1;
  
  [
  r
  +
  
    &#x3B3;
  
  
    
      max
      a
    
    &#x2032;
  
  Q
  (
  
    s
    &#x2032;
  
  ,
  
    a
    &#x2032;
  
  )
  &#x2212;
  Q
  (
  s
  ,
  a
  )
  ]
">

Where:

- α is the learning rate
- r is the immediate reward
- γ is the discount factor
- s' is the next state

You can see that the Q-learning update rule looks like the TD learning update rule, but with the V(s) and V(s’) replaced with Q(s,a) and Q(s’, a’). Both methods are temporal difference methods, which is why the equations look similar. 

Q-learning is an **off-policy** learning method, because it incorporates the best next action regardless of whether or not the current policy says that action should be taken. 

### State action reward state action (SARSA) Learning

SARSA is another temporal difference method. Q-learning updates the value of the current state-action pair based on the current state and action and the maximum value of the next state and action pair. SARSA requires observing the outcome of the next state and action before updating the current state and action’s value. It is an **on-policy** method, meaning the action taken is based upon the current policy. Because it only needs to consider one future action, there is no need to take the maximum over possible actions. This leads to a slightly simpler update rule.

SARSA update rule: ![LaTeX: Q(s,a) ← Q(s,a) + α[r + γ \max_a' Q(s',a') - Q(s,a)]](https://northeastern.instructure.com/equation_images/Q(s%252Ca)%2520%25E2%2586%2590%2520Q(s%252Ca)%2520%252B%2520%25CE%25B1%255Br%2520%252B%2520%25CE%25B3%2520%255Cmax_a'%2520Q(s'%252Ca')%2520-%2520Q(s%252Ca)%255D?scale=1)
  Q
  (
  s
  ,
  a
  )
  &#x2190;
  Q
  (
  s
  ,
  a
  )
  +
  
    &#x3B1;
  
  [
  r
  +
  
    &#x3B3;
  
  
    
      max
      a
    
    &#x2032;
  
  Q
  (
  
    s
    &#x2032;
  
  ,
  
    a
    &#x2032;
  
  )
  &#x2212;
  Q
  (
  s
  ,
  a
  )
  ]
">

The choice between Q-learning and SARSA is usually dependent upon if you want to find an optimal policy (choose Q-learning) or to learn a policy that is good for your agent’s current exploration strategy (choose SARSA).

#### Example: TD learning and SARSA

The example below shows the results of TD learning and SARSA on the 4x4 grid world.

![](https://northeastern.instructure.com/courses/245820/files/39363668/download?verifier=wJplRR5gyb0C6N8WknbjmbtwZJcEeslroR7NT9Y2)
Infographic illustrating TD Learning in a 4x4 Grid World MDP with examples of TD(0) Value Function Learning and SARSA Q-Learning, highlighting their key differences and parameters used.

### Image description: TD Learning in a 4x4 Grid World MDP

This infographic titled "TD Learning in 4x4 Grid World MDP: Learning from Experiences Without Knowing True Model" is structured into several informative sections:

Grid World Setup:

A 4x4 grid labeled from S1 to S16.

Start state: S1; Goal state: S16.

Actions include Up (U), Down (D), Left (L), and Right (R).

TD(0) Value Function Learning:

Displays initial and learned policies.

Update rule:

![](https://northeastern.instructure.com/equation_images/V(St)%25E2%2586%2590V(St)%252B%25CE%25B1%255BRt%252B1%252B%25CE%25B3V(St%252B1)%25E2%2588%2592V(St)%255DV(S_t)%2520%255Cleftarrow%2520V(S_t)%2520%252B%2520%255Calpha%2520%255BR_%257Bt%252B1%257D%2520%252B%2520%255Cgamma%2520V(S_%257Bt%252B1%257D)%2520-%2520V(S_t)%255DV(St%25E2%2580%258B)%25E2%2586%2590V(St%25E2%2580%258B)%252B%25CE%25B1%255BRt%252B1%25E2%2580%258B%252B%25CE%25B3V(St%252B1%25E2%2580%258B)%25E2%2588%2592V(St%25E2%2580%258B)%255D?scale=1)
  V
  (
  S
  t
  )
  &#x2190;
  V
  (
  S
  t
  )
  +
  
    &#x3B1;
  
  [
  R
  t
  +
  1
  +
  
    &#x3B3;
  
  V
  (
  S
  t
  +
  1
  )
  &#x2212;
  V
  (
  S
  t
  )
  ]
  V
  (
  
    S
    t
  
  )
  &#x2190;
  V
  (
  
    S
    t
  
  )
  +
  &#x03B1;
  [
  
    R
    
      t
      +
      1
    
  
  +
  &#x03B3;
  V
  (
  
    S
    
      t
      +
      1
    
  
  )
  &#x2212;
  V
  (
  
    S
    t
  
  )
  ]
  V
  (
  S
  t
  &#x200B;
  )
  &#x2190;
  V
  (
  S
  t
  &#x200B;
  )
  +
  
    &#x3B1;
  
  [
  R
  t
  +
  1
  &#x200B;
  +
  
    &#x3B3;
  
  V
  (
  S
  t
  +
  1
  &#x200B;
  )
  &#x2212;
  V
  (
  S
  t
  &#x200B;
  )
  ]
">

with parameters: α = 0.5, γ = 1.

SARSA Q-Learning:

Shows initial and learned Q-values.

Update rule:

![](https://northeastern.instructure.com/equation_images/Q(St%252CAt)%25E2%2586%2590Q(St%252CAt)%252B%25CE%25B1%255BRt%252B1%252B%25CE%25B3Q(St%252B1%252CAt%252B1)%25E2%2588%2592Q(St%252CAt)%255DQ(S_t%252C%2520A_t)%2520%255Cleftarrow%2520Q(S_t%252C%2520A_t)%2520%252B%2520%255Calpha%2520%255BR_%257Bt%252B1%257D%2520%252B%2520%255Cgamma%2520Q(S_%257Bt%252B1%257D%252C%2520A_%257Bt%252B1%257D)%2520-%2520Q(S_t%252C%2520A_t)%255DQ(St%25E2%2580%258B%252CAt%25E2%2580%258B)%25E2%2586%2590Q(St%25E2%2580%258B%252CAt%25E2%2580%258B)%252B%25CE%25B1%255BRt%252B1%25E2%2580%258B%252B%25CE%25B3Q(St%252B1%25E2%2580%258B%252CAt%252B1%25E2%2580%258B)%25E2%2588%2592Q(St%25E2%2580%258B%252CAt%25E2%2580%258B)%255D?scale=1)
  Q
  (
  S
  t
  ,
  A
  t
  )
  &#x2190;
  Q
  (
  S
  t
  ,
  A
  t
  )
  +
  
    &#x3B1;
  
  [
  R
  t
  +
  1
  +
  
    &#x3B3;
  
  Q
  (
  S
  t
  +
  1
  ,
  A
  t
  +
  1
  )
  &#x2212;
  Q
  (
  S
  t
  ,
  A
  t
  )
  ]
  Q
  (
  
    S
    t
  
  ,
  
    A
    t
  
  )
  &#x2190;
  Q
  (
  
    S
    t
  
  ,
  
    A
    t
  
  )
  +
  &#x03B1;
  [
  
    R
    
      t
      +
      1
    
  
  +
  &#x03B3;
  Q
  (
  
    S
    
      t
      +
      1
    
  
  ,
  
    A
    
      t
      +
      1
    
  
  )
  &#x2212;
  Q
  (
  
    S
    t
  
  ,
  
    A
    t
  
  )
  ]
  Q
  (
  S
  t
  &#x200B;
  ,
  A
  t
  &#x200B;
  )
  &#x2190;
  Q
  (
  S
  t
  &#x200B;
  ,
  A
  t
  &#x200B;
  )
  +
  
    &#x3B1;
  
  [
  R
  t
  +
  1
  &#x200B;
  +
  
    &#x3B3;
  
  Q
  (
  S
  t
  +
  1
  &#x200B;
  ,
  A
  t
  +
  1
  &#x200B;
  )
  &#x2212;
  Q
  (
  S
  t
  &#x200B;
  ,
  A
  t
  &#x200B;
  )
  ]
">

with parameters: α = 0.5, γ = 1.

Sample Experience Trajectory:

Sequence:

S0→A0→R1→S1→A2→R3→…

Tabular format showing transitions between states, actions, and rewards.

Key Differences:

TD(0): Directly updates the value function.

SARSA: Updates the action-value function (Q-values).

While value and policy iteration are powerful for known MDPs, real-world problems often involve uncertainty or unknown environments. Select Next to explore reinforcement learning, deep RL, and advanced frameworks for decision-making under uncertainty. 

Icon Progress Bar (browser only)

## Match 5: 10.9 Deep RL, Exploration, and Robust Decision-Making
- Source: Canvas Module: Module 10: Decision-Making
- Distance: 0.0060

Module: Module 10: Decision-Making

Item: 10.9 Deep RL, Exploration, and Robust Decision-Making

Type: Page

## Module 10
 10.9 Deep RL, Exploration, and Robust Decision-Making

In many AI systems, the environment is too large, dynamic, or partially observable to rely solely on classical MDP solutions. Techniques like deep reinforcement learning, robust reasoning and imprecise probabilities allow agents to learn and make decisions even under uncertainty.

### Deep reinforcement learning

When state/action spaces are large, Q-learning with tables becomes infeasible. **Deep Q-networks (DQN)** use neural networks to approximate Q-values:

![LaTeX: Q(s,a) ≈ Q(s,a; θ)](https://northeastern.instructure.com/equation_images/Q(s%252Ca)%2520%25E2%2589%2588%2520Q(s%252Ca%253B%2520%25CE%25B8)?scale=1)
  Q
  (
  s
  ,
  a
  )
  &#x2248;
  Q
  (
  s
  ,
  a
  ;
  
    &#x3B8;
  
  )
">

Where θ represents neural network parameters.

Breakthroughs enabled by deep RL include:

- Game playing: AlphaGo, Atari games, StarCraft II
- Robotics: Robotic manipulation, locomotion
- Autonomous systems: Self-driving cars, drone control
- Resource management: Data center cooling, traffic optimization

### Exploration vs. exploitation

When an agent is taking an action, it has a choice to perform the action it expects to give the highest reward or to take a different action and potentially learn something new. Because the ground truth is unknown, there is always a chance that the highest reward is still unknown. But if a lot of low-reward actions need to be taken before the agent finds that maximum reward, it may give a lower reward over a fixed amount of time. In that case, taking the best action known so far may end up yielding a higher reward. 

This is a fundamental challenge in RL. The agent needs to balance:

- **Exploration:** Trying new actions to discover better strategies
- **Exploitation:** Using currently known best actions to maximize reward

Common strategies to do this include:

- **ε-greedy:** With probability ε, choose random action; otherwise choose greedy action.
- **Upper Confidence Bound (UCB)**: Choose actions based on both estimated value and uncertainty. 
- **Thompson sampling:** Sample actions according to probability they're optimal.

### Alternative frameworks for uncertainty

While probability theory provides a robust framework for reasoning under uncertainty, some situations call for alternative approaches. These frameworks address limitations of classical probability when dealing with incomplete information, conflicting evidence, or imprecise knowledge.

#### Dempster-Shafer theory

Dempster-Shafer theory (also called belief function theory) extends classical probability to handle uncertainty about uncertainty itself. Instead of assigning probabilities to individual outcomes, it assigns probability masses to sets of outcomes.

 Select the tabs to learn about the key concepts in Dempster-Shafer theory.

### Mass Function (m)

 Assigns probability mass to subsets of outcomes

- m(A) represents the degree of belief that the true answer lies in set A
- Unlike probability, m(∅) = 0 and Σ m(A) = 1 over all subsets A

Select the next tab to learn more.

### Belief function (Bel)

Lower bound on probability

- Bel(A) = Σ m(B) for all B ⊆ A
- Represents minimum degree of belief in A

Select the next tab to learn more.

### Plausibility function (Pl)

Upper bound on probability

- Pl(A) = 1 - Bel(¬A)
- Represents maximum possible belief in A

#### Example: Medical diagnosis with uncertain evidence

A diagnostic system receives conflicting reports about a patient:

- Test A suggests: {Flu, Cold} with mass 0.7
- Test B suggests: {Flu, Pneumonia} with mass 0.8
- Unknown causes: mass 0.3 for Test A, 0.2 for Test B

Classical probability would force the assignment of specific probabilities to each disease. Dempster-Shafer theory allows the expression of uncertainty about which particular disease, while still reasoning about evidence.

Select each tab to learn about the advantages, disadvantages and applications of the Dempster-Shafer theory.

### Advantages

- Handles ignorance explicitly (can express "don't know")
- Combines evidence from multiple sources naturally
- Distinguishes between lack of belief and disbelief

Select the next tab to learn more.

### Disadvantages

- Computationally more complex than probability
- Can lead to counterintuitive results in some cases
- Interpretation of results can be challenging

Select the next tab to learn more.

### Applications

- Sensor fusion: Combining uncertain data from multiple sensors
- Expert systems: Reasoning with incomplete knowledge
- Intelligence analysis: Evaluating conflicting information sources

### Robust reasoning

Robust reasoning approaches acknowledge that probability models themselves may be uncertain or incorrect. Instead of assuming a single "true" probability distribution, these methods consider sets of possible distributions.

Instead of maximizing expected utility under a single probability distribution, robust approaches might:

- Maximize minimum utility: Choose the action that performs best in the worst-case scenario
- Minimize regret: Choose the action that minimizes maximum loss compared to optimal decisions
- Satisficing: Choose any action that meets minimum performance criteria

#### Example: Climate change planning

City planners must prepare for sea level rise but face deep uncertainty about:

- Rate of temperature increase
- Ice sheet dynamics
- Local geographic factors

Robust approach: Design infrastructure that performs adequately across a wide range of climate scenarios, rather than optimizing for a single predicted future. 

Select each tab to learn about the advantages and disadvantages of a robust approach.

### Advantages

- Accounts for model uncertainty
- Provides guarantees under worst-case conditions
- Less sensitive to precise probability estimates

Select the next tab to learn more.

### Disadvantages

- May be overly conservative
- Can ignore valuable probabilistic information
- Computational complexity

### Imprecise probabilities 

Imprecise probability theory uses sets of probability distributions rather than single distributions to represent uncertainty. This allows expression of partial ignorance about probabilities themselves.

Select the flip cards to learn about the key concepts in imprecise probability theory.

##### Credal sets

Sets of probability distributions representing uncertain knowledge 

##### Lower and upper probabilities

Bounds on probability values 

##### Interval probabilities

![LaTeX: P(A) ∈ [p̲, p̄] \textsf{ instead of }P(A) = p](https://northeastern.instructure.com/equation_images/P(A)%2520%25E2%2588%2588%2520%255Bp%25CC%25B2%252C%2520p%25CC%2584%255D%2520%255Ctextsf%257B%2520instead%2520of%2520%257DP(A)%2520%253D%2520p?scale=1)
  P
  (
  A
  )
  &#x2208;
  [
  p
  
    &#x332;
  
  ,
  p
  
    &#x304;
  
  ]
  
    &#xA0;instead of&#xA0;
  
  P
  (
  A
  )
  =
  p
">

#### Example: AI safety assessment

When evaluating the safety of a new AI system:

- Limited historical data makes precise probability estimates impossible
- Expert opinions vary widely
- High stakes make robust reasoning crucial

Imprecise probability approach: Express probability of safety as an interval [0.85, 0.95] rather than a point estimate like 0.9.

Select the tabs to learn more about decision-making with imprecise probabilities.

### Maximin

Choose an action that maximizes the minimum expected utility across all possible distributions.

Select the next tab to learn more.

### Maximax

Choose an action that maximizes maximum expected utility.

Select the next tab to learn more.

### Minimax regret

Choose an action that minimizes maximum regret.

#### Applications

Decision-making with imprecise probabilities has practical applications in fields where uncertainty is high and the stakes are significant, such as risk assessment, AI ethics, and financial regulation.

- Risk assessment: Nuclear safety, environmental policy
- AI ethics: Evaluating potential harms of AI systems
- Financial regulation: Setting capital requirements under model uncertainty

### Practical implementation considerations

Applying decision models to real-world AI systems often encounters computational hurdles. Challenges like large state spaces and continuous variables require careful design choices to keep models efficient and scalable.

Select each title to view more information about the practical considerations to be taken when implementing decision models. Open all sections simultaneously by selecting the Expand All Panels button     .  

#### Computational challenges

Real-world applications of Markov models and decision processes face significant computational challenges. These include state space exploration and continuous spaces. 

State space exploration challenges include:

- Realistic problems often have enormous state spaces
- Exact algorithms become computationally infeasible
- Approximation methods become necessary

Conituous spaces challenges include:

- Many real-world problems have continuous state/action spaces
- Discretization vs. function approximation trade-offs
- Sampling-based approaches

#### Scalability solutions

This section introduces scalability solutions for handling large or complex decision-making problems in AI. Techniques like function approximation, hierarchical methods, and Monte Carlo sampling help balance computational efficiency with learning performance.

Select each tab to learn more about key scalability solutions in AI decision-making.

### Function approximation

Use neural networks or other function approximators to represent value functions

Select the next tab to learn more.

### Hierarchical method

Break complex problems into manageable subproblems

Select the next tab to learn more.

### Approximate dynamic programming

Trade optimality for computational feasibility

Select the next tab to learn more.

### Monte Carlo methods

Use sampling to approximate intractable computations

### Model learning and adaptation

Model learning and adaptation enable AI systems to adjust their internal models in response to new data and changing environments. This ensures continued optimal performance, even under uncertainty, partial observability, or evolving conditions. Techniques like online learning, transfer learning, and safe exploration support this adaptability.

Real-world systems must often learn their models online; the following depicts the challenges and possible solutions to this method of learning.

###### Challenges

- Non-stationary environments (transition probabilities change over time)
- Partial observability
- Safety constraints during learning
- Sample efficiency requirements

###### Solutions

- Online learning algorithms that adapt to changing environments
- Transfer learning to leverage knowledge from similar problems
- Safe exploration methods that maintain safety during learning
- Meta-learning approaches that learn how to learn quickly

###  Use case: Adaptive traffic control

This use case illustrates how adaptive traffic control systems use AI to learn and respond to dynamic traffic patterns. By combining online learning, safe exploration, and hierarchical planning, these systems optimize flow while handling uncertainty and maintaining safety.

Select each tab to explore how adaptive traffic control systems tackle real-world challenges.

### A smart traffic light system must

- Learn traffic patterns that change throughout the day
- Adapt to seasonal variations and special events
- Maintain safety while exploring new timing strategies
- Handle sensor failures and partial information

Select the next tab to learn more.

### The system uses

- Online MDP learning to adapt to traffic patterns
- Safe exploration to ensure traffic flow is maintained
- Hierarchical decomposition (daily patterns, hourly patterns, minute-by-minute adjustments)

Select Next to explore how the techniques you’ve studied can be applied in real-world systems and what principles guide the design of sequential decision-making.

Icon Progress Bar (browser only)
