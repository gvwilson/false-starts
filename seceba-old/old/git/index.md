---
title: "Unfortunately, Git"
lede: "Using version control with other people"
template: page
---

[% i "version control!reasons to use" %]Version control[% /i %] is the
collective memory of the project. It's what lets you move files from one machine
to another without clobbering stuff you just spent three hours writing and
without worrying about whether you forgot something important.  It also lets you
undo your mistakes: if you spend an hour or two going down the wrong path, and
want to get back to where you were, version control lets you do it reliably with
a single command. And if all that wasn't enough, version control keeps track of
who did what so that you know who to turn to with questions.

Dozens of [% i "version control!systems" %]version control[% /i %] systems
exist. [% i "version control!CVS" "CVS (version control)" %][CVS][cvs][% /i %]
was the workhorse of the open source world for many years; it was replaced by
[% i "version control!Subversion" "Subversion (version
control)" %][Subversion][subversion][% /i %], which fixed many of its predecessor's
flaws while introducing a few minor ones of its own.
Both of these were [% i "version control!centralized" %][% g centralized_system %]centralized systems[% /g %][% /i %]:

1.  One [% i "version control!repository" "repository (version control)" %][% g repository %]repository[% /g %][% /i %]
    stored the definitive copy of the project's files.

1.  Nobody ever edited the contents of the main repository directly. Instead,
    everyone worked in a local copy.

1.  In order to share files with other people (or to create a backup, which is
    really just a way to share files with your future self) people would [% g push_git %]push[% /g %]
    the contents of their copy to the main repository.
    To get other people's work, they would [% g pull_git %]pull[% /g %]
    changes from the main repository and combine them with their own work.

Centralized version control systems have largely been replaced by
[% i "version control!decentralized" %][% g decentralized_system %]decentralized[% /g %][% /i %]
ones, and in particular by [% i "version control!Git" "Git" %][Git][git][% /i %].
In theory, Git doesn't need a main
repository: developers can merge the contents of any repository into any other.
In practice, almost every project designates one repository as the master copy
so that people know where to look to find the current state of the project.

Unfortunately, Git has a needlessly complicated interface.
[% b PerezDeRosso2013 %] found that even experienced users have
a [% i "mental model!Git" %][% g mental_model %]mental model[% /g %][% /i %] of how it works that
contradicts its actual operation in important ways, and each of those
contradictions produces a steady stream of "what the hell?"  moments. Other
distributed version control systems like [% i "version control!Mercurial" "Mercurial (version control)" %][Mercurial][mercurial][% /i %]
are proof that this
complexity and pain are unnecessary.  The fact that most people don't
immediately realize that [the random Git manual page
generator][git-man-page-generator] is a [% i "Git!interface
(indistinguishable from hoax)" %]hoax[% /i %] says a lot as well.

So why do people keep using [% i "Git!reasons for popularity" %]Git[% /i %]? The
answer these days is, "Because it's the tax they have to pay in order to use
[GitHub][github]." At the time of writing, GitHub has over 40 million users and
hosts over 28 million public repositories, including those for many well-known
open source projects. It is easily the most popular
[% i "software portal!GitHub" %][% g software_portal %]software portal[% /g %][% /i %] in existence, and
offers all of the tools a small software team needs. Other portals exist, such
as [% i "Bitbucket" "software portal!Bitbucket" %][Bitbucket][bitbucket][% /i %]
and [% i "GitLab" "software portal!GitLab" %][GitLab][gitlab][% /i %], but
GitHub's share of the educational market is even larger than its share
among professional developers.  If you're using anything in class, you're almost
certainly using it, and it's probably helping you become a better programmer
[% b Hsing2019 %].

<blockquote markdown="1">
### Why can't we fix it?

If Git's interface is a problem, why can't we build a new one?
[% b PerezDeRosso2016 %] tried, but as they report, the gravity of the
existing interface is simply too powerful: as soon as people run into a problem
and start searching online for solutions, they're thrown back into the world of
original Git.
</blockquote>

This chapter won't try to teach you Git from scratch: [GitHub's
guides][github-guides] and [the Atlassian Git tutorial][atlassian-git] do an
excellent job of that, as does [the Carpentries lesson on Git][carpentries-git].
Instead, we will FIXME.
We will show the commands as if you were running them in the Unix shell, but we
recommend that you use a [% i "Git!graphical interface" %]graphical
interface[% /i %] like [GitKraken][gitkraken], [SourceTree][sourcetree], or the
one that comes with your [% i "IDE" %]IDE[% /i %]. These
are layered on top of the commands we are going to discuss, so they (should) all
work the same way.

## A Review of the Basics

When I am working on a solo project or in a small team, [% i "Git!basic
commands" %]seven commands[% /i %] account for roughly 85% of my Git
activity. Adding two more commands to set things up produces a toolkit that uses
Git as a file backup system.

The first step is to make sure that [% i "Git!configuring" %]Git knows who
we[% /i %] are by telling it our name and email address:

```sh
$ git config --global user.name "Peggy Springsteen"
$ git config --global user.email "peggy@wolframhart.org"
```

Breaking this down:

-   Git commands are written as <code>git <em>verb</em></code>, where
    <code><em>verb</em></code> is a sub-command telling Git exactly what we want
    to do.

-   The `--global` option is used to specify a value for the command in the same
    way that parameters are used to pass values to functions. In this case,
    we're telling Git that we want to configure things globally (i.e., for every
    project we have on this computer). We can also configure things
    repository-by-repository if we want to have a different name or email
    address for different projects.

-   `user.name` is the thing we want to configure. There are a lot of these;
    `git config --list` displays them all.

-   Finally, we specify the values we want `user.name` and `user.email` to
    have. We wrap these in quotes because they contain spaces and the `@`
    symbol, which might otherwise confuse the shell.

Now that Git knows who we are, let's [% i "Git!creating project" %]set up a
project[% /i %].  If we are starting from scratch, we create a directory, go into
it, and run `git init`. This may or may not print out some messages depending on
what version of Git you have and how much of its output your GUI shows (if
you're using one). Either way, this command creates a sub-directory called
`.git` inside your project directory. That special sub-directory is what makes
something a project: it stores the data Git uses to keep track of what files you
have and how they've changed.

<blockquote markdown="1">
### Don't mess

Don't edit the files in your `.git` directory yourself—it will have the same
unfortunate effect as editing a spreadsheet or an image as if it was a text
file. If you'd like to know more about what they're for and how Git uses them,
please see [% b Chacon2014 %] or [% b Cook2019 %].
</blockquote>

If your instructor or one of your teammates has already created a project, you
won't use `git init`. Instead, you will use `git clone` followed by the
project's URL to get a local copy called a [% i "Git!cloning project" %][% g clone_git %]clone[% /g %][% /i %].
For example, if you want a clone of this book, you can do
this:

```sh
$ git clone https://github.com/gvwilson/buildtogether.tech.git
```

This will create a directory with the same name as the project, create a `.git`
sub-directory inside it, and download the project's history so that you can
start work.

Regardless of how you create your repository, you can use `git log` to look at
its [% i "Git!history" %]history[% /i %]. If I run this command right now for
this book, I get:

```sh
$ git log
```
```out
commit d4351c4f093f60d03f303737b66b28ebb6b9ed45
Author: Greg Wilson <gvwilson@third-bit.com>
Date:   Fri Feb 19 09:48:37 2021 -0500

    Writing the first section of the chapter on version control.

commit 80d38a8cbf650431fe4719ec768bd890e00c7431
Author: Greg Wilson <gvwilson@third-bit.com>
Date:   Thu Feb 18 11:21:00 2021 -0500

    Adding more citations to the description of team formation.

commit 6e30bd5e5af2c3491f25f014c03d5e9ff5c79879
Author: Greg Wilson <gvwilson@third-bit.com>
Date:   Wed Feb 17 20:48:04 2021 -0500

    Moving the discussion of code review into its own chapter.

...
```

Each entry has:

-   A line labeled `commit` followed by a large hexadecimal number.  This number
    is a unique [% i "Git!commit ID" %]label[% /i %] for the state of the
    project's files at that point in time.  if we want to refer to a particular
    version of our project, we can use this or its first half-dozen digits (such
    as `6e30bd`) so long as the latter is unambiguous.

-   Two lines showing who saved the state of the project and when. The name and
    email address in the `Author` field are the ones we set up with `git
    config`; the [% i "timestamp!of Git commit" %][% g timestamp %]timestamp[% /g %][% /i %] is accurate to the second, and includes time zone
    information like the `-0500` showing that I'm in Eastern time so that anyone
    in the world can tell exactly when these files were saved.

-   A short comment called a [% i "commit message (version control)" "Git!commit message" %][% g commit_message %]commit message[% /g %][% /i %] that tells us what this
    change is all about. We will at these below; for now, just remember that if you and your
    teammates have made a hundred changes to the project over the course of ten
    or twelve weeks, you're going to want something more informative than "Fixed
    stuff."

All right: what are [% i "commit (version control)" "Git!commit" %][% g commit %]commits[% /g %][% /i %] and where do they come from? A commit is a snapshot
of the project at a particular moment in time; we create them using a command
like:

```sh
$ git commit -m "Made the status bar display the user name"
```

Here, `commit` is the verb and the `-m` (short for "message") option is followed
by the comment we want to save in the log.

<blockquote markdown="1">
### The most popular question on Stack Overflow

If you use Git on the command line and you *don't* provide a message using the
`-m` option, it will launch an editor so that you can write a longer message.
This is a good thing, except that the default editor on most Unix systems is
something called [% i "Vim editor!exiting" %]Vim[% /i %], whose interface is no
more intuitive than Git's. (In fact, one of the most frequently-viewed questions
on [Stack Overflow][stack-overflow] is "[How do I exit the Vim
editor?][so-exit-vim]". Unsurprisingly, another
[% i "Git!configuring" %]frequently-viewed question[% /i %] on Stack Overflow is
"[How do I make Git use the editor of my choice for my commits?][so-configure-git-editor]"
One of the many reasons you should interact with Git through a GUI is to avoid this issue.
</blockquote>

Before we run `git commit`, though, we need to tell Git which files we want to
save in the commit, which we do using `git add`:

```sh
$ git add version-control.md _data/glossary.yml
```

[% i "Git!difference between add and commit" %]One way to think about
this[% /i %] is that `git add` puts things in a box to be shipped, while `git
commit` actually sends the package. Git requires us to do this in two steps
because we might change our mind about what we want to store: for example, we
might `git add` a file, then realize we need to make a few more edits, `git add`
it again, and then `git commit`. Alternatively, we might add a bunch of files,
then realize that some of them (like editor backup files or temporary files
created by the compiler) shouldn't be saved, so we take them out before
committing.

<blockquote markdown="1">
### Teach us to care and not to care

You can tell Git to [% i "Git!ignoring files" %]ignore certain kinds of
files[% /i %] by putting their names, or patterns that match multiple names, in a
file called `.gitignore`.  For example, the `.gitignore` file for this project
includes:

```txt
*.pyc
*~
.DS_Store
.jekyll-cache
.jekyll-metadata
.sass-cache
__pycache__
_site
```

Be careful not to put files containing passwords or [% g api_key %]API
keys[% /g %] for web services into version control: even if the repository is
private now, it might be public in future, or the team might grow to include
someone who shouldn't have access.
</blockquote>

We can keep track of which changes haven't yet been added and which ones have
using [% i "Git!showing status" %]`git status`[% /i %]. If I run this command
right now in this book's project I get:

```sh
$ git status
```
```out
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   _includes/links.md
	modified:   bibliography.md
	modified:   version-control.md

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   version-control.md
```

The first paragraph titled "Changes to be committed" tells me which files I have
asked Git to save using `git add`. The second paragraph, "Changes not staged for
commit", shows that I have modified `version-control.md` (this chapter) since I
last asked Git to save a snapshot. Both paragraphs tell me that I can use `git
restore` with or without the `--staged` option to put a file back the way it was
if I decide I don't want to save the changes I've made.

I can use [% i "Git!recovering old files" %]`git restore`[% /i %] to recover an
old version of a file from any previous commit. Being able to do this was the
original motivation for version control systems, and is still one of the main
reasons people use them. For example, if I want to get the version of this file
from two days ago, I can use `git log` to find the commit ID `2be70844`, and
then run:

```sh
$ git restore --source 2be70844 version-control.md
```

I can also count backward from where I am now.  The most recent commit has the
special [% i "Git!HEAD" %]symbolic name `HEAD`[% /i %]; the expression `HEAD~1`
means "the one before it", while `HEAD~2` goes back two commits and so
on. Regardless of how I specify what I want, restoring an old version doesn't
erase any of the ones I have saved since then: the project's history stays
intact.

Finally, I should make sure there's a second physical copy of my work so that if
my drive fails or my laptop is stolen I don't lose everything I've done. If I
created the repository by cloning something on GitHub, then Git will
automatically have created a bookmark called a
[% i "Git!remote" "remote (in Git)" %][% g remote_git %]remote[% /g %][% /i %] that points
at the original repository. I can get a list of remotes like this:

```sh
$ git remote -v
```
```out
origin	https://github.com/gvwilson/buildtogether.tech.git (fetch)
origin	https://github.com/gvwilson/buildtogether.tech.git (push)
```

The `-v` option (short for "verbose") tells Git to print more than just the
remote's name. The remote itself is called `origin`, and Git lists two URLs for
it because in theory you can download (or "fetch") from one and upload (or
"push") to another. (I have been using Git for sixteen years, and have never
once needed this feature.)

One of the differences between a version control system like Git and a file
backup tool like [Dropbox][dropbox] is that Git *doesn't* automatically
synchronize local changes to the remote repository.  If I want to [% i "Git!saving changes remotely" %]save[% /i %] everything I've done locally on
GitHub, I have to push them explicitly:

```sh
$ git push origin main
```

The verb is `push`; the word `origin` identifies where I want to send things,
and the word `main` identifies the branch I'm on.  We'll discuss branches in the
next section, but for now, you can run `git branch` to see which ones you have
and which one you're working in.

The counterpart of `git push` is `git pull`. It downloads changes from the
remote repository and merges them into your local copy:

```sh
$ git pull origin main
```

Pushing and pulling changes allows you and your teammates to synchronize your
work. They're also very useful operations if you're working on your own and
using two or more computers (such as a personal laptop and your school's
servers).

<blockquote markdown="1">
### Clean and build

Many instructors require learners to submit work by committing it to a Git
repository. One way to check that what works for you will work for whoever is
grading it is to clone a fresh copy of the project in a temporary directory and
make sure that everything builds and runs there. Doing that will tell you if you
or one of your teammates has forgotten to commit a key file. In an advanced
course, you might be asked to do this automatically every time someone commits
changes.
</blockquote>

## A Branch-Based Workflow

So far we have only used a sequential timeline with Git: each change builds on
the one before, and *only* on the one before.  However, there are times when we
want to work on several things at once.  To do this, we can use
[% i "branch (in Git)" "Git!branch" %][% g branch_git %]branches[% /g %][% /i %] to work on
separate tasks in parallel.  Each branch is like a parallel timeline: changes made
to one branch have no effect on other branches unless and until we explicitly merge
them.

We can see what branches exist in a repository like this:

```sh
$ git branch
```
```out
* main
```

When we initialize a repository, Git automatically creates a branch called
`master`; most people now rename this to `main` by running:

```sh
$ git branch -m main
```

immediately after running `git init`.  The [% i "Git!branch names" %]`main`
branch[% /i %] is usually considered the "official" version of the repository,
i.e., the version of the project that should be graded or published for other
people to use.  The asterisk `*` indicates that it is currently active, i.e.,
that all changes we make will take place in this branch by default.

To create a new branch called `homework3` we run:

```sh
$ git branch homework3
```

The name of the branch should indicate what it's for, just like the names of
files and variables.  We can check that the branch exists by running `git
branch` again:

```sh
$ git branch
```
```out
* main
  homework3
```

Our branch is there, but the `*` shows that we are still in the `main` branch.
To switch to our new branch we use the `checkout` command:

```sh
$ git checkout homework3
$ git branch
```
```out
  main
* homework3
```

We haven't made any changes since switching to the `homework3` branch, so at
this point `main` and `homework3` are at the same point in the repository's
history.  Commands like `ls` and `git log` therefore show that the files and
history haven't changed.

<blockquote markdown="1">
### Where branches are saved

Git saves every version of every file in the repository's `.git` directory.
When we switch from one branch to another, it copies files out of there and
rearranges directories to restore that state of the world.
</blockquote>

Why go to all this trouble?  Because it allows us to work on several things at
once without stepping on our own toes, just as putting variables inside objects
and classes allows us to ignore the details of *this* when we're working on
*that*. For example, if we are close to finishing homework 3 but want to get an
early start on homework 4, we can create a new branch from `main` called
`homework4` and start setting things up in there.

When we are done, we can [% i "merge (in Git)" "Git!merge" %][% g merge_git %]merge[% /g %][% /i %] the state of one branch back into another. Merging
doesn't change the source branch, but once it's done, all of the changes made
there are in the destination branch.

To see what the differences are between two branches, we use [% i "Git!viewing differences" %]`git diff`[% /i %] with those branches' names:

```sh
$ git diff homework3..main
```

More generally, we can use `git diff` to compare any two states of the
repository, including old versions with current ones:

```sh
$ git diff HEAD~3..HEAD
```
```txt
diff --git a/bin/html2tex.py b/bin/html2tex.py
index 4c756f4..10efe1c 100755
--- a/bin/html2tex.py
+++ b/bin/html2tex.py
@@ -35,10 +35,13 @@ def html2tex(options):
     '''Main driver.'''
     update_numbering(options.numbering)
     config = utils.read_yaml(options.config)
-    filenames = get_filenames(options.site, config)
+    entries = get_filenames(options.site, config)
     accum = []
-    for f in filenames:
-        convert_file(f, accum)
+    for [kind, filename] in entries:
+        if kind == 'entry':
+            convert_file(filename, accum)
+        elif kind == 'appendix':
+            accum.append('\n\\appendix\n')
     result = ''.join(accum)
     display(options, config, result)
```

The output marks additions with a `+` and deletions with a `-`. A line that has
changed is shown as a deletion followed by an addition, and the lines marked
with `@@` show where in the file the change occurred.

<blockquote markdown="1">
### See the difference

You have to be a bit of a masochist to read diffs like this; it's a lot easier
using a [% i "Git!graphical interface" %]GUI[% /i %] like
[DiffMerge][diffmerge].  You can [use other tools to view diffs][git-difftool]
between files that aren't plain text, but only if such tools exist. They don't
for many common file formats: for example, there isn't an easy way to see the
differences between two version of an SVG diagram or between two spreadsheets.
If you are looking for projects to work on that people will actually use, these
would be good ones.
</blockquote>

Once we're sure we actually want to merge changes, we do so like this:

```sh
$ git merge homework3 main
```

Git automatically creates a new commit to represent the merge.  If we now run
`git diff main..homework3`, Git doesn't print anything because there aren't any
differences to show.

After we merge the changes from `homework3` into `main` there is no need to keep
the `homework3` branch, so we can delete it:

```sh
$ git branch -d homework3
```
```out
Deleted branch homework3 (was 1577404).
```

Merging `homework3` into `main` went smoothly, but if we are going to use
branches, we must learn how to merge [% i "conflict (in Git)" "Git!conflict" %][% g conflict_git %]conflicts[% /g %][% /i %].  These occur when a line has been changed
in different ways in two branches or when a file has been deleted in one branch
but edited in the other.

If the file `README.md` has been changed in both `main` and `homework4`,
`git diff` will show the conflict:

```sh
$ git diff homework4..main
```

When we try to merge `homework4` into `main`, Git doesn't know which of these
changes to keep:

```sh
$ git merge homework4 main
```

After we run this command, Git has put both sets of changes into `README.md`,
but has marked which came from where:

```sh
$ cat README.md
```

The lines from `<<<<<<< HEAD` to `=======` are what was in `main`, while the
lines from there to `>>>>>>> docs` show what was in `homework4`.  If there were
several conflicting regions in the same file, Git would mark each one this way.
Once again, you have to hate yourself a little to view these conflicts as raw
text files; even legacy text editors like [Emacs][emacs] will highlight them,
and Git GUIs will help you view and edit these regions.

We have to decide what to do next: keep the `main` changes, keep those from
`homework4`, edit this part of the file to combine them, or write something new.
Whatever we do, we must remove the `>>>`, `===`, and `<<<` markers.  Once we are
done, we can add the file and commit the change like we would any other edit:

```sh
$ git add README.md
$ git commit -m "Merging README additions"
```

Our branch's history will now show a single sequence of commits with the `main`
changes on top of the earlier `homework4` changes:

```sh
$ git log --oneline -n 4
```

If we want to see what happened, we can add the `--graph` option to `git log`:

```sh
$ git log --oneline --graph -n 4
```

At this point we can delete the `homework` branch or switch back to it and do
some more work.  Each time we switch to it, we merge changes *from* `main`
*into* `homework4`, do our editing (while switching back to `main` or other
branches as needed to work on the code), and then merge *from* `homework4` *to*
`main` once the documentation is updated.

<blockquote markdown="1">
### Rebasing

One way to make the history of a repository easier to read is to squash several
consecutive commits into one.  This is called
[% i "Git!rebase; rebasing (in version control)" %][% g "rebase_git" %]rebasing[% /g %][% /i %],
and can be done using:

```sh
$ git rebase -i START
```

where `START` identifies the commit *before* the ones you want to start merging
(i.e., the last one *not* to modify). Rebasing can go wrong in a lot of
confusing ways, particularly if you have merged changes from another branch into
the one you're squashing, so we recommend that you avoid it for schoolwork.
</blockquote>

Branches can be confused, but this [% i "Git!workflow" "workflow (in
Git)" %]workflow[% /i %] will help you keep track of what you are doing:

1.  `git checkout main` to make sure you are in the `main` branch.

2.  `git checkout -b name-of-feature` to create a new branch.  *Always* create a
    branch when making changes, since you never know what else might come up.
    The branch name should be as descriptive as a variable name or filename
    would be.

3.  Make your changes.  If something occurs to you along the way—for example,
    if we are writing a new function and realize that the documentation for some
    other function should be updated—*don't* do that work in this branch.
    Instead, commit our changes, switch back to `main`, and create a new branch
    for the other work.

4.  When the new feature is complete, use `git merge` to get any changes you
    merged into `main` after creating `name-of-feature` and resolve any
    conflicts.  This is an important step: you want to test that everything
    works while you are in your feature branch, not in `main`.

5.  Finally, switch back to `main` and `git merge name-of-feature main` to merge
    your changes into `main`.  You should not have any conflicts, and all of
    your tests should pass.

Most developers use this [% g branch_per_feature_workflow %]branch-per-feature workflow[% /g %], but what
exactly is a "feature"?  These rules make sense for small projects:

1.  Anything cosmetic that is only one or two lines long can be done in `main`
    and committed right away.  "Cosmetic" means changes to comments or
    documentation: nothing that affects how code runs, not even a simple
    variable renaming.

2.  A pure addition that doesn't change anything else is a feature and goes into
    a branch.  For example, if you are adding a feature to the user interfaces,
    that should be done on its own branch because it might take several tries to
    get right, and you might interrupt yourself to fix things you discover along
    the way.

3.  Every bug fix is also done in a separate branch

The hardest thing about using a branch-per-feature workflow is sticking to it
for small changes.  As the first point in the list above suggests, most people
are pragmatic about this on small projects; on large ones, where dozens of
people might be committing, even the smallest and most innocuous change needs to
be in its own branch so that it can be reviewed (which we discuss below).

## Teams

[% i "version control!collaboration" %]Version control[% /i %] really comes into
its own when we are working with other people.  People can share work through a
Git repository in one of two ways [% b Irving2021 %]:

1.  Everyone has read and write access to a [% i "version
    control!using a shared repository" %]single shared
    repository[% /i %].

2.  Everyone can read from the project's main repository, but only a few people
    can commit changes to it.  The project's other contributors
    [% i "version control!using forked repositories" %][% g fork_git %]fork[% /g %][% /i %]
    the main repository to create one that they own,
    do their work in that, and then submit their changes to the main repository.

The first approach works well for teams of up to half a dozen people, so we will
focus on it. If the project is larger, or if contributors are worried that they
might make a mess in the `main` branch, the second approach is safer.

<blockquote markdown="1">
### When to commit

When you're working on your own, it's natural to fall into a rhythm of updating
your laptop from your repository in the morning and committing whatever you've
managed to accomplish when you wrap up for the day. You need to break this habit
when you become part of a team. Instead, [% i "version control!when to
commit" %]you should commit[% /i %] when you finish a chunk of work that moves the
project forward or is fit for someone else to review. A good rule is "never
break the build", i.e., never commit anything that
doesn't run well enough to pass all existing tests.
</blockquote>

Suppose Amira and Sami are working together on a course.  They decided at the
start of semester that Sami would host the project repository in her GitHub
account, so they created `https://github.com/sami/bst` and gave Amira permission
to push to it. They have both cloned that repository to their laptops to start
work on homework 5.

We will modify Amira's prompt to include her desktop user ID (`amira`) and
working directory (initially `~`, meaning "home directory") to make it easier to
follow what's happening.  First, she updates her desktop repository to make sure
she is starting with the most recent set of files:

```sh
amira:~ $ cd bst
amira:~/bst $ git pull origin main
amira:~/bst $ ls
```
```out
LICENSE.md   README.md    hw1/    hw2/    hw3/    hw4/
```

Amira creates a new directory for homework 5 and adds a copy of the assignment spec:

```sh
amira:~/bst $ mkdir hw5
amira:~/bst $ cd hw5
amira:~/bst $ cp ~/Downloads/Assignment5.txt hw5/spec.txt
amira:~/bst $ git add .
amira:~/bst $ git commit -m "Adding homework 5 spec"
```
```out
[main f5f7d30] Adding homework 5 spec
 1 files changed, 132 insertions(+)
```

She then pushes her changes to the shared repository:

```sh
amira:~/bst $ git push origin main
```
```out
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 4 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (4/4), 485 bytes | 485.00 KiB/s, done.
Total 4 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To github.com:sami/bst.git
   f5f7d30..433a2d5  main -> main
```

And no, [% i "Git!interface (indistinguishable from hoax)" %]Git's
output[% /i %] here isn't particularly useful to anyone except people who are
debugging Git's internals.

Amira's changes are now on her desktop computer and in the GitHub repository but
not on Sami's laptop. They can get them by running:

```sh
sami:~/bst $ git pull origin main
```

But what if Sami is working on some changes to homework 4 (which homework 5
builds on)? She could just make her changes and push, but that would lead to a
lot of merge conflicts.  Instead, almost everyone uses
[% i "pull request" "Git!pull request" %][% g pull_request %]pull requests[% /g %][% /i %] (PR).
A PR is essentially a note saying, "Someone would like to merge branch A into branch B".
The PR does not contain the changes, but instead points at two particular
branches.  That way, the difference displayed is always up to date if either
branch changes.

But a PR can store more than just the source and destination branches: it can
also store [% i "Git!comments" %]comments[% /i %] people have made
about the proposed merge.  Users can comment on the PR as a whole, or on
particular lines, and mark comments as out of date if the author of the PR
updates the code that the comment is attached to.  Complex changes can go
through several rounds of review and revision before being merged, which makes
PRs the review system we all wish journals actually had.

To see this in action, suppose Sami wants to add their email address to
`README.md`.  They create a new branch and switch to it:

```sh
sami:~/bst $ git checkout -b adding-email
```

then make a change and commit it:

```sh
sami:~/bst $ git commit -a -m "Adding my email address"
```

(Notice that Sami uses the `-a` option to `git commit` to add all changes and
commit them in a single step. This is both convenient and dangerous.)

Sami's changes are only in their local repository.  They cannot create a pull
request until those changes are on GitHub, so they push their new branch to
their repository on GitHub:

```sh
sami:~/bst $ git push origin adding-email
```

When Sami views their repository in the browser, GitHub notices that they have
just pushed a new branch and asks them if they want to create a PR.  When they
click on the button, GitHub displays a page showing the default source and
destination of the PR and a pair of editable boxes for the pull request's title
and a longer comment.

If they scroll down, Sami can see a summary of the changes that will be in the
PR.  When they click "Create Pull Request", Git gives it a unique [% i "pull
request!serial number" %]serial number[% /i %].  This is *not* a commit ID;
instead, each PR in a particular repository is given a sequential ID.

Clicking on the "Pull requests" tab in the repository brings up a list of PRs
and clicking on the PR link itself displays its details.  Since there are no
conflicts in this PR, GitHub will let Sami or Amira merge it immediately using
the "Merge pull request" button.  They could also discard or reject it without
merging using the "Close pull request" button.

But instead, the next time Amira has a few minutes to work on the assignment she
clicks the "Files changed" tab in the PR to see what Sami has changed. She can
review the changes line-by-line and suggest changes; we'll discuss this more in
the next section. Once they are both happy with the changes, either of them can
merge the PR into the main branch. They can both then update their local copies
and be sure that they are synchronized.

If there are any conflicts along the way, Sami and Amira can resolve them just
as they would resolve conflicts between branches in a single repository.  GitHub
and other portals do allow people to merge conflicts through their browser-based
interfaces, but doing it on our desktop means we can use our favorite editor to
resolve the conflict.  It also means that if the change affects the project's
code, we can run everything to make sure it still works.

But what if Sami merges another PR while Amira is resolving this one?  In theory
this [% i "conflict (in Git)!repeating" %]cycle[% /i %] could go on forever; in
practice, it reveals a communication problem that the team needs to address.  If
two or more people are constantly making incompatible changes to the same files,
they should discuss who's supposed to be doing what, or rearrange the project's
contents so that they aren't stepping on each other's toes.

<blockquote markdown="1">
### Trust but verify

[% x automation %] describes how to configure Git to run tests each time
someone tries to commit a change.  The commit only takes effect if those tests
pass, so the team can ensure that the software is always as good as its tests.
</blockquote>

## Commit Messages

A [DuckDuckGo][duckduckgo] search for "how to write a good [% i "Git!commit
message" %]commit message[% /i %]" turns up several thousand articles. Most are
variations on the sample shown below; as with programming style,
the most important thing is being consistent rather than the
particular rules you follow.

```txt
One-line summary

Detailed explanatory text separated from the summary by a blank line.  (If you
do this, many tools will treat the first line like the subject of an email and
the rest of the text as the body.)

Be brief but specific and write your message in the imperative voice, i.e.,
"Handle indentation in configuration files correctly" rather than "Config file
indentation."

- Bullet points are OK (GitHub will format them as a list).  Some other Markdown
  conventions work too.

If this commit fixes an open issue, refer to it like as shown below. GitHub
automatically turns things like `#123` into links.

Closes: #123
```

The most important thing to remember when writing a commit message is that its
purpose is to make work easier to find and understand in the future. You
shouldn't transcribe large chunks of code or duplicate whatever documentation or
tests you wrote for the feature you added; instead, you should give people
enough information to figure out whether this is the commit they're looking for
or not.
