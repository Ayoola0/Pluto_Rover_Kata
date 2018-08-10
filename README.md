# PSTRUCTURING A MACHINE LEARNING PROJECT

What is Machine Learning?
A subject of AI in the field of computer science that often uses statistical techniques to give computers the ability to “learn” with data without being explicitly programmed.
It can also be described as a method of teaching computers to make and improve predictions or behaviours based on some data.
It can also be described as the act of teaching a programme to recognise patterns.
ML is about atomizing the ineffable. Explanation via examples rather than instructions.

Orthogonalization: 
A way to alter only 1 aspect of the output whilst keeping the rest intact. AKA, 1 switch for 1 change.

Chain of Assumptions in Machine Learning:
For a supervised learning system to do well, you need to turn the “knobs” of your system to make sure 4 things hold true:
Fits training set well, based on desired objectives
Bigger Network or better optimization algorithm E.G. Adam’s optimisation. 
2. Fits Dev set well based on desired objectives
Regularization can be used or use bigger training set.

   3. Fits set well based on desired objectives
Bigger dev set.
  4. Performs well in real world therefore solves problem intended.
Change Dev set or objectives


TYPES OF EVALUATION METRICS

Single Number Evaluation Metrics:
Allows you to quickly check if your new idea really improves on previous ones (Recommended to establish this at the start of the programme.) e.g. F(1) score.
  Method of improving your algorithm 

   Definitions
Precisions: Algorithm accuracy %
Recall: From a set of data, what % code the algorithm recognise % effectiveness.
 
   Problem
There is usually a trade off between precision and recall.

Solution
Use a new metric e.g. F1 Score


Informally “Average of Precision and Recall”.
A well defined Dev Set will help with measuring Precision and Recall.
 


Benefits of Single Number Metrics
. Improves efficiency with Decision making when selecting which algorithm to use
           
     2.Satisficing and Optimizing Metrics for each (set)

Optimising metric: The one you want to maximize 
Satisficing metric: The One you keep at a desired  level
(E.g. Accuracy given time taken</= 100ms)

Setting up your goal
Training set/ dev/ test set distribution

Development set -aka- hold out cross validation set
Ensure Dev and test set come from the same distribution 
Setting on Dev set + single number evaluation metric. 

. Choose a dev set and test set to reflect data you except to get in the future and consider important to do well on.
. 
Size of test set:  
Set your test set to be big enough to give high confidence in the overall performance of your system.

When to change dev/test sets and metrics

When there is a metric classification error
No longer correctly ranking preference
     Eg lower error but porn display   <- metric preference
          Vs higher error but not indirecting <- user preference 
Mathematical definition of error: Counts number of misclassified examples

 Solution
Add a weight to increase the error if undesired output shown 

 
If doing well on your metric and dev/test set does not correspond to doing well on your application, change your metric and/or dev/test set.
If it doesn’t work well in the real world (to reflect real world situation).


 
Human level performance
If Machine Learning is worse than humans, you can:
Get labelled data from humans to feed algorithms
Better analysis of bias/variants
Gain insight from manuel error analysis (why did this person get it right)

Avoidable bias
  Gap between Bayes error and Training error.
Variace
  Gap between Training error and dev error 
Important to know bayes error so you error so you know what to focus on.

Machine Learning Surpassing Human Level Performance
Eg online advertising product recommendations, logistics
-What type of data is this possible with?
.Structured data/ data based
.Not natural perception based
.Lots of data

The 2 Fundamentals Assumptions to Supervised Learning
.You can fit the training set pretty well *(low Avoidable bias).
.The training set performance generalize pretty well to the dev/test *(low variable).

Reducing avoidable bias and variable
Human level 





Training error




Dev error  




[CS231:]

Error Analysis: When your algorithm is  not yet at human level
. If you have 12% error you could:
A) Collect more data to improve performance ->Months
OR
B) Get ~100 mislabeled dev set examples
Count up how many are dogs eg 5%

[A] is not wise as this could take months for a marginal improvement.
[B] this will reduce error by a relative 5% ie. from 10% to 9.5% -> Ceiling

Evaluating Multiple ideas in Parallel: focus
How to choose which error to work on. 

Image
Error type
ET2
ET3
ET4
Comments
1
/








2


/
/




3
/




/


4






/


…..




/




….










% of total
8%
[6%]
11%
1%



Makes sense to work on ET2 first
Categorize the types of error you are facing
Update error type as you discover more
This process above usually takes a few hours but vital to not waste time for less than proportionate improvements.
Find a set of mislabeled examples in Dev/Test set
Look at the mislabelled example for false positives and false negative categories.
Count up of the errors that fall into different categories
Helps you prioritize which direction to go in.

Cleaning up Incorrectly Labelled Devs

Y=1 for(...)
Y=0 for non-(...)

Eg. 
x
C
D
C
C
D
D
C
y
1
0
1
1
0
1
1

Mislabelled
Training Set
DL algorithms are quite robust to random errors in the training set
No need to correct data if errors are random and data set is long enough. (No harm is doing so the)
DL algorithms are less robust to systematic errors (eg. white dogs labelled as cats)

Dev Set
Add a column of incorrectly labelled to error analysis, count the number of (...) when y is wrong.
  > Is it worth going in and relabelling? Only if it makes a difference on ability to hit target/ evaluate classifiers 
Things to Examine when considering whether to go to reduce mislabeled examples
Overall dev set error 
Number of errors due to incorrect labels 
Error due to other causes
Goal of Dev set is to help you select between 2 classifiers A and B.


A
B
Overall Dev set error
2%
1.9%
Errors due to incorrect labels
0.6%
0.6%
Errors due to other causes
1.5%
1.3%

Since you can’t trust the labels of Dev set, it is wise to go out to improve the labels.

Correcting Incorrect Dev/Test set examples
-Apply same process to Dev and Test sets to make sure they continue to come from the same distribution. 
-Examine the examples the algorithm got right as well as ones it got wrong as both could contain errors.
Training and Dev/Test may now come from slightly different distributions.

Error Analysis: Usually carried out on Training/Dev error
Building your first system quickly then (....)
Set up Dev and Test set and metric
Build initial system quickly
Use bias/variant analysis and error analysis to prioritise next steps.

Training and Testing on Different Distributions
DL Algorithm have a hunger for huge training data 
They work best when you can find enough labelled
l> Propensity to shove whatever data you can find and shoving it into the training set even if the data is not from the same distribution as Dev and Test data
l> Best practice when Training data and Dev/Test data are from different distributions
Option 1: Merge both data sets, randomly shuffle then allocate

Training
Dev
Test
 




Advantages:
>Dev and test set are from same distribution

Disadvantages:
>Dev set from un-preferred (......) set/distribution eg~~ 2351/2500 from unwanted distribution.

Option 2: 





Advantages: 
>Aiming targets where you want it to be

Disadvantages:
>Training distribution is different to Dev/Test set

Should you always use all the data you have
.Bias and Variance with mismatched data distribution
I.e. when Training data from a different distribution  to understand if Variance truly exists
E.g
Training error 1%
Dev error 10%

Solution


Training error
1%
1%
Training Dev set error


9%
1.5%
Dev error
10%
10%

Addressing Data Mismatch problems (not a systematic problem)
Carry out manual error analysis to try to understand differences between training and Dev/Test sets

luto_Rover_Kata
Using TDD to solve a software engineering problem


