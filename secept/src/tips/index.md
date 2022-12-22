---
title: "Tips"
---

This appendix offers advice that doesn't fit in any specific chapter,
but which we hope you will find useful.

## Joining a Project {: #tips-joining}

Hundreds of books have been published about how to start a tech business
or how to set up and run an open source project [%b Fogel2020 %].
Much less has been written about how to join existing projects,
even though that's what most people do most of the time.
These simple rules can help.

Search first.
:   Whatever question you have, the odds are pretty good that someone has asked
    it before, opened an issue about it, or discussed it in the project chat.
    If the project is well organized it should only take a minute to find out,
    and if you mention what you searched for when you
    do ask a question, people will probably point you in the right direction
    when they answer.

But do ask.
:   The biggest mistake newcomers make is to spend hours looking for something
    rather than asking a question.  If you have searched but haven't found
    anything helpful, it's OK to take a minute of someone else's time,
    especially if you post your question where the answer can be found by the
    next newcomer.

Remember that software is only one part of a project.
:   There are many ways to contribute to a software project.  Updating or
    translating documentation and testing bug fixes are good places to start;
    they will also help you learn your way around and make you friends.

Respect what has already been done.
:   If the first thing you do when you walk into someone's home is say, "Here's
    how I'd redecorate," you shouldn't expect to be invited back.  Follow the
    project's existing coding conventions even if you prefer something else.
    Use existing tags for issues, and above all, don't introduce yourself by
    suggesting that they rearchitect the code or change languages.

Be patient.
:   It took me almost three months of full-time work to get up to speed in my
    previous job, and the first contributor to the Python scripts used to build
    this book needed a couple of evenings to find their way around.  Depending
    on the size, age, and organization of the project you're joining, you should
    expect it to have to invest something like this much time before you feel
    productive.  (You will always look back and say, "I could have done this so
    much more quickly." You will always be wrong.)

Start small.
:   This is a corollary of the previous three points.  As you learn your way
    around a project socially as well as technologically, you will build a
    mental model of how it works.  Offering a small
    contribution is a way to test that mental model.  Do you understand the
    application's architecture?  Do you know where tests are supposed to go and
    how review and merging work?  A three-line change to documentation is a more
    cost-effective way to test this than three hundred lines of new code that
    might completely miss the mark.

Keep exploring.
:   Thousands of books have been written about how to write code, but only a few
    explain how to read it ([%b Spinellis2003 %] being my favorite).
    However, reading other people's code is one of the best ways to learn how to
    be a better programmer, while browsing a project's issues can give you even
    more insight into why the code works the way it does (and where and why it
    stops working).  If you feel that this is a less productive use of your time
    than coding, think about how much time musicians spend listening to each
    other or how much artists look at each other's work.
    (In my experience, the best approach to learning your way around a new code
    base is to trace what happens during a typical operation.  What functions or
    methods are called in what order as an HTTP request is processed?  What
    objects are created?  What changes are made to files or databases, if any?
    The "step over" button your debugger is a very useful tool for this,
    since it allows you ignore low-level details while you're
    trying to paint a bigger picture.)

Get to know people.
:   There is a softball team here in Toronto that practices every Thursday but
    hasn't played an actual game in twenty years.  As with many groups, their
    ostensible reason for existing is just an excuse for people who like each
    other to hang out.  A lot of software projects are like that, in industry as
    well as open source: participants get satisfaction from working with one
    another as well as from what they produce.  While your job won't ever love
    you back, the relationships you make with the people
    you work beside may be as rewarding as the software you build.

Remember that most relationships don't end in marriage.
:   It's OK to do a little work on an open source project and then decide if
    it's for you or not.  It's equally OK to look for a new job if you're not
    happy with the one you're in: after all, most companies wouldn't hesitate to
    eliminate your job if they needed to cut costs.  Don't let anyone manipulate
    you by making you feel guilty about this.

Share what you learn.
:   If you aren't the first person to join a project, you probably won't be the
    last.  One of the most compassionate things you can do is share what you
    found out as you were learning your way around so that the next person can
    do so more quickly.  Doing this also helps you figure out what you know now
    that you didn't know then, which can help you the next time around.

## Welcoming Newcomers {: #tips-welcoming}

To survive and thrive,
a project must attract and retain new members and help them be productive.
These rules taken from [%b Sholler2019 %] describe how to do this.

<div class="callout" markdown="1">
### Communities of practice

What exactly do we mean by "community"?
The most usual meaning in open source is a
[%i "community of practice" %][%g community_of_practice "community of practice" %][%/i%]
[%b Lave1991 Wenger1999 %] with three characteristics:

1.  Participants have a common product or purpose that they work on or
    toward.

2.  They are mutually engaged, i.e., they assist and mentor each another.

3.  They develop shared resources and domain knowledge.
</div>

Be welcoming.
:   Projects should not just say that they welcome new members: they should make
    an effort to foster positive feelings by posting a welcome message on the
    project's social media, offering assistance in making an initial
    contribution, and connecting them with existing project members.

Help potential contributors evaluate if the project is a good fit.
:   The first and most important step in being welcoming is to help them
    determine whether this project is a good fit for their interests and
    abilities.  To do this, the project should explicitly state what the
    different types of skills required are. This information should be easily
    accessible and guide new members to the tasks they may handle.

Make governance explicit.
:   [%b Raymond2001 %] described an egalitarian world in which everyone
    could contribute equally to open projects. Two decades later, we can see how
    misleading it was, and how unequal and unwelcoming projects can be if
    authority lies with those willing to shout loudest and longest
    [%b Cohen2018 %].  Large, well-established projects that incorporate
    as non-profits are required to promulgate bylaws; smaller projects should
    have some explicit [%i "governance" %]governance[%/i%] that explains who
    gets a say in what and how to become someone whose vote counts.

Keep knowledge up to date and findable.
:   A single project may use wikis, files in GitHub, shared Google Docs, old
    tweets or chat messages, and email archives; keeping information about a
    specific topic in a single place and clearly defining the purpose of each
    communication medium saves newcomers from having to navigate multiple
    unfamiliar data sources to find what they need [%b Lin2020 %].  At the
    same time, outdated documentation may lead newcomers to understand the
    project incorrectly, which is also demotivating. While it's hard to keep
    material up to date, community members should at least remove or clearly
    mark outdated information.

Have and enforce a [%i "Code of Conduct" %]Code of Conduct[%/i%].
:   We discussed this rule in [%x teamwork %], but it bears repeating here.
    Your project's culture is defined by the worst behavior it tolerates
    [%b Gruenert2015 %], and every instance of bad behavior will drive
    current and potential contributors away.

Develop forms of legitimate peripheral participation.
:   Newcomers become members of a community by participating in simple, low-risk
    tasks that existing community members believe are valuable. Through this
    [%i "legitimate peripheral participation" %][%g lpp "legitimate peripheral participation" %][%/i%],
    newcomers become acquainted with the community's
    tasks, vocabulary, and governance so that they can ease into the
    project. For example, submitting pull requests on GitHub can be daunting for
    newcomers; asking people to file issues about bugs they have found requires
    less up-front work, but is accepted as also being useful.

Make it easy for newcomers to get started.
:   One way to facilitate legitimate peripheral participation is to make it easy
    for newcomers to get set up so that they can start work on contributions.
    Getting set up to work on a project—going from "I want to help" to "I'm
    able to help" to "I'm helping"—is often someone's first experience as a
    community participant. Any complexity or confusion at this point is
    therefore a significant barrier to participation
    [%b Steinmacher2014 %]. By treating the process of getting involved
    with the same care and attention you give to the product itself, you're
    making it clear that you value those contributors' time and effort

Use opportunities for in-person interaction, but with care.
:   Combining newcomer-friendly events and activities with larger gatherings
    such as conferences amortize participants' financial costs and travel time.
    However, potential contributors might shy away from the project if they are
    introverted, suffer from social anxiety, or have had bad experiences in the
    past in face-to-face settings. A Code of Conduct helps allay these concerns,
    but some newcomers may still feel uncomfortable in group settings. In this
    case, not going to a meetup may leave them feeling less a part of the
    community.

Acknowledge all contributions.
:   People in open source sometimes joke that a programmer is someone who will
    do something for a laptop sticker that they would not do for a hundred
    dollars. The kernel of truth in this joke is that gratitude and recognition
    are the most powerful tools community builders have. It is therefore crucial
    to acknowledge newcomers' contributions and thank them for their work.
    Every project should therefore adopt and publicize guidelines describing
    what constitutes a contribution, how contributions will be acknowledged, and
    how they will be used.

Follow up on both success and failure.
:   Once someone has carried their first contribution over the line, you and
    they are likely to have a better sense of what they have to offer and how
    the project can help them. Helping newcomers find the next problem they
    might want to work on or pointing them at the next thing they might enjoy
    reading is both helpful and supportive. In particular, encouraging them to
    help the next wave of newcomers is both a good way to recognize what they
    have learned, and an effective way to pass it on.

## Being Fired {: #tips-fired}

These ten rules are based on [my experience with DataCamp][wilson_datacamp]
and on the experiences of friends and colleagues there and at other companies.

Insist on a record of all conversations,
:   because the biggest mistake you can make is to assume good faith on the part of those who fired you.
    In most jurisdictions you have a right to record any phone calls you are part of,
    and if that feels too confrontational,
    insist on communicating by email.
    If they insist on communicating by phone or video call,
    follow up immediately with an email summary
    and make sure you send a copy to your personal account.

Pause before speaking, posting, or tweeting.
:   If possible, have someone you trust look everything over before you say it or send it.
    (Don't use someone who still works for the company, even if they are your closest friend:
    it puts them in a legally and morally difficult position.)

Keep your public statements brief:
:   people may care, but most won't care as much as you do.
    A simple recitation of facts is usually damning enough.

If you want to correct something online, add a timestamped amendment
:   do not just take it down or edit it.
    If you do,
    you will be accused of rewriting history,
    and muddied waters only help whoever fired you.
    (Also, be prepared for them to dig through everything you've ever said online
    and re-post parts selectively to discredit you.)

Speak directly to all the issues rather than omitting or ignoring things you'd rather not discuss.
:   Your honesty is your greatest asset,
    and it's hypocritical to criticize your opponents for spin or selective reporting if you're doing it too,

Don't sign any agreement that might prevent you from speaking about moral or legal concerns,
:   or make sure the agreement explicitly excludes your concerns before signing it.
    (And yes, it's very privileged of me to be able to say this:
    someone whose immigration status, essential health benefits, or family income is being threatened
    may not have a choice.
    That is why I think people who do have a choice also have an obligation to fight.)

Don't cite the law unless your lawyer tells you to.
:   It probably doesn't mean what you think it means,
    and they almost certainly do have lawyers on their side
    who will seize on any mis-statement or mistake you make.

Don't try to get them to acknowledge that they were wrong.
:   This probably wouldn't have happened if they were the sort of people who could.

Go for long walks, cook some healthy meals, pick up the guitar you haven't touched in years,
:   or do anything else
    that requires you to focus on other things for a while.
    This isn't just for your mental health:
    exhausted people make poor decisions,
    and you need to be at the top of your game.

Remember that it's OK to cry,
:   because grief and anger are part of life too.

## Handing Over and Moving On

This advice is for founders who are handing on their projects;
see [this talk][wilson_carpentrycon] for more detail.

Be sure you mean it.
:   Letting go will be hard on you, but not letting go will be even harder on your
    successors, so be sure you're actually going to let go.

Do it when other people think you should.
:   Just as you are the last person to realize when you're too tired to be coding,
    you will often be the last person to realize that you ought to be moving on, so
    ask people and pay attention to what they say.

Be open about what, when, and why.
:   Tell people that you're leaving and what the succession plan is as soon as
    possible (which in practice means "as soon as you think you won't have to revise
    what you have said publicly").

Leave for something.
:   People who start things usually aren't good with idleness, and idleness tends
    not to be good for them, so when you leave, leave *for* something, even if it's
    something small.

Don't choose your successor on your own.
:   You may have strong opinions about who should succeed you, but you should still
    check those opinions with someone more objective.

Train your successor.
:   Share tasks with your successor for a few days or weeks: they will get to see
    how things actually work, and you'll discover things you would otherwise forget
    to tell them.  Go on holiday for a week and leave your successor temporarily in
    charge.  You'll discover even more things you would otherwise forget to pass on.

Celebrate.
:   Many people are uncomfortable being praised, but give the organization a chance
    to celebrate what you accomplished and thank you for it.

Leave.
:   It may be tempting to continue to have a role in the organization, but that
    usually leads to confusion, since people are used to looking to you for answers.
    It will be easier for your successor, particularly if they weren't a founder as
    well, but the best thing you can do to help them is to find something else to do
    for a year.

Learn from your mistakes.
:   Whatever you have left will almost certainly not be the last thing you ever do.
    Take some time to think about what you could have done differently, write it
    down, and then move on: obsessing over only-ifs and might-have-beens won't help
    anyone.

Do something before you go.
:   Everything comes to an end, but you have time before then to do something.  What
    are you waiting for?
