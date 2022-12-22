# Topics

-   This is a rough draft:
    topics will change and be presented in a different order.
-   Contrast what the gurus say with what working programmers do
    with what students can aim for in their context

## What problems are we trying to solve?

This list goes into the introduction.

-   How do we decide what to build?
-   How do we decide who does what, in what order, without burning out?
-   How do we avoid doing harm to our teammates, stakeholders, and society?
-   What do we do when goals change or we fall behind?
-   How do we tell we're done?
-   What do we do then?

## What three things are most important?

-   How to run meetings fairly and efficiently
-   Time management
    -   Why crunch mode doesn't work
    -   How to prioritize tasks
    -   Think of yourself as one of your own customers
-   How to report problems, progress, and achievements

## How can we tell which claims are true and which aren't?

Introduce these topics early to (a) motivate the running example
and (b) give readers tools to understand empirical claims.

-   Research methods
-   Data cleaning
-   Summary statistics and data visualization
-   Hypothesis testing
-   Clustering
-   Qualitative analysis and grounded theory
-   How to lie with statistics

## What empirical facts should every software engineer know?

-   The syntax of some programming languages is harder to learn than that of others (Stefik)
-   Static typing helps, but only a little (Hanenberg, others)
-   Most configuration parameters are never used
-   Code metrics are no better than counting lines
-   There is no geek gene

## What's in a minimum viable software project?

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

## What roles are there in a team and why?

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

## How do we know what software to build?

-   Personas
-   User research
-   Requirements gathering
-   Product management

## How do we design software?

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

## How do we test software?

-   Code coverage (and how it can mislead)
-   Fixtures
-   Mocking functions
-   Mocking the file system
-   Testing an interface
-   Fuzzing

## How do we debug software?

-   Minimum reproducible example
-   Using a breakpointing debugger
-   Program slicing
-   Binary search to find regression point

## How do we review software?

-   Code reviews

## How do we handle errors?

-   Exceptions: but what then?

## How do we describe software?

-   How people think and learn (abridged)
-   Tutorials
-   Vignettes/FAQs/Q&A: which is how most people learn
-   Reference guides: auto-generated from code
-   Marketing: both static and presentations

## How does software do harm?

-   Developing threat models
-   Eroding privacy: classroom surveillance and plagiarism detection
-   Algorithmic bias
-   Lack of accessibility
-   Amplifying misinformation and hate

## How do we deploy software?

-   Package creation (for code)
-   Virtualization (for services)
-   Logging and other monitoring
-   For students: the delivery report
-   Retrospectives

## How do we build software together?

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

## What else do we use to build software?

-   Refactoring
-   Profiling
-   Continuous integration

## How do we decide who owns what?

-   What it means to own something intangible (or tangible)
-   Forms of intellectual property
-   Open licenses
-   Student work

## What other rights do you have?

-   Labor rights
-   Non-disclosure and non-disparagement agreements and the enforceability thereof
-   How stock options work

## How do we manage people?

-   Interviewing
-   Onboarding: getting newcomers up to speed
-   Professional development
-   Firing
-   Offboarding

## NWIT

- http://localhost:4000/2011/06/27/organizational-volatility-and-its-effects-on-software.html
- http://localhost:4000/2011/06/30/lets-go-to-the-whiteboard.html
- http://localhost:4000/2011/07/07/the-confounding-effect-of-class-size-on-the-validity-of-object-oriented-metrics.html
- http://localhost:4000/2011/07/26/effects-of-personality-on-pair-programming.html
- http://localhost:4000/2011/08/09/an-empirical-study-of-build-maintenance-effort.html
- http://localhost:4000/2011/08/16/cloning-considered-harmful-considered-harmful.html
- http://localhost:4000/2011/08/24/is-transactional-programming-actually-easier.html
- http://localhost:4000/2011/09/06/does-adding-manpower-also-affect-quality.html
- http://localhost:4000/2011/10/11/the-irop-paper.html
- http://localhost:4000/2011/10/18/the-impact-of-irrelevant-and-misleading-information.html
- http://localhost:4000/2011/10/22/three-results-many-definitions.html
- http://localhost:4000/2012/01/05/the-effects-of-stand-up-and-sit-down-meeting-formats-on-meeting-outcomes.html
- http://localhost:4000/2012/04/26/on-the-naturalness-of-software.html
- http://localhost:4000/2012/05/18/willingness-to-share-research-data-is-related-to-the-strength-of-the-evidence-and-the-quality-of-reporting-of-statistical-results.html
- http://localhost:4000/2012/10/25/an-experiment-about-static-and-dynamic-type-systems.html
- http://localhost:4000/2013/06/13/uml-in-practice-2.html
- http://localhost:4000/2013/07/07/how-and-why-process-metrics-are-better.html
- http://localhost:4000/2014/01/29/stefik-siebert-syntax.html
- http://localhost:4000/2016/04/26/java-exception-handling.html
- http://localhost:4000/2016/06/09/hidden-truths.html
- http://localhost:4000/2016/06/09/novice-programming-mistakes.html
- http://localhost:4000/2016/06/09/too-many-knobs.html
- http://localhost:4000/2016/06/13/polymorphism-in-python.html
- http://localhost:4000/2016/09/30/rethinking-git.html
- http://localhost:4000/2016/10/05/test-driven-development.html
- http://localhost:4000/2021/08/09/impact-of-rapid-release-cycles-on-integration-delay-of-fixed-issues.html
- http://localhost:4000/2021/08/09/task-interruption-in-software-development-projects.html
- http://localhost:4000/2021/08/10/developers-fix-their-own-simple-bugs-differently-from-other-developers.html
- http://localhost:4000/2021/08/11/cheating-death-survival-analysis-of-python-projects.html
- http://localhost:4000/2021/08/12/on-the-nature-of-merge-conflicts.html
- http://localhost:4000/2021/08/16/modern-code-review.html
- http://localhost:4000/2021/08/17/python-language-features.html
- http://localhost:4000/2021/08/18/how-agile-teams-make-self-assignment-work.html
- http://localhost:4000/2021/08/19/toxic-code-snippets-on-stack-overflow.html
- http://localhost:4000/2021/08/23/links-in-source-code-comments.html
- http://localhost:4000/2021/08/28/privacy-threats-in-intimate-relationships.html
- http://localhost:4000/2021/08/29/beyond-the-code-itself.html
- http://localhost:4000/2021/09/02/compiler-error-messages-considered-unhelpful.html
- http://localhost:4000/2021/09/03/two-papers-about-the-blackbox-project.html
- http://localhost:4000/2021/09/05/two-papers-on-errors.html
- http://localhost:4000/2021/09/06/commenting-source-code.html
- http://localhost:4000/2021/09/07/characterizing-software-engineering-work-with-personas.html
- http://localhost:4000/2021/09/08/to-type-or-not-to-type.html
- http://localhost:4000/2021/09/11/common-bug-fix-patterns.html
- http://localhost:4000/2021/09/13/whats-wrong-with-tech-hiring.html
- http://localhost:4000/2021/09/16/analyzing-the-effects-of-tdd-in-github.html
- http://localhost:4000/2021/09/16/exception-handling-practices-and-post-release-defects.html
- http://localhost:4000/2021/09/18/code-of-conduct-in-open-source-projects.html
- http://localhost:4000/2021/09/19/impact-of-task-switching-and-work-interruptions.html
- http://localhost:4000/2021/09/20/do-developers-read-compiler-error-messages.html
- http://localhost:4000/2021/09/22/taxonomy-of-package-management.html
- http://localhost:4000/2021/09/23/the-secret-life-of-bugs.html
- http://localhost:4000/2021/09/24/coverage-is-not-strongly-correlated-with-test-suite-effectiveness.html
- http://localhost:4000/2021/09/24/how-software-designers-interact-with-sketches-at-the-whiteboard.html
- http://localhost:4000/2021/09/26/are-delayed-issues-harder-to-resolve.html
- http://localhost:4000/2021/09/27/technology-facilitated-intimate-partner-abuse.html
- http://localhost:4000/2021/09/27/the-evolution-of-javascript-code-in-the-wild.html
- http://localhost:4000/2021/10/01/python-coding-style-compliance-on-stack-overflow.html
- http://localhost:4000/2021/10/01/the-relevance-of-classic-fuzz-testing.html
- http://localhost:4000/2021/10/03/how-gamification-affects-software-developers.html
- http://localhost:4000/2021/10/03/is-40-the-new-60.html
- http://localhost:4000/2021/10/05/three-papers-on-readability.html
- http://localhost:4000/2021/10/07/finding-bugs-in-database-systems-via-query-partitioning.html
- http://localhost:4000/2021/10/08/do-hackathon-projects-change-the-world.html
- http://localhost:4000/2021/10/21/the-impact-of-sleep-deprivation.html
- http://localhost:4000/2022/03/02/ethics-in-decision-making.html
- http://localhost:4000/2022/03/08/obsolete-answers-on-stack-overflow.html
- http://localhost:4000/2022/03/11/single-statement-bugs-in-python-projects.html
- http://localhost:4000/2022/03/16/resume-driven-development.html
- http://localhost:4000/2022/03/18/python-3-types-in-the-wild.html
- http://localhost:4000/2022/03/28/remote-onboarding.html
- http://localhost:4000/2022/04/08/continuous-integration-single-statement-bugs.html
- http://localhost:4000/2022/04/20/open-source-exception-handling-testing.html


- https://techworkerhandbook.org/

If your site is supposed to be about *evidence-based* software engineering [emphasis in original], shouldn't you restrict it to quantititative [sic] analysis of controlled experiments?" The answer to both parts is "no": qualitative analysis can be just as rigorous (or not) as quantitative, and if we only counted controlled lab experiments as science, we would have to exclude much of geology and astronomy.