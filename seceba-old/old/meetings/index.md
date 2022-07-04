---
title: "Meetings"
lede: "The most useful thing you will learn in this book"
template: page
---

[% i "meetings" %]Meetings[% /i %] are the atoms out of which projects are made,
so if you want your project to succeed,
you need to learn how to run meetings efficiently.
The key is to distinguish between:

-   [% i "meetings!status" "status meeting" %][% g status_meeting %]Status meetings[% /g %][% /i %]
    that keep people up to date with what their teammates are doing.

-   [% i "meetings!discussion" %][% g discussion_meeting %]Discussion meetings[% /g %][% /i %]
    for weighing alternatives and making complex decisions.

-   Co-working sessions like brainstorming sessions and programming sprints
    that are devoted to the content of the project rather than its operation.

## Status Meetings

Every team should have a short weekly status meeting.
Create a table in a shared document like the one in [% t meetings-status %] for each meeting.
Everyone adds a few bullet points to their row in the table
at least half an hour before the meeting starts
so that everyone else can see where they are,
what they're planning to do,
and what's on their mind.
If anyone wants to discuss something,
they highlight it by adding a comment.
The meeting moderator then goes through the highlighted items one by one,
spending no more than a couple of minutes on each;
anything that requires more time is deferred to a discussion meeting.

<div class="table" id="meetings-status" caption="Status Update Table" markdown="1">
| Person | Progress | Plans | Problems |
| ------ | -------- | ----- | ---------- |
| Ren    | Parsing OCTL records | Tag OCTL records in DVC | Duplicate OCTL tags? |
|        | Deployed progress bar patch | Help onboard Silvia | |
| Mikka  | Refactored PostgreSQL connector | #156: handle records with NULL timestamp | Clarify authorship guidelines |
|        | Patched database tests | #171: auto-archive duplicate records | |
| Sanjay | … | … | … |
| Jess   | … | … | … |
</div>

## Decision Meetings

Decision meetings are for issues that need deeper discussion,
either because they will have significant long-term impact on the project
or because team members disagree on what to do.
Since the stakes are higher,
they need more structure:

Decide if there actually needs to be a meeting.
:   If the only purpose is to share information,
    send an email:
    most people can read faster than they can speak.

Write an agenda.
:   If you are using Martha's Rules (discussed below and in [% x governance %]),
    the agenda is every issue in the repository marked `proposal`.
    If not,
    ask team members to add discussion items to a shared document
    at least a few hours before the meeting.
    If nobody cares enough about the meeting to prepare
    a point-form list of what's to be discussed,
    the team either doesn't need to have a meeting
    or is running out of steam.

Include timings in the agenda.
:   Doing this helps prevent early items stealing time from later ones.
    The first estimates with any new group are inevitably optimistic,
    so expect to revise them upward for subsequent meetings.

Select a moderator.
:   Put one person in charge of keeping items on time,
    selecting the next person to speak,
    chiding people who are having side conversations or checking email,
    and asking people who are talking too much to get to the point.
    The moderator should *not* do all the talking:
    in fact,
    the moderator will talk less in a well-run meeting than most other participants.

Prioritize.
:   Tackle the most important issues first,
    even if they're the longest,
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

Take [% i "meetings!minutes)" %]minutes[% /i %].
    Someone other than the moderator should record
    the most important information that was shared
    and every decision that was made or every task that was assigned to someone.
    (It's difficult for the moderator to do this and stay on top of the discussion,
    so it's common for the previous week's moderator to be this week's note-taker.)

End early.
:   If the meeting is scheduled for 10:00--11:00,
    end at 10:50 to give people a break before whatever they're doing next.

As soon as the meeting is over,
share the minutes with the whole team so that:

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

To share the minutes,
add them to the project's wiki,
version control repository,
or shared cloud drive.
Don't email them to people
unless the project is using a searchable mailing list as its primary communication channel:
newcomers and whoever is grading your work will need access to the project's history,
and they can't read your personal inbox.

<blockquote markdown="1">
### No distractions

Side conversations make meetings less efficient
because people can't actually pay attention to two things at once.
More importantly,
if someone checks their email or texts a friend during a meeting,
it's a signal that they don't think the speaker is important.
This rule doesn't mean a complete ban on technology—people may need accessibility aids
or be waiting for a call about childcare—but by default
phones should be face down and laptops should be closed
during in-person meetings.

FIXME: online meetings
</blockquote>

## Air Time

One problem with meetings is that
some people may talk far more than others.
Other people may be so accustomed to this
that they don't speak up even when they have valuable points to make.

You can combat this
by giving everyone [% i "meetings!three sticky notes" "three sticky notes (in meetings)" %]three sticky notes[% /i %]
(or coins, or paperclips—anything inedible will do) at the start of the meeting.
Every time someone speaks,
they have to give up one sticky note.
When they're out of stickies,
they aren't allowed to speak until everyone has used at least one,
at which point everyone gets all of their sticky notes back.
This rule ensures that nobody talks more than three times as often as
the quietest person in the room,
which completely changes group dynamics.
People who have given up trying to be heard suddenly have space to contribute,
and overly-frequent speakers realize how talkative they have been.

Another useful technique is called
[% i "meetings!interruption bingo" "interruption bingo (in meetings)" %]interruption bingo[% /i %].
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

<blockquote markdown="1">
### Are you a blowfish or a clam?

[NOAA's guide][noaa-disruptive] to dealing with disruptive behaviors
has useful labels and even more useful advice
for handling people who may send meetings off course.
</blockquote>

[% i "meetings!online" %]Online meetings[% /i %]
pose special challenges for regulating speaking time and interruptions.
[% b Troy2018 %] points out that in most online meetings,
the first person to speak during a pause gets the floor.
As a result,
"If you have something you want to say,
you have to stop listening to the person currently speaking
and instead focus on when they're gonna pause or finish
so you can leap into that nanosecond of silence
and be the first to utter something.
The format…encourages participants who want to contribute to say more and listen less."

One solution is to require people to use the "raise hand" feature included in most video conferencing tools
when they want to speak,
and then wait until the moderator calls on them.
Another is to use the video conferencing tool's text chat
and have people type something like `/question budget`,
which gives the moderator some idea of *why* they want to speak.

## Making Decisions

The first release of GitHub's [Minimum Viable Governance][github-mvg] guidelines
included this:

<blockquote markdown="1">
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
but it is harmfully naïve.
Every team has a power structure:
the question is whether it's formal and accountable
or informal and unaccountable [% b Freeman1972 %].
In the latter case,
decisions will effectively be made based on stubbornness and self-confidence
rather than knowledge and ability.
To guard against this,
groups need to spell out how decisions are made and who gets to make them.
In other words,
they need explicit [% i "governance" %][% g governance %]governance[% /g %][% /i %].

[% i "Martha's Rules" %][% g marthas_rules %]Martha's Rules[% /g %][% /i %] [% b Minahan1986 %]
are a practical way to do this in groups with up to a few dozen members
who broadly agree with one another;
if your group is larger or regularly has deeper disagreements,
you may need something more formal like
[% i "Robert's Rules of Order" %][% g roberts_rules %]Robert's Rules of Order[% /g %][% /i %]
(and some training in how to follow them).

[% x governance %] explains how Martha's Rules work,
but do *not* explain who gets to vote.
In a course project the answer is "whoever is part of the team,"
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
You can put this in the project's [% i "README file" %]`README`[% /i %] file ([% x mvp %])
or in a separate file called [% i "GOVERNANCE file" %]`GOVERNANCE`[% /i %].
Wherever it goes,
remember that the easier it is for people to figure out how to participate,
the more likely they are to do so [% b Steinmacher2014 %].

## Nothing About Us Without Us

The rules laid out above were created
by and for people near the middle of the bell curve with respect to focus and attention span.
People who are [% i "neurodivergence" %][% g "neurodivergence" %]neurodivergent[% /g %][% /i %],
i.e., whose brains work differently from the average
when it comes to sociability, learning, attention, and mood
may find that other approaches work better for them.

But while society accepts that
people of different heights need different desks and seating to be comfortable,
there is still a lot of [% i "neurodivergence (stigma associated with)" %]stigma[% /i %]
associated with differences in mental function,
which are often classified according to
[how inconvenient they are to other people][adhd-thread].
One example is how tests for
[% i "ADHD" %][% g "adhd" %]attention-deficit/hyperactivity disorder[% /g %][% /i %]
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
If you are [% i "neurotypical" %][% g "neurotypical" %]neurotypical[% /g %][% /i %]
and have neurodivergent teammates,
ask them what works well for them rather than ignoring the difference
or guessing what they might want.
Please do the same if you have teammates who have difficulty seeing, hearing, or moving about:
they have expertise you don't.

<blockquote markdown="1">
### Further Reading

If you would like to become better at sharing information and making decisions,
there is no better place to start than [% b Brookfield2016 %],
which catalogs fifty different techniques for managing discussions
and explains when and how each is useful.
</blockquote>

## Exercises

FIXME: create exercises for this chapter.
