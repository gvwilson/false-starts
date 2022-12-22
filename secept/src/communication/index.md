---
title: "Communication"
syllabus:
- Use an issue tracker as a shared to-do list for a project.
- Label issues to help search and triage.
- Include a short reproducible example in every bug report.
- Document the public interface of code.
- Embed documentation in code and use a documentation generator to format it.
- Create different documentation for novices, competent practitioners, and experts.
- Create a blog to summarize and discuss progress.
- Create FAQ entries by recycling users' questions.
---

Knowing how to steer isn't enough to drive a car:
you need to know how to signal when you're turning or changing lanes.
Similarly,
knowing how to program isn't enough to build software:
you must coordinate with your teammates.

## To Do {: #communication-todo}

You probably have a to-do list somewhere.
It might be in a notebook,
on your phone,
or in your head,
but however you maintain it,
it lists the things you're supposed to do,
when they're due,
and how urgent they are.

An [%i "issue tracker" "issue" %][%g issue_tracker "issue tracker" %][%/i%]
is a structured, shared to-do list.
(They are also called [%i "bug tracker" %]bug trackers[%/i%]
because programmers originally used them
to keep track of bugs they needed to fixed.)
While a team uses version control to record and share the project's history,
it should use an issue tracker to record and share the project's future.
Without it,
you and your teammates will constantly have to ask each other
"What are you working on?",
"What am I supposed to be working on?",
and "Who was supposed to do that?"

To create a new issue,
you enter a title and a short description;
the system then assigns it a unique serial number.
You can usually also specify:

-   what kind of issue it is,
    such as a bug report,
    a request for a new feature,
    or a question to be answered;

-   who is responsible for it
    (i.e., who's supposed to fix the bug);

-   how important it is; and

-   when it's due.

An issue tracker is only as useful as what you put into it.
Empirical studies find that if you are describing a bug,
the most important thing is to provide enough information for someone to reproduce the problem
[%b Zimmermann2010 Soltani2020 %].
This may include:

-   what version of the software you were using;

-   what platform it was running on;

-   what you did to make it crash;

-   any data or configuration files the program relies on; and

-   whatever stack traces, error reports, or log messages the program produced.

Here's a bug report for a tool that reads and merges spreadsheets:

[%excerpt f="bug-report.txt" %]

The ID on the first line is assigned by the issue tracker
and often serves as a shorthand name for the issue in conversation.
("Hey, is anyone working on number fifty-five yet?")
The timestamp is in [%i "issue!timestamps" %][%g utc "UTC" %][%/i%]
because teams are increasingly scattered across several time zones.

The [%i "issue!good titles" %]title[%/i%] is the most important part of the issue.
Projects can accumulate hundreds or thousands of issues over time;
a good subject line makes them easier to browse and search.
The `labels` improve [%i "discoverability!of issues" %][%g discoverability "discoverability" %][%/i%],
but are more important for triage (discussed below).

Finally,
the [%i "issue!description of" %]description[%/i%] briefly summarizes the problem.
A good description includes a short
[%i "reproducible example (reprex)" %][%g reprex "reproducible example" %][%/i%] (or "reprex")
that explains how to reproduce the problem in the simplest way.
A reprex helps the reader understand the issue much better than,
"The program crashes when I open strange files."
Experience also shows that if people are required to come up with a reprex when filing an issue,
they will often solve their own problem along the way.

### Labeling and Triage

Using an issue tracker makes it much easier to summarize the project's status:
just look at issues that have been opened or changed since the last meeting.
You can use this to create the agenda for status meetings ([%x teamwork %])
and to remind yourself what you were doing three months ago
when you need to create a final report.

<div class="callout" markdown="1">

### Summarizing Makes You Think

Some teams use the issue tracker directly as the agenda for their status meetings.
However,
going through the issues and summarizing them once a week
is a good opportunity to do triage
and often reminds team members of things that *aren't* in the issue tracker.

</div>

The bigger a project gets, the harder it is to find things.
Most issue trackers therefore let people add [%i "issue!labels" %][%g issue_label "labels" %][%/i%] to issues
so that they will be easier to search and organize.

You can define whatever labels you want for issues.
A small project should always have:

Bug
:   Something should work but doesn't.

Change
:   Something should be added or modified.

Task
:   something needs to be done but won't show up in code
    (e.g., organizing the next team meeting).

<div class="callout" markdown="1">

### Issues versus pull requests

Some teams use the same labels for issues and pull requests,
but this leads to confusion:
does `Bug` mean a bug report or a bug fix?
Separate labels makes this clearer:
for example,
a project could use `Fix` to label pull requests that fix bugs
and `Enhancement` for ones that add new features.

</div>

Almost every project adds more labels to this basic set,
including things like:

Question
:   where is something or how is something supposed to work?
    Teams often turn these issues and their answers into [%i "FAQ" %]FAQ[%/i%] entries
    (discussed below).

Proposal
:   something the team needs to discuss and make a decision about
    ([%x teamwork %]).

Urgent
:   Work needs to be done right away.
    (This label is typically reserved for security fixes).

Current
:   This issue is included in the current round of work.

Backlog
:   Someone has looked at the issue and believes it needs to be tackled,
    but there's no immediate plan to do it.

Won't Fix
:   Someone has decided that the issue isn't going to be addressed,
    either because it's out of scope or because it's not actually a bug.
    An issue marked this way is usually then closed.

Duplicate
:   This issue is a duplicate of one that's already in the system.
    Issues marked this way are usually also then closed.

<div class="callout" markdown="1">

### Milestones

Some projects use labels for upcoming assignments or releases
instead of labeling states like `Current` and `Backlog`.
This approach works in the short term,
but becomes unwieldy the number of assignments or releases grows.
Instead,
a team can create a [%i "milestone (in issue tracker)" "issue tracker!milestones" %][%g milestone "milestone" %][%/i%]
to group a set of issues together.
Milestones can have a due date and show progress toward completion
so that the team can easily see how much work is left.

</div>

## Other Channels {: #communication-channels}

Issues are the best way to keep track of where you are,
but teams can and should communicate in other ways.
These channels can be fully [%i "communication!synchronous" %]synchronous[%/i%] like video calls,
fully [%i "communication!asynchronous" %]asynchronous[%/i%] like email,
or somewhere in between like chat.
Synchronous channels are better for quick back-and-forth and for maintaining social connections,
but they bias communication in favor of people who are more self-confident,
more fluent in the language of discussion,
or have better network connections.
Additionally,
finding things afterward is hard or impossible.

If you prefer fewer interruptions and more time to think
you should use [%i "communication!email" "email (for team communication)" %]email[%/i%].
It allows everyone to deal with issues when it's convenient for them
while supporting long-running conversations and findability.
Projects should always use mailing lists rather than person-to-person messages
so that people don't have to remember to CC the rest of the team
and to create a shared archive to search later.
The second point is as important as the first:
if you can't go back and find out what was said a month ago—or
if someone *else* can't do that—you might as well not have said it.

<div class="callout" markdown="1">

### Filters are your friend

Every email client allows you to set up [%i "email!filters" %][%g "mail_filter" "filters" %][%/i%]
that automatically move messages into specific folders.
I have fourteen of these set up right now
to organize messages belonging to particular projects;
it only took a couple of minutes to set up,
and it means I can focus on one problem at a time when checking mail.

</div>

Most teams now use semi-synchronous [%i "communication!chat" "chat!inevitable use of" %]chat[%/i%]
like [Slack][slack] more than either video calls or email.
Chat combines the conversationality of a video call
with the ability to ignore messages without missing them
(and to edit a reply before sending it).
It also enables people to manage multiple parallel conversations like mail threads.
However,
chat is a more interruptive medium than email,
which means team members are less able to focus ([%x teamwork %]).
It also feels harder to find things in old chat conversations than in email archives,
in part because chat channels proliferate more rapidly than mailing lists.

Many teams now have bots send notifications when builds fail,
software is deployed,
or security vulnerabilities are detected.
These messages help maintain [%i "peripheral awareness" %][%g peripheral_awareness "peripheral awareness" %][%/i%],
but if they are frequent or usually don't require action,
team members quickly learn to ignore them.
We will discuss this more in [%x devops %].

However the team communicates,
it should have guidelines to ensure that
the conversation isn't dominated by its most self-confident members.
The tricks in [%x teamwork %] for ensuring that meetings are fair
apply here as well.
For example,
on one project I was involved in,
team members in the americas would sometimes wake up to find a thread
with fifty or sixty messages among two or three people in Europe.
This was so overwhelming that they would simply not try to catch up.
Once we brought in a rule saying,
"One message per person per thread per day,"
many more people began contributing,
and everyone's contributions became more thoughtful.

<div class="callout" markdown="1">

### How Did He Know?

In his 1961 story "[Harrison Bergeron][harrison_bergeron]",
[%i "Vonnegut, Kurt" %]Kurt Vonnegut[%/i%]
described a future in which everyone is forced to be equal.
Good-looking people have to wear masks,
athletic people have to wear weights,
and intelligent people
are forced to carry around radios that interrupt their thoughts at random intervals.

Slack and other instant messaging tools are our radios.

</div>

### Other Channels

[%i "software portal" %][%g software_portal "Software portals" %][%/i%]
like [Bitbucket][bitbucket], [GitHub][github], and [GitLab][gitlab]
provide many other ways to communicate,
which project members use in a wide variety of ways [%b Treude2011 %].
[%i "wiki" "communication!wiki" %]Wikis[%/i%] seem like a good way to keep notes,
create documentation,
and so on,
but if team members already know how to use version control,
they will get more mileage out of [%i "Markdown" %]Markdown[%/i%] pages:
they can use commits to synchronize changes to documentation with changes to code
and pull requests provide an opportunity for review.

[%i "communication!blog" "blog!as team journal" %]Blogs[%/i%],
on the other hand,
are very useful.
Team members can blog regularly about their progress;
such a journal is useful for people watching the project from the outside,
like instructors,
but also serves as a live draft of a project's final report.

If you are going to create a blog,
use a [%i "static site generator" %][%g static_site_generator "static site generator" %][%/i%]
to format and publish content consistently.
[%i "GitHub Pages" %][GitHub Pages][github_pages][%/i%] uses
a Ruby-based tool called [%i "Jekyll" "static site generator!Jekyll" %][Jekyll][jekyll][%/i%],
but [every language provides alternatives][ssg_list].

## Documentation {: #communication-documentation}

An old proverb says, "Trust, but verify."
The equivalent in programming is,
"Write clear code, but [%i "documentation!as communication" %]document[%/i%]."
No matter how well software is written,
it always embodies decisions that aren't explicit
or accommodates complications that won't be obvious to the next reader.
Putting it another way,
the best function names in the world aren't going to answer the question,
"Why does the software do this?"

We can divide people in any domain into novices, competent practitioners, and experts
[%b Wilson2019 %].
Each group needs a different kind of documentation:

-   A [%i "novice!documentation needs" "documentation!for novices" %]novice[%/i%]
    needs a tutorial that introduces key ideas one by one
    and shows how they fit together.

-   A [%i "competent practitioner!documentation needs" "documentation!for competent practitioners" %]competent practitioner[%/i%]
    needs reference guides, cookbooks, and Q&A sites
    with solutions close enough to what she needs
    that she can tweak them the rest of the way.

-   [%i "expert!documentation needs" "documentation!for experts" %]Experts[%/i%]
    need guides as well—nobody's memory is perfect—but they also want
    discussions of alternatives and tradeoffs.

No documentation can serve all three groups equally well.
Tutorials help novices build a [%i "mental model" %][%g mental_model "mental model" %][%/i%],
but competent practitioners will be frustrated
by their slow pace and low information density.
They want single-point solutions to specific problems,
and are able to search for what they need.

### Creating an FAQ

A good [%i "FAQ" %]FAQ[%/i%] uses the terms and concepts that people bring to the software
rather than the vocabulary of its authors.
The questions are things people actually search for online,
not things the program's developers wish they would ask.

Creating and maintaining an FAQ is a lot of work.
A lot of that effort may be wasted
because it's hard for the authors or maintainers of a piece of software
to anticipate what newcomers will be mystified by.
A better approach is the "answer on demand" approach of [%i "Stack Overflow" %][Stack Overflow][stack_overflow][%/i%].
Its guide to [asking a good question][stack_overflow_good_question] is:

Write the most specific title you can.
:   "Why does division sometimes give a different result in Python 2.7 and Python 3.5?"
    is much better than, "Help! Math in Python!!"

Give context before giving sample code.
:   A few sentences to explain what you are trying to do and why
    helps people determine if their question matches the one in the article.

Provide a minimal reprex.
:   Readers will have a much easier time figuring out
    if this article matches their question
    if they can see a few lines of code.

Tag, tag, tag.
:   Keywords make everything easier to find.
    They are even more effective if the system encourages people to re-use tags
    so that they don't proliferate [%b Lin2020 %].

Use "I" and question words (how/what/when/where/why).
:   Writing this way forces people to think more clearly
    about what they're actually asking.

Keep each answers short.
:   Break every answer down into single steps
    and devote half of each answer to troubleshooting.
    Doing this may feel trivializing if you already know the answer,
    but is often as much as a person searching and reading can handle.
    It also helps writers realize just how much implicit knowledge they are assuming.

Allow for a chorus of explanations.
:   Do not be afraid of providing multiple explanations to a single question
    that suggest different approaches
    or are written for different prior levels of understanding.
    This is one of the things that has made Stack Overflow so successful:
    different users are best served by a [%i "chorus of explanation" %]chorus of explanations[%/i%]
    [%b Caulfield2016 %].

### Documenting Code

Every language has [%g doc_generator "documentation generators" %]
that extract information from  [%g docstring "docstring" %] or [%g doc_comment "doc comments" %]
and produces cross-indexed HTML pages.
Programmers believe they are more likely to update
[%i "documentation!embedded" %]embedded documentation[%/i%] like this
because it is right there with the code
instead of in a separate file.

Each piece of embedded documentation should begin with an active verb
like "extract" or "normalize"
and describe either how inputs are turned into outputs
or what side effects the function has.
Some examples of good one-line docstrings are:

-   "Create a list of capital cities from a list of countries."
-   "Clip signals to lie in [0...1]."
-   "Reduce the red component of each pixel."

Once you start writing code for other people
your [%i "documentation!what to include" %]documentation[%/i%] should include:

-   The name and purpose of every public class, function, and constant.

-   The name, purpose, and default value (if any) of every parameter.

-   Any side effects the functions and methods have.

-   What value every function or method returns.

-   What exceptions those functions can raise and when.

The word "public" in the first rule is important.
You don't have to write full documentation for helper functions
that are only used inside your package,
but these should still have at least a one-liner explaining their purpose.

### Comments as Communication

People don't usually think of [%i "comments!as communication" "communication!comments" %]code comments[%/i%]
as a form of communication like email or chat,
but the only significant difference is that
the comments are right there in the code where the recipients can't miss them
rather than in an archive somewhere that they'll have to go and search.
If you choose names for functions and variables carefully,
the code itself will explain *what* it's doing when someone reads it aloud.
The comments should therefore explain *why*.
For example, this is not a useful comment:

```py
x = x[1:] # take all but first element of list
```

This, on the other hand, tells the next person why we're doing it:
{: .continue}

```py
threads = threads[1:] # First thread is already running so save the others.
```

## Code Reviews {: #communication-reviews}

People usually don't think of [%g code_review "code reviews" %] as a kind of communication either,
but they are one of the most effective ways to share knowledge within a team.
There's no point creating PRs if they are all merged as-is.
One study after another since the mid-1970s has proven that
code review is the most cost-effective way to find bugs in software [%b Cohen2010 %].

<div class="callout" markdown="1">

### Do more eyes make for fewer bugs?

Some people have claimed that many eyes make all bugs shallow
(i.e., easy to find)
but the evidence doesn't support that claim.
For example,
[%b Meneely2014 %] found that,
"…source code files reviewed by more developers are,
counter-intuitively,
more likely to be vulnerable (even after accounting for file size).
However,
files are less likely to be vulnerable
if they were reviewed by developers
who had experience participating on prior vulnerability-fixing reviews."
In short, *whose* eyes matters more than how many.

</div>

There are many guides online for doing code reviews,
most of them based on individual experience.
A notable exception is the [SmartBear guide][smartbear_code_review],
which draws on a large study of code review in industry.
The [%i "code review!procedure" %]rules below[%/i%] present some of their findings
with modifications for students' situations.

Have the instructor do a demonstration review.
:   Even if you have done code reviews before,
    you may not know what's expected for this course.
    The instructor can show you by putting up some sample code and going through it,
    thinking aloud as they notice things worth commenting on
    so that you have an idea of how much detail they expected.

Authors should clean up code before review.
:   If the person creating the PR goes through and adds some more comments,
    cleans up some variable names,
    and does a bit of [%i "refactoring!for code review" %]refactoring[%/i%],
    they won't just make reviewing easier:
    the odds are very good that they will find and fix a few problems on their own.

Review at most 200 lines of a code at a time.
:   The SmartBear guide recommends reviewing at most 400 lines at a time,
    which should take 60–90 minutes.
    You will probably get there eventually,
    but in our experience it's better to start with something smaller
    and work up to that.
    A corollary of this rule is that no PR should be more than 200 lines long.
    If one is,
    the odds are that reviewers won't be able to hold it all in their head at once and so will miss things.

Use checklists.
:   [%b Gawande2011 %] popularized the idea that
    using [%i "checklists!use in code review" %]checklists[%/i%]
    improves results even for experts.
    While [%b Hatton2008 %] found no evidence that they made a difference to code reviews by professionals,
    I have found them very useful as a starter for students.
    If you are new to code reviews,
    ask the instructor for a list of the dozen most common problems to check for;
    anything more than that is likely to be overwhelming.
    (The code quality rubric developed in [%b Stegeman2014 Stegeman2016 %] is a good starting point.)
    If you and your teammates have been working together for a while,
    look at your own code reviews and make a list of the things that keep coming up.
    Having the list will make you more aware of the issues while you're coding,
    which in turn will make you less likely to keep making the same mistakes.

Look for algorithmic problems first.
:   Code review isn't primarily about style:
    your linter should catch those problems.
    Code review's real purpose is to find bugs before they can affect anyone.
    The first pass over any change should therefore look for algorithmic problems.
    Are the calculations right?
    Are any rare cases going to be missed?
    Are errors being caught and handled?

Offer alternatives.
:   Telling authors that something is wrong is helpful;
    telling them what they might do instead is more so.

Don't [%g feigning_surprise "feign surprise" %] or pass judgment.
:   "Gosh, didn't you know [some obscure fact]?" isn't helpful;
    neither is,
    "Bloody hell, why don't you just [some clever trick] here?"

Don't overwhelm people with details.
:   If someone has used the letter `x` as a variable name in several places,
    and they shouldn't have,
    comment on the first two or three and
    put a check beside the others—the reader won't need the comment repeated.

Don't try to sneak in feature requests.
:   Nobody enjoys fixing bugs.
    Asking them to add entirely new functionality while they're at it is rude.

Follow up.
:   The author of the code doesn't have to accept every suggestion,
    but should have a better reason than "I don't want to" for rejecting any of them.
    GitHub and other platforms allow people to create discussion threads for each comment,
    and will mark threads as being out of date when the pull request is updated.
    Whoever did the review should then scan the changes to make sure their points have been addressed,
    and to give themselves a chance to learn a few more things from the author.

Don't tolerate rudeness.
:   Most code review guidelines say, "Be respectful."
    The problem is that if you are,
    you probably don't need to be told that,
    and if you aren't,
    those two works alone won't change your behavior.
    What *will* is teammates defending the victims of rudeness by telling the offender,
    "That's not how we speak to each other."

How we [%i "code review!responding to" %]respond[%/i%] to reviews
is just as important:

Be specific in replies to reviewers.
:   If someone has suggested a better variable name you can simply fix it.
    If someone has suggested a major overhaul to an algorithm
    you should reply to their comment to point at the commit that includes the fix.

Thank your reviewers.
:   If someone has taken the time to read your code carefully, thank them for doing it.

So what does a code review actually look like?
Here's a Python program that searches for duplicated files
with comments added to show review.

[%excerpt f="dup.py" %]

## Reporting {: #communication-reporting}

As well as reporting progress to your teammates,
you may have to [%i "reporting!to your manager" %]report[%/i%] it regularly
to your instructor or manager.
[%i "Evans, Julia" %][Julia Evans][evans_julia][%/i%] described
[eight things your manager might not know][evans_manager], all of which apply to student teams:

1.  What's slowing the team down.

1.  Exactly what individual people on the team are working on.

1.  Where the [%i "technical debt" %][%g technical_debt "technical debt" %][%/i%] is.

1.  How to help you get better at your job.

1.  What your goals are.

1.  What issues they should be escalating.

1.  What extra work you're doing.

1.  How compensation/promotions work at the company. (For students, this one translates to, "How grading works.")

[%i "Kaplan-Moss, Jacob" %][Jacob Kaplan-Moss][kaplan_moss_jacob][%/i%]
has a similar guide to [giving a status update to executives][kaplan_moss_executives],
and [Ask a Manager][ask_a_manager] is full of good advice and discussion as well.
These guidelines produce briefs like this:

> Project X is running smoothly.
> We're making steady progress: we've delivered a bit over half of the features on our roadmap,
> and we're on track to launch publicly in May.
>
> I want to particularly highlight J's design work.
> Every time we share a new demo with our users
> they rave over the design.
>
> We do have some cost risk:
> right now the code is pretty inefficient
> and would require us to increase our AWS spend by 25% in production.
> We either need to decide that cost is acceptable
> or add some extra time to the schedule for performance optimization.
> Please let us know which you prefer.

If you learn how to summarize your status like this,
you will be a very popular team member.

## Exercises {: #communication-exercises}

FIXME
