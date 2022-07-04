# Software Engineering: A Compassionate, Evidence-Based Approach

This book is designed for a first course in software engineering.
Some parts explain when, why, and how to use tools like version control and testing frameworks
when working in teams;
others summarize empirical research on programs, programmers, and programming,
while the remainder introduce essential working practices like running productive meetings,
deciding who is responsible for what,
and cutting features when time runs short.

*SECEBA* differs from other introductions to software engineering in three ways:

1.  It teaches you how to be *compassionate programmers*:
    ones who care as much about the well-being of their colleagues and users
    as they do about their own.
    This focus is not entirely altruistic—everything we do to help others
    also helps our future selves—but given how much harm software can do,
    we need to learn how to make it better.

2.  It discusses the differences between what developers believe they ought to do,
    what they actually do in practice,
    and what students can reasonably expect to do
    when they are juggling several courses at once.

3.  Its recommendations are based on empirical studies wherever possible.
    To help you understand and evaluate those studies,
    *SECEBA* uses data science problems for its examples.

All of this material can be re-used and remixed under open licenses.
Fixes and additions are very welcome:
please see our contributors' guide for details,
and please note that all contributors must abide by our Code of Conduct.

## Topics

-   This is a rough draft:
    topics will change and be presented in a different order.
-   Contrast what the gurus say with what working programmers do
    with what students can aim for in their context

### What problems are we trying to solve?

This list goes into the introduction.

-   How do we decide what to build?
-   How do we decide who does what, in what order, without burning out?
-   How do we avoid doing harm to our teammates, stakeholders, and society?
-   What do we do when goals change or we fall behind?
-   How do we tell we're done?
-   What do we do then?

### What three things are most important?

-   How to run meetings fairly and efficiently
-   Time management
    -   Why crunch mode doesn't work
    -   How to prioritize tasks
    -   Think of yourself as one of your own customers
-   How to report problems, progress, and achievements

### How can we tell which claims are true and which aren't?

Introduce these topics early to (a) motivate the running example
and (b) give readers tools to understand empirical claims.

-   Research methods
-   Data cleaning
-   Summary statistics and data visualization
-   Hypothesis testing
-   Clustering
-   Qualitative analysis and grounded theory
-   How to lie with statistics

### What empirical facts should every software engineer know?

-   The syntax of some programming languages is harder to learn than that of others (Stefik)
-   Static typing helps, but only a little (Hanenberg, others)
-   Most configuration parameters are never used
-   Code metrics are no better than counting lines
-   There is no geek gene

### What's in a minimum viable software project?

We assume some previous experience with version control, unit testing, and documentation;
we illustrate these ideas by building a data analysis project.

-   Version control
-   Unit testing and integration testing
-   Task automation
-   Style checking
-   Package management
-   Developer documentation (including checklists for tasks that can't be automated)
-   Governance documentation
-   Other onboarding and offboarding material

### What roles are there in a team and why?

Typical:

| Department | Also Called | What It Does |
| ---------- | ----------- | ------------ |
| Marketing | Awareness | Making people aware of who we're trying to help and how |
| Sales | Adoption | Getting people from "this looks interesting" to "we're using it" |
| Support | Success | Removing roadblocks and providing help |
| Human Resources | Community | Peer support and gathering feedback |
| Product Management | — | Translate user pain into feature lists |
| Project Management | — | Who should be working on what right now and what's stopping them |

Another way of looking at it:

| Department | What Risk It Addresses |
| ---------- | ---------------------- |
| Marketing | People don't know we exist or how we ca help |
| Sales | It's too hard to start using what we build |
| Support | It's too hard to *keep* using what we build |
| Human Resources | We don't have the right people to do the work |
| Product Management | We're building the wrong thing |
| Project Management | People aren't working on the right things or aren't working well together |

### How do we know what software to build?

-   Personas
-   User research
-   Requirements gathering
-   Product management

### How do we design software?

-   Design after the fact
-   Design for people's cognitive capacity
-   Design in coherent levels
-   Design for evolution
-   Group related information together
-   Use common patterns
-   Design for delivery
-   Design for testability
-   Design as if code was data
-   Design graphically
-   Design with everyone in mind
-   Design for contribution

### How do we test software?

-   Code coverage (and how it can mislead)
-   Fixtures
-   Mocking functions
-   Mocking the file system
-   Testing an interface
-   Fuzzing

### How do we debug software?

-   Minimum reproducible example
-   Using a breakpointing debugger
-   Program slicing
-   Binary search to find regression point

### How do we review software?

-   Code reviews

### How do we handle errors?

-   Exceptions: but what then?

### How do we describe software?

-   How people think and learn (abridged)
-   Tutorials
-   Vignettes/FAQs/Q&A: which is how most people learn
-   Reference guides: auto-generated from code
-   Marketing: both static and presentations

### How does software do harm?

-   Developing threat models
-   Eroding privacy: classroom surveillance and plagiarism detection
-   Algorithmic bias
-   Lack of accessibility
-   Amplifying misinformation and hate

### How do we deploy software?

-   Package creation (for code)
-   Virtualization (for services)
-   Logging and other monitoring
-   For students: the delivery report
-   Retrospectives

### How do we build software together?

-   Agile vs. sturdy
    -   In terms of feedback loops
    -   They're usually the same thing in practice
    -   But students usually can't do either
-   Forming teams
-   How to write a good bug report or feature request
-   Tracking and planning work with an issue tracker
-   Labeling
-   Discussion: email, slack
-   Archiving information: discoverability and maintenance (labeling again)
-   Code comments as communication
-   Status reporting
-   Conflict resolution
-   Safeguards against systemic bias (and the problem of Goodhart's Law)

### What else do we use to build software?

-   Refactoring
-   Profiling
-   Continuous integration

### How do we decide who owns what?

-   What it means to own something intangible (or tangible)
-   Forms of intellectual property
-   Open licenses
-   Student work

### What other rights do you have?

-   Labor rights
-   Non-disclosure and non-disparagement agreements and the enforceability thereof
-   How stock options work

### How do we manage people?

-   Interviewing
-   Onboarding: getting newcomers up to speed
-   Professional development
-   Firing
-   Offboarding
