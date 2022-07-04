---
title: "Code Reviews"
lede: "Learning from teammates while giving them feedback"
template: page
---

There's no point creating PRs if they are all merged as-is. The reason they
exist is to allow [% i "code review!effectiveness of" %][% g code_review %]code review[% /g %][% /i %].
One study after another since the mid-1970s has proven that code
review is the most cost-effective way to find bugs in software
[% b Cohen2010 %]. It is also the most effective way to share knowledge
between team members: if you read someone else's code, you have a chance to
learn all the things that you didn't know to ask and they didn't realize they
should tell you.

<blockquote markdown="1">
### Do more eyes make for fewer bugs?

Some people have claimed that many eyes make all bugs shallow (i.e., easy to
find), but the evidence doesn't support that claim: [% b Meneely2014 %]
reports that, "…source code files reviewed by more developers are,
counter-intuitively, more likely to be vulnerable (even after accounting for
file size). However, files are less likely to be vulnerable if they were
reviewed by developers who had experience participating on prior
vulnerability-fixing reviews." In short, *whose* eyes matters more than how
many.
</blockquote>

There are lots of guides online for doing code reviews, most of them based on
their authors' personal experience. A notable exception is the [SmartBear
guide][smartbear-code-review], which draws on a large study of code review in
industry. The [% i "code review!procedure" %]rules below[% /i %] present some of
their findings with modifications for students' situations.

Have the instructor do a demonstration review.
:   Even if you have done code reviews before, you may not know what's expected
    for this class. The instructor can show you by putting up some sample code
    and going through it, thinking aloud as they notice things worth commenting
    on so that you have an idea of how much detail they expected.

Authors should clean up code before review.
:   If the person creating the PR goes through and adds some more comments,
    cleans up some variable names, and does a bit of [% i "refactoring!for
    code review" %]refactoring[% /i %] ([% x design %]), they won't just make
    reviewing easier: the odds are very good that they will find and fix a few
    problems on their own.

Review at most 200 lines of a code at a time.
:   The SmartBear guide recommends reviewing at most 400 lines at a time, which
    should take 60--90 minutes. You will probably get there eventually, but in
    our experience it's better to start with something smaller and work up to
    that.  A corollary of this rule is that no PR should be more than 200 lines
    long.  If one is, the odds are that reviewers won't be able to hold it all
    in their head at once ([% x thinking %]) and so will miss things.

Use checklists.
:   [% b Gawande2011 %] popularized the idea that using
    [% i "checklists!use in code review" %]checklists[% /i %] improves results even
    for experts.  While [% b Hatton2008 %] found no evidence that they made
    a difference to code reviews by professionals, I have found them very useful
    as a starter for students.  If you are new to code reviews, ask the
    instructor for a list of the dozen most common problems to check for, since
    anything more than that is likely to be overwhelming.  (The code quality
    rubric developed in [% b Stegeman2014 Stegeman2016 %] is a good
    starting point.)  If you and your teammates have been working together for a
    while, look at your own code reviews and make a list of the things that keep
    coming up.  Having the list will make you more aware of the issues while
    you're coding, which in turn will make you less likely to keep making the
    same mistakes.

Look for algorithmic problems first.
:   Code review isn't just (or even primarily) about style: its real purpose is
    to find bugs before they can affect anyone.  The first pass over any change
    should therefore look for algorithmic problems.  Are the calculations right?
    Are any rare cases going to be missed?  Are errors being caught and handled?
    Using a consistent style helps reviewers focus on these issues.

Offer alternatives.
:   Telling authors that something is wrong is helpful; telling them what they
    might do instead is more so.

Don't [% g feigning_surprise %]feign surprise[% /g %] or pass judgment.
:   "Gosh, didn't you know [some obscure fact]?" isn't helpful; neither is,
    "Geez, why don't you [some clever trick] here?"

Don't overwhelm people with details.
:   If someone has used the letter `x` as a variable name in several places, and
    they shouldn't have, comment on the first two or three and simply put a
    check beside the others—the reader won't need the comment repeated.

Don't try to sneak in feature requests.
:   Nobody enjoys fixing bugs and style violations.  Asking them to add entirely
    new functionality while they're at it is rude.

Follow up.
:   The author of the code doesn't have to accept every suggestion, but should
    have a better reason than "I don't want to" for rejecting any of them.
    GitHub and other platforms allow people to create discussion threads for
    each comment, and will mark threads as being out of date when the pull
    request is updated. Whoever did the review should then scan the changes to
    make sure their points have been addressed, and to give themselves a chance
    to learn a few more things from the author.

Don't tolerate rudeness.
:   Most code review guidelines say, "Be respectful."  The problem is that if
    you are, you probably don't need to be told that, and if you aren't, those
    two works alone won't change your behavior. What *will* is teammates
    defending the victims of rudeness by telling the offender, "That's not how
    we speak to each other."

How we [% i "code review!responding to" %]respond[% /i %] to reviews is just as
important:

Be specific in replies to reviewers.
:   If someone has suggested a better variable name, you can probably simply fix
    it.  If someone has suggested a major overhaul to an algorithm, you should
    reply to their comment to point at the commit that includes the fix.

Thank your reviewers.
:   If someone has taken the time to read your code carefully, thank them for
    doing it.

So what does a code review actually look like? Here's a Python program that
searches for duplicated files. [% t collaborate-code-review %] shows the
comments I left when reviewing it.

[% excerpt file="dup.py" %]

<div class="table" id="collaborate-code-review" caption="Code Review" markdown="1">
| Line(s) | Comment |
| ------- | ------- |
| 02      | Add a [% g docstring %]docstring[% /g %] describing the program. |
| 03      | Put imports in alphabetical order. |
| 07      | Use a set instead of a list for faster lookup. |
|         | One entry per line will be easier to read. |
| 09      | `SENSES` isn't used anywhere: delete. |
| 12      | Add a docstring describing this function. |
| 12-22   | Use `argparse` to handle options. |
| 12-22   | Put option handling in its own function. |
| 17      | Print error message to `sys.stderr`. |
| 33      | Add a docstring describing this function. |
| 34-39   | Use `any` instead of a loop to check this. |
| 41      | [% g magic_number %]Magic number[% /g %] 10. |
| 41      | Provide option to control progress reporting. |
| 47      | Use `'rb'` to read files as binary. |
| 57      | Add a docstring describing this function. |
| 60      | Why `paths.pop()`? |
</div>
