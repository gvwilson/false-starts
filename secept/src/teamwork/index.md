---
title: "Teamwork"
syllabus:
- Fair, efficient meetings produce better outcomes in less time.
- Report progress, plans, and problems.
- Make major decisions by majority consensus with opportunity for discussion.
- Having a plan for handling bad behavior makes bad behavior less likely and less harmful.
- People are less productive overall when they work more than 35-40 hours a week.
- Use an effort-importance grid to prioritize work.
---

[%b Sedano2017 %] found nine types of waste in software development projects:

1.  building the wrong feature or product;
2.  mismanaging the backlog;
3.  rework;
4.  unnecessarily complex solutions;
5.  extraneous cognitive load;
6.  psychological distress;
7.  waiting and multitasking;
8.  knowledge loss; and
9.  and ineffective communication.

Only two of these are software issues,
so if you only think about the code in your project and not about the people writing it,
everything will take longer and hurt more than it needs to.
Our first lesson therefore focuses on working efficiently with others;
we will look at development process in more detail in [%x process %].

## Meetings {: #teamwork-meetings}

The most important team skill is running meetings efficiently.
The key to doing that is to distinguish between:

-   [%g status_meeting "status" %] or [%g stand_up_meeting "standup meetings" %]
    for keeping everyone up to date on what everyone else is doing
    and making simple decisions when the options are well understood;

-   [%g discussion_meeting "discussion meetings" %]
    for weighing alternatives and making complex decisions;
    and

-   brainstorming sessions and programming sprints
    devoted to the content of the project rather than its operation.

Every team should have a short weekly status meeting
to ensure team members are still working toward the same goals
and to give them a chance to figure out how they can help one another.
For each meeting,
create a table in a shared document like the one in [%t teamwork_status %].
Everyone adds a few bullet points to their row in the table
at least half an hour before the meeting starts
so that the whole team can mull everything over.
If anyone wants to discuss something,
they highlight it by adding a comment.
The meeting moderator then goes through the highlighted items one by one,
spending no more than a couple of minutes on each;
anything that requires more time is deferred to a discussion meeting

<div class="table" id="teamwork_status" caption="Status Update Table" markdown="1">
| Person | Progress | Plans | Problems |
| ------ | -------- | ----- | ---------- |
| Ren    | Parsing OCTL records | Tag OCTL records in DVC | Duplicate OCTL tags? |
|        | Deployed progress bar patch | Help onboard Silvia | |
| Mikka  | Refactored PostgreSQL connector | #156: handle records with NULL timestamp | Clarify authorship guidelines |
|        | Patched database tests | #171: auto-archive duplicate records | |
| Sanjay | … | … | … |
| Jess   | … | … | … |
</div>

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
    Equally,
    nobody should [%g feigning_surprise "feign surprise" %]:
    saying, "Gosh, I thought *everyone* knew [random fact],"
    is about putting people down rather than sharing information.

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
there is no better place to start than [%b Brookfield2016 %],
which catalogs fifty different techniques for managing discussions
and explains when and how each is useful.

### Air Time

One problem with meetings is that
some people may talk far more than others.
Other people may be so accustomed to this
that they don't speak up even when they have valuable points to make.

You can combat this
by giving everyone [%g three_sticky_notes "three sticky notes" %]
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
[%g interruption_bingo "interruption bingo" %].
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
[%b Troy2018 %] points out that in most online meetings,
the first person to speak during a pause gets the floor.
As a result:

> If you have something you want to say,
> you have to stop listening to the person currently speaking
> and instead focus on when they're gonna pause or finish
> so you can leap into that nanosecond of silence
> and be the first to utter something.
> The format…encourages participants who want to contribute to say more and listen less.

The solution is to run a text chat beside the video conference
where people can signal that they want to speak;
the moderator can then select people from the waiting list.
Text chat is better than the "raise hand" feature most video conferencing tools offer
because the person who wants to speak can indicate why.
For example,
they can type "question about budget"
rather than just "question"
so that the moderator can group related questions together.

<div class="callout" markdown="1">

### Are you a blowfish or a clam?

[NOAA's guide][noaa_disruptive] to dealing with disruptive behaviors
has useful labels and even more useful advice
for handling people who may send meetings off course.

</div>

## Making Decisions {: #teamwork-decisions}

The first release of GitHub's [Minimum Viable Governance][github_mvg] guidelines said:

> **2.1. Consensus-Based Decision Making**
>
> Projects make decisions through consensus of the Maintainers.
> While explicit agreement of all Maintainers is preferred,
> it is not required for consensus.
> Rather,
> the Maintainers will determine consensus based on their good faith consideration of a number of factors,
> including the dominant view of the Contributors and nature of support and objections.
> The Maintainers will document evidence of consensus in accordance with these requirements.

It sounds reasonable,
but it is harmfully wrong.
Every team has a power structure:
the question is whether it's formal or informal—in other words,
whether it's accountable or unaccountable [%b Freeman1972 %].
In the latter case,
decisions will effectively be made by the people
who are the most self-confident or stubborn
rather than by those with the most insight.

To guard against this,
groups need to spell out who has the authority to make which decisions
and how to achieve consensus.
In short,
they need explicit [%g governance "governance" %].

[%g marthas_rules "Martha's Rules" %] [%b Minahan1986 %]
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
    a [%g sense_vote "sense vote" %] is cast:
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
the more likely they are to do so [%b Steinmacher2014 %].

### Nothing About Us Without Us

The rules laid out above were created
by and for people near the middle of the curve with respect to focus and attention span.
People who are [%g neurodivergent "neurodivergent" %],
i.e., whose brains work differently from the average
when it comes to sociability, learning, attention, and mood
may find that other approaches work better for them.

But while society accepts that
people of different heights need different desks and seating to be comfortable,
there is still a lot of stigma
associated with differences in mental function,
which are often classified according to
[how inconvenient they are to other people][adhd_thread].
One example is how tests for
[%g adhd "attention-deficit/hyperactivity disorder" %]
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
If you are [%g neurotypical "neurotypical" %]
and have neurodivergent teammates,
ask them what works well for them rather than ignoring the difference
or guessing what they might want.
Please do the same if you have teammates who have difficulty seeing, hearing, or moving about:
they have expertise you don't.

## Handling Conflict {: #teamwork-conflict}

You just missed an important deadline, and people are unhappy.
The sick feeling in the pit of your stomach has turned to anger:
you did *your* part, but Sylvie didn't finish her stuff until the very last minute,
which meant that no one else had time to spot the two big mistakes she'd made,
and Surinder didn't deliver at all—again.
If something doesn't change, you're going to fail this course.

[%i "conflict (interpersonal)" %]Conflicts[%/i%] like this
come up all the time.
We can deal with them in four ways:

1.  Cross our fingers and hope that things will get better on their own,
    even though they didn't the last three times.

2.  Do extra work to make up for others' shortcomings.
    This strategy avoids the stress of confronting others in the short run,
    but the time for that "extra" has to come from somewhere.
    Sooner or later,
    our personal lives or other responsibilities will suffer.

3.  Lose our temper.
    People often displace anger into other parts of their lives:
    they may yell at someone for taking an extra few seconds to make coffee
    when what they really need to do is tell their teammates that
    they aren't going to miss another dinner with their family
    in order to clean up a mess that someone else made.

4.  Fix the underlying problem.

Most of us find the first option easiest.
The fourth is harder because we don't like confrontation.
Managed properly,
though,
it can be much less bruising,
which means that we don't have to be as afraid of it.
And if people believe that we will take steps when they lie,
bully,
procrastinate,
or do a half-assed job,
they will often avoid making it necessary.

### Bad Actors are Rare

An internal study at Facebook in 2021 found that
just over 100 people were the source of almost half of harmful disinformation
about COVID-19 vaccination [%b Dwoskin2021 %].
Similarly,
one of the designers of the game *Ultima Online* [reported][ultima_online_players],
"…we asked players what percentage of the player base were degenerate player killers.
Players responded with 10%.
The metrics told us the answer was closer to 0.1%."

These findings and many others tell us that
[%i "toxic people!rarity of" %]a small number of people[%/i%]
cause a disproportionate amount of grief in our communities (online and otherwise),
and that they seem much more common than they are
because incidents of abuse and conflict loom large in our memories.

The irony is that *The Walking Dead* and *Mad Max* have it completely backward:
when a real disaster strikes,
most people actually rise to the occasion.
As [%b Solnit2010 %] describes,
[%i "toxic people!misperception of" %]neighbors don't turn on each other[%/i%]
in the aftermath of an earthquake or a hurricane.
Instead,
they are more likely to look out for each other than under normal circumstances.
That doesn't make for exciting viewing,
though,
and the powerful have always wanted the rest of us to believe that
the only alternative to their rule is chaos.

### What to Do

A shared understanding of [%i "conflict (interpersonal)!handling" %]how to handle conflict[%/i%]
helps in the same way as basic first aid training:
having some idea of what to do makes you more likely to actually do *something*
when the time comes.

Make sure you are not guilty of the same sin.
:   You won't get very far complaining about someone else interrupting in meetings
    if you do it just as frequently.

Check expectations.
:   Are you sure the offender knows what standards they are supposed to meet?
    This is where things like a `CONTRIBUTING` file are helpful.

Check the situation.
:   Is someone dealing with an ailing parent or immigration woes?
    Do they have deadlines for three other projects that we don't know about?
    Use open questions like, "Can you help me understand this?" when checking in.
    These give them the freedom to explain something you may not have expected
    while avoiding the pressure of being asked directly about
    something they don't want to discuss.

Document the offense.
:   Write down what the offender has actually done and why it's not good enough.
    Doing this helps you clarify what you're upset about
    and is essential if you have to escalate.

Check with other team members.
:   Are you alone in feeling that the offender is letting the team down?
    If so, you aren't necessarily wrong,
    but it will be a lot easier to fix things if you have the support of the rest of the team.
    Finding out who else on the team is unhappy can be the hardest part of the whole process,
    since you can't even ask the question without letting on that you are upset,
    and word will almost certainly get back to whoever you are asking about,
    who might then accuse you of stirring up trouble.

Talk with the offender.
:   This should be a team effort.
    Put it on the agenda for a meeting,
    present the complaint,
    and make sure that the offender understands it.
    This is sometimes enough to solve the problem:
    if someone realizes that they're going to be held accountable,
    they will often change their ways.

Escalate as soon as there's a second offense.
:   People who don't have good intentions
    count on us giving them one last chance after another
    until the project is finished and they can go suck the life out of their next victim.
    *Don't fall into this trap.*
    If someone stole your laptop you would report it right away.
    If someone steals your time,
    it's foolish to give them a chance to do it again and again.

In a student project,
"escalation" means taking the issue to the instructor.
They have probably had dozens of students complain to them over the years
about teammates not doing their share,
and it isn't uncommon to have both halves of a pair say that they're doing all the work.
In order to get them to take you seriously and help you fix the problem,
you should send them an email signed by several people
that describes what's happened and the steps already taken.
Make sure the offender gets a copy as well,
and ask the instructor to arrange a meeting to resolve the issue.

One technique your instructor may ask you to use in a meeting of this kind
is [%i "active listening" %][%g active_listening "active listening" %][%/i%].
When one person makes a point,
the person on the other side of the issue explains it back to them,
as in, "So what I think Igor is saying is…"
This confirms that the second person has actually paid attention to what the first person said.
It can also defuse a lot of tension,
since explaining your position back to you clearly
forces the other person to see the world through your eyes,
if only for a few moments.

<div class="callout" markdown="1">

### Hitchhikers

[%i "hitchhiker" %][%g hitchhiker "Hitchhikers" %][%/i%]
who show up but never actually do anything are particularly difficult to manage,
in part because they are usually very good at appearing reasonable.
They will nod as you present your case,
then say,
"Well, yes, but…" and list a bunch of minor exceptions
or cases where others on the team have also fallen short of expectations.
Tracking progress and contributions is essential for handling them.
If you can't back up your complaint,
the instructor may be left with the impression that the whole team is dysfunctional.

</div>

Finally,
it's important to recognize that good principles sometimes conflict [%b Berlin2000 %].
For example,
suppose that a student has a medically diagnosed attention difference
that requires them to talk to themselves quite loudly while programming in order to stay focused,
but other members of their team find this very distracting.
Asking the student in question to program somewhere else
would be punishing them for something they can't control,
while asking everyone else to put on headphones
would make their interaction more difficult and their work less fun.
There might not be a solution that satisfies everyone;
in such cases,
the best path is to do the kindest thing possible.

### Escalation

What can you do if [%i "conflict (interpersonal)!escalating" %]conflict[%/i%]
becomes more personal and heated?
[Charles' Rules of Argument][charles_rules] are a good starting point:
FIXME check this

Be short, simple, and firm.
:   People rarely complain that a speech is too short.

Don't try to be funny.
:   It almost always backfires, or will later be used against you.

Play for the audience.
:   You probably won't change the person you are calling out,
    but you might change the minds or strengthen the resolve of people who are observing.

Pick your battles.
:   You can't challenge everyone, every time,
    without exhausting yourself and deafening your audience.
    An occasional sharp retort is much more effective than constant criticism.

Don't shame or insult one group when trying to help another.
:   For example,
    don't call someone ugly when what you really mean is
    that they're racist or homophobic.

But sometimes it isn't just one person on the team who's a problem;
sometimes the whole team is dysfunctional.
I worked at a startup for a couple of years in my early 30s.
Individually, we were all smart, decent people.
Put us together,
though,
and our IQs and personalities canceled out,
leaving us collectively as dumb as a sack full of hammers.

There's not a lot you can do in cases like this except [%i "teams!dissolving" %]start over[%/i%].
Instructors can allow for this by announcing at the start of the course
that teams will be dissolved and re-formed halfway through the project
*unless* every member on the team submits a separate signed request to stay together.
There's a bit of psychology here:
if people are required to ask for their team to be dissolved
they will often think it's more trouble than it's worth.
If dissolution is the default,
though,
students won't be inhibited by any stigma attached to being the one who caused trouble.

Students also usually understand that
dissolving their team and forming a new one
takes time that could be invested in earning a higher grade.
In practice,
therefore,
teams usually stick together if they see that troublemakers are actually being dealt with.

<div class="callout" markdown="1">

### Who gets to keep the cat?

If the instructor allows or requires teams to re-form partway through the
project, they should explain at the start of the course what will happen to the
work the team has done up to that point. Can each member of the team that is
dissolving use everything the whole team has built up to that point? Do they
have to re-start with whatever has been written by the teams they are joining?
Knowing this in advance helps everyone decide whether breaking up is worth it.

</div>

## Crunch Mode {: #teamwork-crunch}

We said above that bad actors are rare,
but exhaustion can make anyone grumpy.
Scientific study of [%i "overwork" %]overwork[%/i%] goes back to at least the 1890s [%b Robinson2005 %].
The most important results are:

1.  [%i "productivity" %]Productivity[%/i%] varies over the course of the workday;
    you are most productive in the first 4–6 hours;
    after that productivity approaches zero and eventually becomes negative.

1.  Working more than eight hours a day for more than a couple of weeks of time
    lowers your total productivity,
    not just your hourly productivity—i.e., you get less done *in total*
    in [%i "crunch mode" %][%g crunch_mode "crunch mode" %][%/i%]
    than when you work regular hours.

1.  Working over 21 hours in a stretch
    increases the odds of you making a catastrophic error
    just as much as being legally drunk.

These facts have been verified through hundreds of experiments
over the course of more than a century,
including some on novice software developers [%b Fucci2020 %].
The data behind them is as solid as the data linking smoking to lung cancer.
However,
while most smokers will at least acknowledge that their habit is killing them,
people in the software industry still talk and act as if
they were somehow immune to science.
To quote  [%b Robinson2005 %]:

> When [%i "Ford, Henry" %]Henry Ford[%/i%] famously adopted a 40-hour workweek in 1926,
> he was bitterly criticized by members of the National Association of Manufacturers.
> But his experiments,
> which he'd been conducting for at least 12 years,
> showed him clearly that cutting the workday from ten hours to eight hours—and
> the workweek from six days to five days—increased
> total worker output and reduced production cost…
> the core of his argument was that reduced shift length meant more output.
>
> …many studies,
> conducted by businesses, universities, industry associations and the military,
> …support the basic notion that,
> for most people,
> eight hours a day,
> five days per week,
> is the best sustainable long-term balance point between output and exhaustion.
> Throughout the 30s, 40s, and 50s, these studies were apparently conducted by the hundreds;
> and by the 1960s,
> the benefits of the 40-hour week were accepted almost beyond question in corporate America.
> In 1962,
> the Chamber of Commerce even published a pamphlet extolling the productivity gains of reduced hours.
>
> But, somehow, Silicon Valley didn't get the memo…

I spent two years at a data visualization startup.
Three months before our first release,
the head of development "asked" us to start coming in on Saturdays.
We were already pulling one late night a week at that point
(without overtime pay—our boss seemed to think that
ten dollars' worth of pizza
was adequate compensation for four hours of work)
and most of us were also working at least a couple of hours at home in the evenings.
To no one's surprise,
we missed our "can't miss" deadline by ten weeks,
and had to follow up our 1.0 release with a 1.1 and then a 1.2
to fix the crash-and-lose-data bugs we'd created.
We were all zombies, and zombies can't code.

Hours like these are sadly still normal in many parts of the software industry,
and may actually be worse now that so many people are working from home.
Designing and building software is a creative act that requires a clear head;
it only takes a couple of minutes to create a bug
that will take hours to track down later.

It's hard to quantify the productivity of programmers, testers, and UI designers
[%b Sadowski2019b Forsgren2021 %],
but five eight-hour days per week has been proven to maximize long-term total output
in every industry that has ever been studied.
There is no reason to believe that ours is any different.

Ah, you say, but that's *long-term* output.
What about short bursts now and then,
like pulling an all-nighter to meet a deadline?
That's been studied too,
and the results aren't pleasant.
Your ability to think drops by 25 points for each 24 hours you're awake.
Put it another way,
the average person's IQ is only 75 after one [%i "all-nighters" %]all-nighter[%/i%],
which puts them in the bottom 5% of the population.
Two all nighters in a row and their effective IQ is 50—the level at which
people are considered incapable of independent living.

The catch in all of this is that people usually don't notice their abilities declining.
Just like drunks who think they're still able to drive,
people who are deprived of sleep don't realize that they're not finishing their sentences (or thoughts).
They certainly don't realize that they're calling functions with parameters in the wrong order
or that the reason the tests are failing is that
they've forgotten to redeploy the application—again.

### Time Management

[%b Edwards2009 %] found that
starting assignments early and working consistently predicted good grades.
However,
while people in industry joke that having two bosses means living in hell,
students usually answer to four or five professors
whom don't coordinate due dates across their courses.

The least bad way to handle this situation is to prioritize carefully.
Get a piece of paper and draw
[%i "effort-importance grid" %][%g effort_importance_grid "a 3×3 grid" %][%/i%].
The X axis is effort: label its divisions "minutes", "hours", and "days".
The Y axis is time: label it "low", "medium", and "high".
You should wind up with something like [%f effort-importance %].

[% figure
   slug="effort-importance"
   img="effort-importance.svg"
   alt="Effort/importance matrix"
   caption="An example of an effort/importance matrix."
%]

Next,
put everything you need to do somewhere on the grid,
and then throw away the high-effort, low-importance items in the bottom right—you
aren't going to get to those.
You can then start assembling the other items into a schedule,
starting with the upper-left corner.
These are the things that will give the highest return on invested time;
more importantly,
starting with these means that if you've under-estimated effort,
you will still deliver *something*.

The tricky items are the ones on the diagonal.
Should you tackle one thing that is high effort and high importance
or three things that are individually less important
but require the same total effort?
Laying things out on a grid can't answer that question,
but at least it can tell you what the question is.

> How to prioritize:
> always finish first the tasks that will allow other people to continue/start/finish their work.
>
> — Yanina Bellini Saibene

If any task on your list is more than an hour long,
break it down into smaller pieces and prioritize those separately.
Figuring out what those pieces are can take time,
so don't be embarrassed to make "plan XYZ" a task in its own right.
And remember that the future is approaching at a rate of 24 hours per day:
if something is going to take thirty hours to finish,
you had better allow at least five working days for it,
which means you'd better start at least that far ahead of the deadline.

The point of all this organization and preparation is
to be able to immerse yourself in your problem.
[%b Csikszentmihalyi1991 %] popularized the term [%i "flow" %][%g flow "flow" %][%/i%] for this;
athletes call it "being in the zone",
while musicians talk about losing themselves in what they're playing.
The good news is that you're much more productive in this state
than when you're multi-tasking.
The bad news is that
it takes anywhere from several seconds to several minutes
to get back into this state after an interruption [%b Parnin2010 Borst2015 %].
In other words,
if you are interrupted half a dozen times per hour
you are *never* at your productive peak.
Ironically,
the cost of self-interruptions may be even worse than the cost for external interruptions [%b Abad2018 %].

<div class="callout" markdown="1">

### Open offices suck

[%i "open offices (evils of)" %]Open offices[%/i%] were created
so that (mostly male) managers could keep an eye on (mostly female) office workers,
and to reduce air conditioning costs [%b Eley1995 %].
They lower productivity in every other way we can measure [%b Bernstein2018 %];
sadly,
the same is true of other interruption-rich environments
like your favorite coffee shop.
If you really want to be productive,
you should avoid both.

</div>

Finally,
you will be more productive in the long run if your back doesn't ache,
and being away from the keyboard
gives your brain a chance to reflect on what you've just been doing.
You should therefore take a five-minute [%i "breaks (importance of regular)" %]break[%/i%] every hour.
Checking email doesn't count:
get up and stretch,
refill your water bottle,
or go and restack the dishwasher.
You'll be amazed at how often you can solve a problem that's been baffling you for an hour
by taking a short walk…

## Exercises {: #teamwork-exercises}

FIXME
