---
title: "Introduction"
---

This book will help you succeed in your first team software project.
Some of the tools we describe are technical,
like version control and testing frameworks;
others will help you form teams,
manage people who aren't pulling their weight,
cut features when time runs short,
and understand who should get credit for what you build.

All of the content is free to use under a Creative Commons license,
and all of the software can be re-used under an ethical source license;
please see the license file for details.
Fixes and additions are very welcome:
please see our contribution guide and governance guide for details
and please note that all contributors must abide by our Code of Conduct.

## What distinguishes this book from others?

This book differs from most other introductions to software engineering in two ways:

1.  Our aim is to teach you how to be a *compassionate programmer*:
    one who cares about the well-being of their colleagues and users.
    This focus is not entirely altruistic—everything you do to help others
    also helps your future self—but now that we know how much harm software can do,
    we need to learn to build it in better ways.

2.  Wherever possible,
    we base our recommendations on empirical studies
    of software and the people who build it.
    To help you understand and evaluate these studies,
    our running example is a series of data science problems
    rather than an online store or video game.

Many of the hard problems in software engineering stem from the fact that
we have to design programs to fit our limited mental capacity [% b Hermans2021 %].
Many others are rooted in the social psychology of group interactions,
or in our tendency to believe what people around us believe
rather than examining evidence.
We are therefore guided throughout by a modified version of [Dobzhansky's Rule][dobzhansky]:

> Nothing in software engineering makes sense except in the light of psychology.

## What do you mean by "evidence"?

Are some programmers really ten times more productive than average?
To find out,
[% b Prechelt2000 %] had N programmers solve the same problem
in the language of their choice,
then looked at how long it took them,
how good their solutions were,
and how fast those solutions ran.
The data is [available online][prechelt-data],
and the first few rows look like this:

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

[% figure slug="boxplot" img="boxplot.svg" caption="Development Time" alt="Box-and-whisker plot show that most developers spent between zero and 20 hours but a handful took as long as 63 hours." %]

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

## Who is this book intended for?

Every lesson should be written with specific learners in mind.
These [personas][t3-personas] describe ours:

-   Yanina is in the third year of a computer science degree.
    She worked on several volunteer projects in high school and through her mosque,
    but the "Introduction to Software Engineering" course she's about to take
    will be her first semester-long team project at university.
    This guide will help her and her teammates figure out what to do when.

-   Ahmadou worked as a lab technician doing genomic assays for several years
    before doing an intensive 14-week conversion course to become a software developer.
    He has a lot of experience meeting deadlines on his own and in teams,
    but is still often bewildered by the tools, jargon, and culture of programming.
    This guide will help him figure out what his programming colleagues think is normal.

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

-   Be able to create a web site using HTML and CSS.

-   Know how to create directories, delete files, and find things with the Unix shell.

-   Have used [Git][git] on individual projects.

## Acknowledgments

This book is dedicated to all of the students who have done projects with me over the years.
I would also like to thank
Alexandra Elbakyan for [Sci-Hub][sci-hub]:
this book would have been impossible to write without her idealism and hard work.
