# course-content
This is the CIS 522 course, being updated for 2023

# Course Description
 
Deep learning now touch on data systems of all varieties. It can be a product itself; optimize a pipeline, provide critical insights, shed light on neuroscience, or scare us by providing remarkably human-like text. The purpose of this course is to deconstruct the hype by teaching deep learning theories, models, skills, and applications that are useful for applications. Here, we will shed light on the methods behind the “magic” of Deep Learning.

# Course Setup 
In this course, we reimagine the way Deep Learning is taught by diverging from traditional lecture-based instruction. We believe that Deep Learning should be taught in an environment that focuses on collaboration, implementation, and active learning. 

Our course has a flipped classroom setup. Students will, in part on their own time and in part of a group activity go through prepared mixtures of lectures and exercises (for an example see: https://colab.research.google.com/github/CIS-522/course-content/blob/main/tutorials/W03_MLPs/student/W3_Tutorial1.ipynb). The in person components of the course will aim at deeper understanding, discussion, and clarity.

In our deep learning course much of the learning happens in small groups - referred to as pods. Each pod will have roughly 15 students, and will be led by a TA. Every week, the pod will meet for 5h, where they will collaboratively work through parts of the tutorials and above all will jointly work on understanding the materials. Attendance to the pod is mandatory, happens in person, and is part of the class’ lecture time. The professors will rotate through these pods.

# Grading
We strive to use grades that get at the process of learning while also giving the chance to show mastery. 10% show up, 10% participate, 10% askgood qustions, 10% go beyond taught materials, 10% good coding/style, 10% systems understanding, 20% homework (including points for competitive solutions), 10% helpfulness. 10% project,  All scores will be curved within and across pods for an average grade of A-. ![image](https://user-images.githubusercontent.com/3504693/210634860-8e9e3679-e5a9-4bea-a68b-62d7159d2abd.png). You have two absence weeks in the pod and 1 missing homework that will simply be ignored. Late submissions are only accepted upon specific approval by the professors.

# Collaboration/Resources
For the class-time you are welcome and encouraged to work together with your entire pod. For homework you are allowed to use any resource on the internet, but are not allowed to use any hope by humans. This means that you are welcome to use chatGPT and similar tools for code generation.

# Wellness Statement
Reach out to your TA if you are experiencing extenuating or special circumstances that are ongoing for a shorter period of time, say two weeks. Reach out to one of the professors if things run for longer/ there is a need for specific changes for you.

We strive to produce a positive learning environment. UPenn has plenty of mental health resources to offer (https://wellness.upenn.edu/). Make sure you are your best to all other students and team members. For specifi. insights see also the upenn harrassment policies (https://catalog.upenn.edu/pennbook/sexual-misconduct-resource-offices-complaint-procedures/) and the UPenn code of conduct (https://catalog.upenn.edu/pennbook/code-of-student-conduct/). 


# DEI Statement
We strive to uphold the University of Pennsylvania’s dedication to diversity and inclusion inside and outside of the classroom
Deep learning touches on many issues related to (lack of) diversity and inclusion. Some exposure to problems in the DEI space is a crucial part of the content of this course.

# Schedule

## Week 1: Introduction
Where we get to know one another, successfully implement alphaZero and use it to solve Othello but realize that we would not have been able to build it from scratch
Plenty of team building. Get used to PyTorch. Do the coolest few lines of alpha zero. See the forest. Not understand the trees.

## Week 2: Linear
Where we implement linear DL from scratch and learn that the various components of DL are so much deeper and more fun than we thought. 
Really build stuff in pytorch. Variable types, autograd as a concept, the compute graph,  low rank matrix stuff, race models, network initialization, cost functions. Debug something with vanishing gradients. Linear neurons in neuroscience, intuitions about high-d spaces

## Week 3: Multilayer Perceptrons
Where we implement MLPs, see how well they often work, and obtain a real meaningful understanding of why and when they work	
Transfer functions, Real neuron transfer functions, Completeness proof for MLP, construction for completeness. Why MLPs are good at interpolation. Why the exact choice of transfer functions matters. Discretization allows nonlinear computation in linear networks. More cost functions, hinge loss/SVM link, weight initialization. Debug something with bad initialization. Nonlinear neurons in neuroscience
 
## Week 4: Optimization and regularization 
Where we talk show how gradient descent can be tweaked (minibatch, adagrad…) to really speed things up, and hint at the theory behind it.	
The landscape we optimize over.  SGD, AdaGrad, Adam, and how they affect generalization.  Batchnorm, minibatch. We see how ANNs can fit anything. Overparameterization and regularization: L2, dropout, early stopping. SGD as a regularizer, effect of minibatch size. Why DL often miraculously works and generalizes.

## Week 5: Convnets
Where we learn about convnets, implement a few versions of them, and learn the right intuitions and ways of seeing where and how we want to use them
Hierarchical processing in the brain, Neocognitron, Build a convnet. Visualize the outputs of level 2. Intuition for invariance/equivariance. Visualize at higher levels. Re-using weights, max layers, padding, unpooling, edge detection through convolution, convolution by hand, 3d convolution,1x1 convolutions. What backprop does in convnets.

## Week 6: 
Where we talk about the specifics of vision problems and the magic of transfer learning				
Domain adaptation, transfer learning, multi-task/continual learning. Attention networks, pose tracking, kaggle competitions

## Week 7: 
Where we play with Autoencoders, implement GANs and discover how we can make an artificial world
Generative models. VAEs, pPCA, nonlinear CCA. GANs. 

## Week 8: 
Where we play with architectures, and learn about RNNs and Attention and work with text		
RNNs, GRUs, LSTMs,seq2seq, the role of attention, symbol-like computations, memory in brains, 

## Week 9: 
Where we solve NLP and muse about the meaning of text.		CNNs/LSTMs on text for tagging and classification; word embeddings: Word2Vec,  BERT/transformers,  encoder/decoder in seq2seq, attention for language

## Week 10: 
Where we review RL, and how it  can be  deep				Mode-based and model-free RL.  Good ways to represent policies/values. Speeding up learning. Exploration, off-policy methods, inverse reinforcement learning, goal conditioning, multi-agent RL.

## Week 11: 
Where we successfully implement alphaZero and use it to solve Othella but this time we can appreciate the details and have the skills to improve it
Alpha zero. Only now we make everything better.

## Week 12: 
Where students get to repeat what they really should know and start projects
Transfer functions, Cost functions, Optimizers, MLPs, convnets, GANs, RNNs, NLP, RL, and the meaning of life.   

# Week 13+: 
Projects		
