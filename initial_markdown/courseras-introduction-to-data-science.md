Title: Coursera's Introduction to Data Science course
Date: 2013-07-14 13:13
Author: Steven Maude (noreply@blogger.com)
Tags: data, course, Coursera, analytics, science
Slug: courseras-introduction-to-data-science

I've recently become a lot more interested in what [data
science](http://en.wikipedia.org/wiki/Data_science) involves — to the
point of considering careers that use these skills — so when I noticed
Coursera's [Introduction to Data
Science](https://www.coursera.org/course/datasci) course taught by
[Prof. Bill Howe](http://homes.cs.washington.edu/~billhowe/) at the
University of Washington, I decided to take it. I finished the last
assignment this weekend, so it's a good time to write up my thoughts
while they're still fresh.  
  
The first week gave a quick overview of what data science is and why
it's becoming increasingly important. From then on, it covered a lot of
topics. Starting with traditional
[SQL](https://en.wikipedia.org/wiki/SQL) databases, we moved on to
covering
[MapReduce](http://ayende.com/blog/4435/map-reduce-a-visual-explanation)
algorithms, [NoSQL](https://en.wikipedia.org/wiki/NoSQL) databases,
statistical topics relevant to large data sets, unsupervised and
supervised [machine
learning](https://en.wikipedia.org/wiki/Machine_learning) algorithms,
[graph](https://en.wikipedia.org/wiki/Graph_theory) analytics, and
looked at data visualisation considerations (particularly features that
can help make visualisations easy for the viewer to comprehend).  
  
The lecture style was pretty brisk. Lectures were broken up into short
5-15 minute segments, but often information dense. This isn't a bad
thing. The fact the lectures are recorded means that you can repeat
sections, or go and look something up for more details. Usually, the
lectures weren't too difficult to follow. There were a few occasions
where I think a little *too*much was crammed in. One instance: rule
learning by sequential covering was discussed in less than five minutes
which was far too short to explain clearly. It took me another 20
minutes of reading and working through this
[explanation](http://www.cs.bc.edu/~alvarez/DataMining/Notes/covering.html)
to actually grasp the concept properly.  
  
On the other hand, the emphasis on breadth rather than depth in the
course fits well for an introductory course. It gives you sufficient
grounding and the vocabulary to start understanding concepts you might
encounter elsewhere, and points you in the right direction to look
further. I was impressed at the considerable amount I learnt about
technologies that I knew nothing about previously.  
  
The range of assignments was diverse: analysing tweets, using SQL
databases and implementing some very simple MapReduce algorithms. There
were also two open ended, assignments: using [Tableau
Desktop](http://www.tableausoftware.com/) to do some data visualisation,
and entering a [Kaggle](https://www.kaggle.com/) competition. In these,
it was up to the student to choose a question and challenge themselves.
This approach was a good way of handling the very varied academic
backgrounds of students on the
course.[](https://www.blogger.com/blogger.g?blogID=2392456333762205400#1)  
  
Entering a Kaggle competition was interesting. Even with the
[tutorials](https://www.kaggle.com/c/titanic-gettingStarted) Kaggle
provides, it's a little intimidating if you haven't tackled those kind
of predictive model problems before. Because it was a part of the
course, it gave me the motivation to have a go and try using
[scikit-learn](http://scikit-learn.org/); this is certainly a positive.
I'm more aware now of the issues in working with other people's data
sets: often a large part of the problem is deciding how to handle
missing data.  
  
(There were also a further two optional assignments, which I skipped due
to a lack of spare time. One of these was a real world project, so there
was no shortage of ways in which you could delve in more deeply should
you wish.)  
  
Three of the assignments used Python and required some basic language
knowledge to complete them. However, if you weren't familiar with Python
prior to the first assignment, being thrown in head first to it was
probably not the most fun or easiest way to go about learning it. If you
were going to take this course, it's definitely worth working through a
few tutorials beforehand to learn the basics in Python (data types,
expressions, conditionals, loops, functions); these are good
[lectures](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011)
and this is a [good free
book](http://www.greenteapress.com/thinkpython/).   
  
There were some initial grading issues that meant the course didn't get
off to the start that was probably hoped. The first assignment was
autograded but, with having to deal with
[Unicode](http://www.joelonsoftware.com/articles/Unicode.html) strings,
input data sets likely being unique for everyone, and opaque grading
feedback, it made for a difficult experience.  
  
Completing the actual assignment itself didn't require any complicated
coding. Getting the grader to recognise that you had the right answer
was something else entirely. I spent more time on the latter than the
former. It didn't help that the grader became increasingly slow to
respond as users were subjecting it to repeated attempts, making the
whole process a little bit frustrating and to the detriment of the
assignment itself (which was actually an interesting one, analysing mood
sentiment of tweets).  
  
This was several weeks ago and a fairly distant memory now. In fairness
to the staff, they listened to feedback and most of the subsequent
assignments were handled more smoothly. Over the past week, I have read
some complaints about having the use of Tableau for the final
visualisation assignment, but I personally haven't had any problems with
it.  
  
There was a post on the course forums suggesting that the course is
going to be repeated, tentatively next spring. At the moment, I'm not
aware of any free courses that discuss the subject as a whole (there are
several that discuss [machine
learning](https://www.coursera.org/course/ml)). With that in mind, one
strong aspect was how this course linked ideas together. It never seemed
like topics were thrown in there simply for the sake of it and
frequently ideas (especially relational algebra) were recurring
throughout. Overall, I'm glad I completed the course; I learnt a lot
from it. If you want to take a starter course in data science, I
wouldn't hesitate to recommend it. Thanks to the staff for providing it!
