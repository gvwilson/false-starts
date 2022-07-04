---
title: "Introduction"
lede: "Who you are and what you'll learn"
template: page
---

This book will help you succeed in your first team software project.
Some of the tools we describe are technical,
like version control and testing frameworks;
others will help you form teams,
manage people who aren't pulling their weight,
cut features when time runs short,
and understand who should get credit for what you build.

*SECA* differs from other introductions to software engineering in three ways:

1.  Our aim is to teach you how to be a *compassionate programmer*:
    one who cares as much about the well-being of their colleagues and users.
    This focus is not entirely altruistic—everything you do to help others
    also helps your future self—but now that we know how much harm software can do,
    we need to learn to build it in better ways.

2.  Wherever possible,
    we base our recommendations on empirical studies
    of software and the people who build it.
    To help you understand and evaluate these studies,
    we use data science problems for our examples.

3.  All of the content is free to use under a Creative Commons license,
    and all of the software can be re-used under an ethical source license;
    please see the license file for details.
    Fixes and additions are very welcome:
    please see our contribution guide and governance guide for details
    and please note that all contributors must abide by our Code of Conduct.

Many of the hard problems in software engineering stem from the fact that
we have to design programs to fit our limited mental capacity [% b Hermans2021 %].
Many others are rooted in the social psychology of group interactions,
or in our tendency to believe what people around us believe
rather than examining evidence.
We are therefore guided throughout by a modified version of [Dobzhansky's Rule][dobzhansky]:

> Nothing in software engineering makes sense except in the light of psychology.

## Audience

Every lesson should be written with specific learners in mind.
These [% i "learner persona" %][personas][t3-personas][% /i %] describe ours:

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

Like these personas, readers should:

-   Be able to write multi-page programs in Java, Python, JavaScript,
    or some other modern programming language.

-   Be able to create static web sites using HTML and CSS.

-   Know how to create directories, delete files, and find things with the Unix shell.

-   Have used [Git][git] on individual projects.

This book can be read on its own or as a companion to *[Software Design by Example][stjs]*,
which teaches the basics of software design
by showing you how to build the tools you program with.
If you are looking for a project to do in a course,
adding a tool to those covered there would be fun as well as educational.

## Using and Contributing

All of the written material on this site is made available
under the [Creative Commons - Attribution - NonCommercial 4.0 International license][cc-by-nc]
(CC-BY-NC-4.0),
while the software is made available under the [Hippocratic License][hippocratic-license].
The first allows you to use and remix this material for non-commercial purposes,
as-is or in adapted form,
provided you cite its original source;
the second allows you to use and remix the software on this site
provided you do not violate international agreements governing human rights.
Please see [% x license %] for details.

If you would like to improve what we have or add new material,
please see the Code of Conduct in [% x conduct %]
and the contributor guidelines in [% x contributing %].

## Acknowledgments

This book is dedicated to [% i "Petre, Marian" %][Marian Petre][petre-marian][% /i %],
who taught me that not everything worth studying can be measured,
and to [% i "Wilkie, Tom" %]Tom Wilkie[% /i %],
who taught me how to turn a thousand words I'd written into a hundred someone would actually want to read.
I am also grateful to [% i "Taylor & Francis" %][Taylor & Francis][taylor-francis][% /i %],
[% i "PLoS" %][PLoS][plos][% /i %],
and my previous co-authors for making material available under open licenses,
to all of the students who have done projects with me over the years,
and to the reviewers listed below:

- [Bram Adams](https://mcis.cs.queensu.ca/bram.html)
- [Rohan Alexander](https://rohanalexander.com/)
- [Tavish Armstrong](http://tavisharmstrong.com/)
- [Titus Barik](https://www.barik.net/)
- [Robert Beghian](http://www.vasken.ca/)
- [Yanina Bellini Saibene](https://yabellini.netlify.app/)
- [Neil Brown](https://twistedsquare.com/)
- [Jordi Cabot](https://jordicabot.com/)
- [Silvia Canelón](https://silvia.rbind.io/)
- Francisco Canas
- [Mike Conley](https://mikeconley.ca/)
- [Michael DiBernardo](https://mikedebo.com/)
- [Isaac Ezer](http://www.isaacezer.com/)
- [Ian Flores Siaca](https://ianfs.dev/)
- [Adam Goucher](https://adam.goucher.ca/)
- [Mustafa Haddara](https://twitter.com/MustafaHaddara/)
- [Johan Harjono](http://johanharjono.com/)
- [Kate Hertweck](https://katehertweck.com/)
- [Daniel Jackson](https://people.csail.mit.edu/dnj/)
- [Jacob Kaplan-Moss](https://jacobian.org/)
- [Ritu Kapur](https://sites.google.com/view/ritu-kapur)
- [Zain Kazmi](https://zainhkazmi.github.io/)
- [Laurie MacDougall Sookraj](https://www.linkedin.com/in/lauriemacdougallsookraj/)
- [Darren McElligott](https://www.linkedin.com/in/darren-mcelligott-07689473/)
- [Kim Moir](https://kimmoir.blog/)
- [Natalia Morandeira](https://nmorandeira.netlify.app/)
- [Meiyappan Nagappan](https://cs.uwaterloo.ca/~m2nagapp/)
- [Iain Parris](https://parris.org/)
- [Elizabeth Patitsas](https://patitsas.github.io/)
- [Andrew Petersen](https://utmandrew.bitbucket.io/)
- [Andrey Petrov](https://shazow.net/)
- [Andrew Potapov](https://www.andrewpotapov.com/)
- [Lutz Prechelt](http://www.mi.fu-berlin.de/w/Main/LutzPrechelt)
- [Yim Register](https://students.washington.edu/yreg/)
- [Evan Schultz](https://evanjustevan.com/)
- [Alex Serebrenik](https://www.win.tue.nl/~aserebre/)
- [Naaz Sibia](https://www.linkedin.com/in/naaz-sibia/)
- [Andreas Stefik](https://web.cs.unlv.edu/stefika/)
- Rory Tulk
- [Blake Winton](https://bwinton.latte.ca/)
- [Andy Zaidman](https://azaidman.github.io/)
- [Andreas Zeller](https://andreas-zeller.info/)

Finally,
I would like to thank
[% i "Elbakyan, Alexander" %]Alexandra Elbakyan[% /i %] for [% i "Sci-Hub" %][Sci-Hub][sci-hub][% /i %]:
this book would have been impossible to write without her idealism and hard work.

*All proceeds from this project will go to support the [Red Door Family Shelter][red-door].*
