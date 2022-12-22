---
title: "Introduction"
---

[% root README.md %]

## An Example {: #introduction-example}

Are some programmers really ten times more productive than average?
To find out,
[%b Prechelt2000 %] had a set of programmers solve the same problem in the language of their choice,
then looked at how long it took them,
how good their solutions were,
and how fast those solutions ran.
The data,
which is [available online][prechelt_data],
looks like this:

```
person,lang,z1000t,z0t,z1000mem,stmtL,z1000rel,m1000rel,whours,caps
s015,C++,0.050,0.050,24616,374,99.24,100.0,11.20,??
s017,Java,0.633,0.433,41952,509,100.00,10.2,48.90,??
s018,C,0.017,0.017,22432,380,98.10,96.8,16.10,??
s020,C++,1.983,0.550,6384,166,98.48,98.4,3.00,??
s021,C++,4.867,0.017,5312,298,100.00,98.4,19.10,??
s023,Java,2.633,0.650,89664,384,7.60,98.4,7.10,??
s025,C++,0.083,0.083,28568,150,99.24,98.4,3.50,??
...
```

The columns hold the following information:

| Column | Meaning |
| ------ | ------- |
| person | subject identifier |
| lang | programming language used |
| z1000t | running time for z1000 input file |
| z0t | running time for z0 input file |
| z1000mem | memory consumption at end of z1000 run |
| stmtL | program length in statement lines of code |
| z1000rel | output reliability for z1000 input file |
| m1000rel | output reliability for m1000 input file |
| whours | total subject work time |
| caps | subject self-evaluation |

The `z1000rel` and `m1000rel` columns tell us that
all of these implementations are correct 98% of the time or better,
which is considered acceptable.
The rest of the data is much easier to understand as a [%g box_and_whisker_plot "box-and-whisker plot" %]
of the working time in hours (the `whours` column from the table).
Each dot is a single data point
([%g jitter "jittered" %] up or down a bit to be easier to see).
The left and right boundaries of the box show the 25th and 75th [%g percentile "percentiles" %] respectively,
i.e., 25% of the points lie below the box and 25% lie above it,
and the mark in the middle shows the [%g median "median" %]
([%f introduction-boxplot %]).

[% figure
   slug="introduction-boxplot"
   img="boxplot.svg"
   caption="Development Time"
   alt="Box-and-whisker plot show that most developers spent between zero and 20 hours but a few took as long as 63 hours."
%]

So what does this data tell us about productivity?
As [%b Prechelt2019 %] explains,
that depends on exactly what we mean.
The shortest and longest development times were 0.6 and 63 hours respectively,
giving a ratio of 105X.
However,
the subjects used seven different languages;
if we only look at those who used Java (about 30% of the whole)
the shortest and longest times are 3.8 and 63 hours,
giving a ratio of "only" 17X.

But comparing the best and the worst of anything is guaranteed to give us
an exaggerated impression of the difference.
If we compare the 75th percentile (which is the middle of the top half of the data)
to the 25th percentile (which is the middle of the bottom half)
we get a ratio of 18.5/7.25 or 2.55;
if we compare the 90th percentile to the 50th we get 3.7,
and other comparisons give us other values.
The answers to our original question are therefore:

1.  It depends what you mean.

2.  No, good programmers aren't 10 times more productive than average.

3.  But yes, it's reasonable to say that they are about four times more productive.

The last point begs the question, "Why?"
The rest of this book offers some answers.

## Audience {: #introduction-audience}

Every lesson should have specific learners in mind [%b Wilson2019 %].
These [%i "learner persona" %][personas][t3_personas][%/i%] describe ours:

-   *Yanina* is in the third year of a computer science degree.
    She worked on several volunteer projects in high school and at her mosque,
    but the "Introduction to Software Engineering" course she's about to take
    will be her first large team project at university.
    This book will help her and her teammates figure out what to do when and now.

-   *Brad* is in Yanina's classes.
    He can do many assignments in half the time it takes other students,
    which he attributes to innate aptitude
    rather than to his parents having sent him to after-school coding camps
    since he was nine years old.
    He finds discussion of what he calls "social justice bullshit" tiresome;
    this book will help him understand why that attitude is self-defeating.

-   *Ahmadou* worked as an illustrator for several years
    before doing an intensive 14-week conversion course to become a JavaScript developer.
    He has a lot of experience working in teams to meet deadlines,
    but is still often bewildered by the tools, jargon, and culture of programming.
    This book will help him figure out what his programming colleagues think is "normal".

-   *Sharla* teaches JavaScript at Yanina's college
    and for the conversion course that Ahmadou went through.
    They taught the "Introduction to Software Engineering" class last semester,
    but felt their students wasted a lot of time on things that turned out not to be useful.
    This book will help them give more structure to the next offering
    and set more realistic expectations.

Like these personas, readers should:

-   Be able to write multi-page programs in Java, Python, JavaScript,
    or some other modern programming language.

-   Be able to create static web sites using HTML and CSS.

-   Know how to create directories, delete files, and find things with the Unix shell.

-   Have used [Git][git] on individual projects.

## Acknowledgments

This book is dedicated to [%i "Petre, Marian" %][Marian Petre][petre_marian][%/i%],
who taught me that not everything worth studying can be measured,
and to [%i "Wilkie, Tom" %]Tom Wilkie[%/i%],
who taught me how to turn a thousand words I'd written into a hundred someone would actually want to read.
I am grateful to all of the students who have done projects with me over the years,
and for feedback from the people listed below.
Any remaining errors or omissions are mine alone.

[% acknowledgments %]

Finally,
I would like to thank [%i "Graf, David" %]David Graf[%/i%] for [%i "doi2bib" %][doi2bib][doi2bib][%/i%]
and [%i "Elbakyan, Alexander" %]Alexandra Elbakyan[%/i%] for [%i "Sci-Hub" %][Sci-Hub][sci_hub][%/i%]:
writing this book would have been much harder without their idealism and hard work.

## Exercises {: #introduction-exercises}

FIXME
