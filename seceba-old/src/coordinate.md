---
title: "Coordination"
lede: "Because you're probably not doing this alone"
template: page
---

The worst mistakes people make are related to people, not software,
so we need to talk about meetings,
making decisions,
and keeping track of what needs to be done
and who's going to do it.

<blockquote markdown="1">
### Not Writing Software Takes Less Time

[% b Sedano2017 %] found that software development projects have
nine types of waste:
building the wrong feature or product,
mismanaging the backlog,
rework,
unnecessarily complex solutions,
extraneous cognitive load ([% x thinking %]),
psychological distress,
waiting and multitasking,
knowledge loss,
and ineffective communication.
*None of these are software issues,*
so if you only think about the code in your project and not about the people writing it,
everything will take longer and hurt more than it needs to.
</blockquote>

## Meetings

The most important team skill is running meetings efficiently,
and the key to doing that is to distinguish between:

-   Status meetings,
    often called [% g stand_up_meeting "standup meetings" %],
    for keeping everyone up to date on what everyone else is doing
    and for making simple decisions when the options are well understood.

-   [% g discussion_meeting "Discussion meetings" %]
    for weighing alternatives and making complex decisions.

-   Co-working sessions like brainstorming sessions and programming sprints
    that are devoted to the content of the project rather than its operation.

Every team should have a short weekly status meeting.
For each meeting,
create a table in a shared document like the one in [% t important-status %].
Everyone adds a few bullet points to their row in the table
at least half an hour before the meeting starts
so that the whole team can mull everything over.
If anyone wants to discuss something,
they highlight it by adding a comment.
The meeting moderator then goes through the highlighted items one by one,
spending no more than a couple of minutes on each;
anything that requires more time is deferred to a discussion meeting

<div class="table" id="important-status" caption="Status Update Table" markdown="1">
| Person | Progress | Plans | Problems |
| ------ | -------- | ----- | ---------- |
| Ren    | Parsing OCTL records | Tag OCTL records in DVC | Duplicate OCTL tags? |
|        | Deployed progress bar patch | Help onboard Silvia | |
| Mikka  | Refactored PostgreSQL connector | #156: handle records with NULL timestamp | Clarify authorship guidelines |
|        | Patched database tests | #171: auto-archive duplicate records | |
| Sanjay | … | … | … |
| Jess   | … | … | … |
</div>

<blockquote markdown="1">
### Are you a blowfish or a clam?

[NOAA's guide][noaa-disruptive] to dealing with disruptive behaviors
has useful labels and even more useful advice
for handling people who may send meetings off course.
</blockquote>

Decision meetings are for issues that will have more long-term impact on the project
or that team members disagree about.
Since the stakes are higher,
they need more structure:

Decide if there actually needs to be a meeting.
:   If the only purpose is to share information,
    send a brief email instead:
    most people can read faster than they can speak.

Write an agenda.
:   If nobody cares enough about the meeting to prepare
    a point-form list of what's to be discussed,
    the meeting probably doesn't need to happen.
    (Note that "the agenda is all the open issues in our GitHub repo" doesn't count.)

Include timings in the agenda.
:   Doing this helps prevent early items stealing time from later ones.
    The first estimates with any new group are inevitably optimistic,
    so expect to revise them upward for subsequent meetings.
    But don't have second or third
    meeting just because the first one ran over time: instead, try to figure out
    *why* it ran over and fix the underlying problem.

Select a moderator.
:   Put one person in charge of keeping items on time,
    selecting the next person to speak,
    chiding people who are having side conversations or checking email,
    and asking people who are talking too much to get to the point.
    The moderator should *not* do all the talking:
    in fact,
    the moderator will talk less in a well-run meeting than most other participants.

Prioritize.
:   Tackle the most important issues first, even if they're the longest,
    because the little ones always take more time than you expect.

Require politeness.
:   No one gets to be rude,
    no one gets to ramble,
    and if someone goes off topic,
    it's the moderator's job to say, "Let's discuss that elsewhere."

No interruptions.
:   This rule is a special case of the one above,
    since treating other people with respect is the sincerest form of politeness.
    Participants should raise a hand (physically or electronically)
    when they want to speak.
    The moderator should keep track of the queue
    and give each person time in turn.

No distractions.
:   Side conversations make meetings less efficient
    because nobody can actually pay attention to two things at once.
    More importantly,
    if someone is checking their email or texting a friend during a meeting,
    it's a clear signal that they don't think the speaker or their work is important.
    This doesn't mean a complete ban on technology—people may need accessibility aids
    or be waiting for a call about childcare—but by default
    phones should be face down and laptops should be closed
    during in-person meetings.

Take minutes.
:   As discussed below,
    someone other than the moderator should take
    point-form notes
    about the most important information that was shared
    and about every decision that was made or every task that was assigned to someone.

End early.
:   If the meeting is scheduled for 10:00--11:00,
    aim to end at 10:50 to give people a break before whatever they're doing next.

As soon as the meeting is over,
add the minutes to the project's wiki,
version control repository,
or shared cloud drive.
Please don't email minutes to everyone:
our inboxes are full enough,
and the more places new team members need to search in order to find things,
the more likely they are to miss something important.

Sharing the minutes ensures that:

People who weren't at the meeting can follow what's going on.
:   We all have to juggle tasks from several projects or courses,
    which means that sometimes we can't make it to meetings.
    Checking a shared record is more accurate and more efficient than asking a colleague,
    "What did I miss?"

Everyone can check what was actually said or promised.
:   Accidentally or not, people often remember things differently;
    writing them down gives everyone a chance to correct mistakes
    and misinterpretations.

People can be held accountable.
:   Whoever has to draw up the agenda for the next meeting
    can start with the action items from the previous one.

If you would like to become better at sharing information and making decisions,
there is no better place to start than [% b Brookfield2016 %],
which catalogs fifty different techniques for managing discussions
and explains when and how each is useful.

## Air Time

One problem with meetings is that
some people may talk far more than others.
Other people may be so accustomed to this
that they don't speak up even when they have valuable points to make.

You can combat this
by giving everyone three sticky notes
(or coins, or paperclips—anything inedible will do) at the start of the meeting.
Every time someone speaks,
they have to give up one sticky note.
When they're out of stickies,
they aren't allowed to speak until everyone has used at least one,
at which point everyone gets all of their sticky notes back.
This ensures that nobody talks more than three times as often as
the quietest person in the room,
which completely changes group dynamics.
People who have given up trying to be heard suddenly have space to contribute,
and the overly-frequent speakers realize how talkative they have been.

Another useful technique is called
interruption bingo.
Draw a grid and label the rows and columns with the participants' names;
each time person A interrupts person B,
add a tally mark to the appropriate cell.
Look at the results Halfway through the meeting:
in most cases it will be clear that one or two people are doing all of the interrupting,
and that they're always interrupting the same people.
After that,
saying, "All right, I'm adding another tally to the bingo card,"
is usually enough to get them to throttle back.
If it isn't,
well,
you just learned something about your teammate…

Online meetings provide special challenges for regulating how often individuals speak.
[% b Troy2018 %] discusses why online meetings
are often frustrating,
and points out that in most online meetings,
the first person to speak during a pause gets the floor.
As a result,
"If you have something you want to say,
you have to stop listening to the person currently speaking
and instead focus on when they're gonna pause or finish
so you can leap into that nanosecond of silence
and be the first to utter something.
The format…encourages participants who want to contribute to say more and listen less."

The solution is to run a text chat beside the video conference
where people can signal that they want to speak;
the moderator can then select people from the waiting list.
Text chat is better than the "raise hand" feature most video conferencing tools offer
because the person who wants to speak can indicate why.
For example,
they can type "question about budget"
rather than just "question"
so that the moderator can group related questions together.

## Governance

The first release of GitHub's [Minimum Viable Governance][github-mvg] guidelines said:

<blockquote>
**2.1. Consensus-Based Decision Making**

Projects make decisions through consensus of the Maintainers.
While explicit agreement of all Maintainers is preferred,
it is not required for consensus.
Rather,
the Maintainers will determine consensus based on their good faith consideration of a number of factors,
including the dominant view of the Contributors and nature of support and objections.
The Maintainers will document evidence of consensus in accordance with these requirements.
</blockquote>

It sounds reasonable,
but it is harmfully wrong.
Every team has a power structure:
the question is whether it's formal or informal—in other words,
whether it's accountable or unaccountable [% b Freeman1972 %].
In the latter case,
decisions will effectively be made by the people
who are the most self-confident or stubborn
rather than by those with the most insight.

To guard against this,
groups need to spell out who has the authority to make which decisions
and how to achieve consensus.
In short,
they need explicit [% g governance "governance" %].

[% g marthas_rules "Martha's Rules" %] [% b Minahan1986 %]
are a practical way to do this in groups of up to a few dozen people,
and work very well for smaller teams too:

1.  Before each meeting, anyone who wishes may sponsor a proposal.
    Proposals must be filed at least 24 hours before a meeting in order to be considered,
    and must include:
    -   a one-line summary
    -   the full text of the proposal
    -   any required background information
    -   pros and cons
    -   possible alternatives

2.  A quorum is established in a meeting if half or more of voting members are present.

3.  Once a person has sponsored a proposal,
    the group may not discuss or vote on the issue
    unless the sponsor or their delegate is present.

4.  After the sponsor presents the proposal
    a [% g sense_vote "sense vote" %] is cast:
    -   Thumbs up: who likes the proposal?
    -   Thumbs down: who is uncomfortable with the proposal?
    -   Thumbs sideways: who can live with?

5.  If everyone likes or can live with the proposal,
    it passes with no further discussion.

6.  If the majority is uncomfortable with the proposal,
    it is sent back to its sponsor for further work.
    (The sponsor may decide to drop it if it's clear the majority isn't ever going to support it.)

7.  Otherwise,
    the group has a brief moderated discussion.
    After 10 minutes,
    or when no one has anything further to add,
    the moderator calls for a straight yes-or-no vote on the proposal.
    If a majority votes "yes" it is adopted;
    otherwise,
    it is returned to the sponsor for further work.

Every group that uses Martha's Rules must make two procedural decisions:

How are proposals put forward?
:   The easiest way to do this in a software project
    is to file an issue in the project's issue tracker
    tagged *Proposal*.
    Team members can comment on it there
    so that the sponsor can revise it before bringing it to a vote.

Who gets to vote?
:   In a course project the answer is "whoever is part of the team,"
    but a more explicit rule is needed for larger or longer-lived projects.
    One method is for existing members to nominate new ones,
    and for the team to hold a straight yes-or-no vote on each.
    Another is to automatically include anyone whose changes to the code
    were accepted by existing members,
    though this under-values non-programming contributions
    like doing code reviews
    or testing new releases.

Rules that people don't know about can't help them.
Once your team agrees on a decision-making procedure,
document it for newcomers
(and to prevent disputes among people already in the team).
You can put this in the project's `README` file
or in a separate file called `CONTRIBUTING`.
Wherever it goes,
remember that the easier it is for people to figure out how to contribute,
the more likely they are to do so [% b Steinmacher2014 %].

<blockquote markdown="1">
### Nothing about us without us

The rules laid out above were created
by and for people near the middle of the curve with respect to focus and attention span.
People who are [% g "neurodivergent" "neurodivergent" %],
i.e., whose brains work differently from the average
when it comes to sociability, learning, attention, and mood
may find that other approaches work better for them.

But while society accepts that
people of different heights need different desks and seating to be comfortable,
there is still a lot of stigma
associated with differences in mental function,
which are often classified according to
[how inconvenient they are to other people][adhd-thread].
One example is how tests for
[% g "adhd" "attention-deficit/hyperactivity disorder" %]
(ADHD) are phrased.
"Subject is overly talkative": compared to who?
"Subject does X when it is inappropriate": by whose rules?
"Struggles to pay attention": in fact,
most people with ADHD can pay very close attention,
but not when they are in environments like noisy classrooms
that are full of distractions.

Decisions that affect people should only be made
with the full participation of those who will be affected.
If you are neurodivergent,
you probably have a set of strategies for managing time and attention.
If you are [% g "neurotypical" "neurotypical" %]
and have neurodivergent teammates,
ask them what works well for them rather than ignoring the difference
or guessing what they might want.
Please do the same if you have teammates who have difficulty seeing, hearing, or moving about:
they have expertise you don't.
</blockquote>


## To Do

You probably have a to-do list somewhere. It might be scribbled in a calendar or
lab notebook, kept in a text file on your laptop, or in your head; wherever and
however you maintain it, it lists the things you're supposed to do, when they're
due, and (possibly) how urgent they are.

At its simplest, an [% g issue_tracker "issue tracker" %]
is a shared to-do list. Issue tracking systems are also called
ticketing systems and bug trackers because most software projects use them to keep
track of the bugs that developers and users find. These days, issue trackers are
almost invariably web-based. To create a new issue, you enter a title and a
short description; the system then assigns it a unique serial number. You can
usually also specify:

-   what kind of issue it is (such as a bug report, a request for a new feature,
    or a question to be answered);

-   who is responsible for the issue (i.e., who's supposed to fix the bug, test
    the fix, or update the documentation);

-   how important it is; and

-   when it's due.

If version control keeps track of where your project has been, your issue
tracking system keeps track of where you're going. After version control, it is
the most important part of a team project; without it, you and your teammates
will have to constantly ask each other "What are you working on?", "What am I
supposed to be working on?", and "Who was supposed to do that?" Once you start
using one it's easy (or at least easier) to find out what the project's status
is: just look at the open issues and at those that have been closed recently.
You can use this to create agendas for your status meetings, and to remind
yourself what you were doing three months ago when the time comes to write your
final report.

Of course, a issue tracker is only as useful as what you put into it.  If you're
describing a bug in a large application, you should include enough information
to allow someone to reproduce the problem. This is why industrial-strength
systems like [Jira][jira] can have a couple of dozen fields for each issue, including:

-   what version of the software you were using;

-   what platform it was running on;

-   what you did to make it crash;

-   any data or configuration files the program relies on;

-   whatever stack traces, error reports, or log messages the program produced;

-   its severity (i.e., how much damage the bug might do); and

-   other issues that might be related.

This is a lot more information than student projects require. In addition,
students are almost always working on several courses at once, and it's common
for students to have to put their team project aside for a few days to work on
assignments for other courses. For these reasons, I've found that most student
teams won't actually use anything more sophisticated than a web-base to-do list
unless they're forced to by the grading scheme. In that case, most come away
with the impression that issues are something you only use when you have to.

So what does a good issue look like?  [% b Bettenburg2008 %] found that the
information users supply when they file a bug report tends not to be that which
the relevant developers need the most, and most importantly, it differs in
fairly predictable ways and for understandable reasons:

FIXME: bug-report.txt

The ID on the first line is assigned by the issue tracker, an often serves as a
shorthand name for the issue in conversation. ("Hey, is anyone working on number
fifty-five yet?") The date is in [% g utc "UTC" %]
so that it is unambiguous: while your team may all be in one place, it's
increasingly likely that you are scattered across several time zones.

The title on line 3 is probably the most
important part of the issue. Projects will accumulate hundreds of issues over
time; a good subject line makes it much easier to find the ones you need. The
`type`, `severity`, and `labels` fields also improve
[% g discoverability "discoverability" %];
while `type` and `severity` could be labels, having them in fields of their own
makes it easier to sort and filter issues.

Finally, the description briefly
summarizes the problem. If the author hadn't already identified the cause, it
should include a [% g reprex "reproducible example" %] (also called a reprex). This helps the person understand what the
issue is much more than, "The program crashes when I open strange files," but
experience shows that if people are required to come up with a reprex when
filing an issue, they will often solve their own problem along the way.

<blockquote markdown="1">
### When to start saying "no"

As we will see LATER, one purpose of a schedule is to tell you
when to start cutting corners. Similarly, one of the main reasons to keep
issues in
one place is to help you prioritize work when time starts to run short.
The simplest rule comes from Yanina Bellini Saibene:
always finish first the tasks that will allow other people to continue/start/finish their work.
</blockquote>

## Labeling Issues

The bigger a project gets, the harder it is to find things.  Issue trackers
therefore let project members add [% g issue_label "labels" %] to issues to make things easier to search
and organize.  Labels are also often called tags; whatever term is used, each
one is just a descriptive word or two.

GitHub allows project owners to define any labels they want.  A small project
should always use some variation on these three:

Bug
:   Something should work but doesn't.

Enhancement
:   Something that someone wants added to the software.

Task
:   something needs to be done, but won't show up in code (e.g., organizing the
    next team meeting).

Projects also often use:

Question
:   where is something or how is something supposed to work?  As noted above,
    issues with this label can often be recycled as documentation.

Discussion or Proposal
:   something the team needs to make a decision about or a concrete proposal to
    resolve such a discussion.  All issues can have discussion: this category is
    for issues that start that way.  (Issues that are initially questions are
    often relabeled as discussions or proposals after some back and forth.)

The labels listed above identify the kind of work an issue describes.  A
separate set of labels can be used to indicate the state of an issue:

Urgent
:   Work needs to be done right away.  (This label is typically reserved for
    security fixes).

Current
:   This issue is included in the current round of work.

Next
:   This issue is (probably) going to be included in the next round.

Eventually
:   Someone has looked at the issue and believes it needs to be tackled, but
    there's no immediate plan to do it.

Won't Fix
:   Someone has decided that the issue isn't going to be addressed, either
    because it's out of scope or because it's not actually a bug.  Once an issue
    has been marked this way, it is usually then closed.  When this happens,
    send the issue's creator a note explaining why the issue won't be addressed
    and encourage them to continue working with the project.

Duplicate
:   This issue is a duplicate of one that's already in the system.  Issues
    marked this way are usually also then closed; this is another opportunity to
    encourage people to stay involved.

Some projects use labels corresponding to upcoming assignments instead of
Current, Next, and Eventually.  This approach works well in the short term, but
becomes unwieldy as labels with names like `exercise-14` pile up.  Instead, a
project team will usually create a [% g milestone "milestone" %], which is a set of issues
and pull requests in a single project repository.  GitHub milestones can have a
due date and display aggregate progress toward completion, so the team can
easily see when work is due and how much is left to be done.