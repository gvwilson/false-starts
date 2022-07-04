---
title: "Introduction"
---

[% b Sedano2017 %] found that software development projects have nine types of waste:
building the wrong feature or product,
mismanaging the backlog,
rework,
unnecessarily complex solutions,
extraneous [% g cognitive_load "cognitive load" %],
psychological distress,
waiting and multitasking,
knowledge loss,
and ineffective communication.
*None of these are in your software.*
Instead,
they stem from the fact that
we have to design programs to fit our limited mental capacity [% b Hermans2021 %]
or are rooted in the social psychology of group interactions.
We are therefore guided throughout this book by a modified version of [Dobzhansky's Rule][dobzhansky]:

> Nothing in software engineering makes sense except in the light of psychology.

## A Quick Example

Are some programmers really ten times more productive than average?
To find out,
[% b Prechelt2000 %] had a set of programmers solve the same problem in the language of their choice,
then looked at how long it took them,
how good their solutions were,
and how fast those solutions ran.
The data,
which is [available online][prechelt-data],
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
The rest of the data is much easier to understand as a [% g box_and_whisker_plot "box-and-whisker plot" %]
of the working time in hours (the `whours` column from the table).
Each dot is a single data point
([% g jitter "jittered" %] up or down a bit to be easier to see).
The left and right boundaries of the box show the 25th and 75th [% g percentile "percentiles" %] respectively,
i.e., 25% of the points lie below the box and 25% lie above it,
and the mark in the middle shows the [% g median "median" %]
([% f boxplot %]).

[% figure
   slug="boxplot"
   img="boxplot.svg"
   caption="Development Time"
   alt="Box-and-whisker plot show that most developers spent between zero and 20 hours but a few took as long as 63 hours."
%]

So what does this data tell us about productivity?
As [% b Prechelt2019 %] explains,
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

## Who You Are

Every lesson should be written with specific learners in mind.
These [personas][t3-personas] describe ours:

-   Yanina is in the third year of a computer science degree.
    She worked on several volunteer projects in high school and through her mosque,
    but the "Introduction to Software Engineering" course she's about to take
    will be her first semester-long team project at university.
    This guide will help her and her teammates figure out what to do when.

-   Brad is in Yanina's classes.
    He started programming when he was nine years old,
    and as a result can do many assignments in half the time it takes other students
    (something he attributes to intelligence and aptitude
    rather than to his parents being able to afford to send him to after-school coding camps).
    He finds any discussion of what he privately called "social justice bullshit" tiresome;
    this guide will help him understand why that attitude is self-defeating.

-   Ahmadou worked as an illustrator for several years
    before doing an intensive 14-week conversion course to become a JavaScript developer.
    He has a lot of experience working in teams to meet deadlines,
    but is still often bewildered by the tools, jargon, and culture of programming.
    This guide will help him figure out what his new colleagues think is "normal".

-   Sharla teaches JavaScript at Yanina's college
    and for the conversion course that Ahmadou went through.
    They taught the "Introduction to Software Engineering" class last semester,
    and came away feeling that their students had wasted a lot of time
    on things that turned out not to be useful.
    This guide will help them give more structure to the next offering
    and set more realistic expectations.

Like these personas, you should:

-   Be able to write multi-page programs in Java, Python, JavaScript,
    or some other modern programming language.

-   Be able to create a web site using HTML and CSS

-   Know how to create directories, delete files, and find things with the Unix shell.

-   Have used Git on individual projects.

## Acknowledgments

This book is dedicated to [% i "Petre, Marian" %][Marian Petre][petre-marian][% /i %],
who taught me that not everything worth studying can be measured,
and to [% i "Wilkie, Tom" %]Tom Wilkie[% /i %],
who taught me how to turn a thousand words I'd written into a hundred someone would actually want to read.
I am also grateful to my previous co-authors for making material available under open licenses,
and to [% i "Elbakyan, Alexander" %]Alexandra Elbakyan[% /i %] for [% i "Sci-Hub" %][Sci-Hub][sci-hub][% /i %]:
this book would have been impossible to write without her idealism and hard work.
