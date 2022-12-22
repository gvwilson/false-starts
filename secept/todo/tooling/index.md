---
title: "Tooling"
syllabus:
- FIXME
---

FIXME: cut Git material in half

## Version Control {: #development-versioning}

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
Both of these were [% i "version control!centralized" %][% g centralized_system "centralized systems" %][% /i %]:

1.  One [% i "version control!repository" "repository (version control)" %][% g repository "repository" %][% /i %]
    stored the definitive copy of the project's files.

1.  Nobody ever edited the contents of the main repository directly. Instead,
    everyone worked in a local copy.

1.  In order to share files with other people (or to create a backup, which is
    really just a way to share files with your future self) people would [% g push_git "push" %]
    the contents of their copy to the main repository.
    To get other people's work, they would [% g pull_git "pull" %]
    changes from the main repository and combine them with their own work.

Centralized version control systems have largely been replaced by
[% i "version control!decentralized" %][% g decentralized_system "decentralized" %][% /i %]
ones, and in particular by [% i "version control!Git" "Git" %][Git][git][% /i %].
In theory, Git doesn't need a main
repository: developers can merge the contents of any repository into any other.
In practice, almost every project designates one repository as the master copy
so that people know where to look to find the current state of the project.

Unfortunately, Git has a needlessly complicated interface.
[% b PerezDeRosso2013 %] found that even experienced users have
a [% i "mental model!Git" %][% g mental_model "mental model" %][% /i %] of how it works that
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
[% i "software portal!GitHub" %][% g software_portal "software portal" %][% /i %] in existence, and
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
Instead, we will review the basics that we hope you have learned previously,
then look at how to use Git and GitHub to collaborate.
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
project's URL to get a local copy called a [% i "Git!cloning project" %][% g clone_git "clone" %][% /i %].
For example, if you want a clone of this book, you can do
this:

```sh
$ git clone https://github.com/gvwilson/buildtogether.tech.git
```

<!-- continue -->
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
    config`; the [% i "timestamp!of Git commit" %][% g timestamp "timestamp" %][% /i %] is accurate to the second, and includes time zone
    information like the `-0500` showing that I'm in Eastern time so that anyone
    in the world can tell exactly when these files were saved.

-   A short comment called a [% i "commit message (version control)" "Git!commit message" %][% g commit_message "commit message" %][% /i %] that tells us what this
    change is all about. We will take a look later at how to
    write a good commit message; for now, just remember that if you and your
    teammates have made a hundred changes to the project over the course of ten
    or twelve weeks, you're going to want something more informative than "Fixed
    stuff."

All right: what are [% i "commit (version control)" "Git!commit" %][% g commit "commits" %][% /i %] and where do they come from? A commit is a snapshot
of the project at a particular moment in time; we create them using a command
like:

```sh
$ git commit -m "Made the status bar display the user name"
```

<!-- continue -->
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

<!-- continue -->
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

Be careful not to put files containing passwords or [% g api_key "API keys" %]
for web services into version control: even if the repository is
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

<!-- continue -->
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

<!-- continue -->
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
[% i "Git!remote" "remote (in Git)" %][% g remote_git "remote" %][% /i %] that points
at the original repository. I can get a list of remotes like this:

```sh
$ git remote -v
```
```out
origin	https://github.com/gvwilson/buildtogether.tech.git (fetch)
origin	https://github.com/gvwilson/buildtogether.tech.git (push)
```

<!-- continue -->
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

<!-- continue -->
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
changes; we'll explore this in [% x automation %].
</blockquote>

## A Branch-Based Workflow

So far we have only used a sequential timeline with Git: each change builds on
the one before, and *only* on the one before.  However, there are times when we
want to work on several things at once.  To do this, we can use
[% i "branch (in Git)" "Git!branch" %][% g branch_git "branches" %][% /i %] to work on
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

<!-- continue -->
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

When we are done, we can [% i "merge (in Git)" "Git!merge" %][% g merge_git "merge" %][% /i %] the state of one branch back into another. Merging
doesn't change the source branch, but once it's done, all of the changes made
there are in the destination branch.

To see what the differences are between two branches, we use [% i "Git!viewing differences" %]`git diff`[% /i %] with those branches' names:

```sh
$ git diff homework3..main
```

<!-- continue -->
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

<!-- continue -->
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

<!-- continue -->
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
branches, we must learn how to merge [% i "conflict (in Git)" "Git!conflict" %][% g conflict_git "conflicts" %][% /i %].  These occur when a line has been changed
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
[% i "Git!rebase; rebasing (in version control)" %][% g "rebase_git" "rebasing" %][% /i %],
and can be done using:

```sh
$ git rebase -i START
```

<!-- continue -->
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

Most developers use this [% g branch_per_feature_workflow "branch-per-feature workflow" %], but what
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


[% i "version control!collaboration" %]Version control[% /i %] really comes into
its own when we are working with other people.  People can share work through a
Git repository in one of two ways [% b Irving2021 %]:

1.  Everyone has read and write access to a [% i "version
    control!using a shared repository" %]single shared
    repository[% /i %].

2.  Everyone can read from the project's main repository, but only a few people
    can commit changes to it.  The project's other contributors
    [% i "version control!using forked repositories" %][% g fork_git "fork" %][% /i %]
    the main repository to create one that they own,
    do their work in that, and then submit their changes to the main repository.

<!-- continue -->
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
break the build" ([% x automation %]), i.e., never commit anything that
doesn't run well enough to pass all existing tests.
</blockquote>

## Using Git Together

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

<!-- continue -->
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
[% i "pull request" "Git!pull request" %][% g pull_request "pull requests" %][% /i %] (PR).
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

<!-- continue -->
then make a change and commit it:

```sh
sami:~/bst $ git commit -a -m "Adding my email address"
```

<!-- continue -->
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

## Code Reviews

There's no point creating PRs if they are all merged as-is. The reason they
exist is to allow [% i "code review!effectiveness of" %][% g code_review "code review" %][% /i %].  One study after another since the mid-1970s has proven that code
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
    code review" %]refactoring[% /i %], they won't just make
    reviewing easier: the odds are very good that they will find and fix a few
    problems on their own.

Review at most 200 lines of a code at a time.
:   The SmartBear guide recommends reviewing at most 400 lines at a time, which
    should take 60--90 minutes. You will probably get there eventually, but in
    our experience it's better to start with something smaller and work up to
    that.  A corollary of this rule is that no PR should be more than 200 lines
    long.  If one is, the odds are that reviewers won't be able to hold it all
    in their head at once and so will miss things.

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

Don't [% g feigning_surprise "feign surprise" %] or pass judgment.
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

[% excerpt f="dup.py" %]

<div class="table" id="collaborate-code-review" caption="Code Review" markdown="1">
| Line(s) | Comment |
| ------- | ------- |
| 02      | Add a [% g docstring "docstring" %] describing the program. |
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
| 41      | [% g magic_number "Magic number" %] 10. |
| 41      | Provide option to control progress reporting. |
| 47      | Use `'rb'` to read files as binary. |
| 57      | Add a docstring describing this function. |
| 60      | Why `paths.pop()`? |
</div>

## Unit Testing {: #development-unit}

-   FIXME

## Linting {: #development-linting}

-   FIXME

## Packaging {: #development-packaging}

-   FIXME

## Other Tools {: #development-misc}

Tools don't just help us do things more easily; they shape what we consider
possible and encourage some working practices while discouraging others. They
also advertise how seriously we take our craft: people who want to be good at
something are willing to invest time in learning how to do it better.

I believe that processes are more important than tools, but that's because I
know how to use whatever tools I have to support productive working practices.
However, I focus on tools when talking to students because they are more
tangible: it's easier to tell if someone is using version control or a style
checker than it is to tell if they're designing or estimating sensibly.

[% x automation %] introduced build managers, style checkers, and profilers;
the sections below discuss some other tools you might want in your toolbox.  You
shouldn't try to adopt all of them in a single semester unless the focus of your
project course is to try out as many tools as possible (which is actually a good
theme for a project course).  If you'd rather not improve your tools, but are
afraid that someone on your team might want to do so, [% b Farmer2006 %] is
a not-entirely-serious guide to preventing something new from being adopted.

## Programming Language

You may not get to choose what programming language you use for your project,
but it may be the most important choice there is.  Programmers have argued about
which language is best for as long as there have *been* programmers. In my
experience, it makes a lot less difference than most people think…

…as long as you use the right one, that is. Twenty years ago there was a pretty
clear tradeoff between how quickly you can get a program running and how fast it
ran.  [% i "programming language!interpreted" %][% g interpreted_language "Interpreted languages" %][% /i %] like [% i "Perl" %]Perl[% /i %] optimized programmers' time; [% i "programming language!compiled" %][% g compiled_language "compiled languages" %][% /i %] like [% i "C" %]C[% /i %] optimized the machine's.

Today, the balance has shifted in favor of higher-level languages. One reason is
that processors have gotten faster but people haven't, so one programmer-hour is
worth many more computer-hours than before. Another reason is that
[% i "just-in-time compiler" %][% g jit "just-in-time compilers" %][% /i %] (JITs) and
[% i "generational garbage collection" "garbage collection!generational" %][% g generational_garbage_collection "generational garbage collection" %][% /i %]
have made higher-level languages intrinsically faster. The biggest, though, is that
the execution time of a modern application depends less on squeezing cycles out
of processors than it used to. The bottleneck in a web site is almost always
network latency or the time required to perform database operations; your code
probably accounts for only a few percent of the total, so doubling or tentupling
its speed has less effect than you'd think.

That said, there are three things to keep in mind:

Some languages are [% i "programming language!ease of learning" %]easier to learn[% /i %] than others.
:   [% b Stefik2013 %] did a controlled experiment to see how quickly
    people could learn to recognize correct and incorrect syntax in several
    different languages. They found that [% g curly_brace_language "curly-brace languages" %] like [% i "Java" %]Java[% /i %] and [% i "Perl" %]Perl[% /i %] were as hard for people
    to learn as a language with a randomly designed syntax. (They rolled
    *Dungeons & Dragons* dice to pick random names and characters for a made-up
    language.) Other languages like [% i "Ruby" %][Ruby][ruby][% /i %] and [% i "Python" %][Python][python][% /i %] were significantly easier to learn, and
    they are now building a language called [% i "Quorum" %][Quorum][quorum][% /i %] by testing the usability of every
    language feature.

Static typing helps, but only a little.
:   A [% i "static typing" "typing!static" "programming language!statically typed" %][% g static_typing "statically-typed" %][% /i %] language like [% i "Java" %]Java[% /i %] requires programmers to specify the data type of each
    variable; a [% i "dynamic typing" "typing!dynamic" "programming language!dynamically typed" %][% g dynamic_typing "dynamically-typed" %][% /i %]
    one like [% i "Python" %]Python[% /i %] doesn't require them, though you can add
    them if you want, while [% i "TypeScript" %]TypeScript[% /i %] adds types as
    a layer on top of [% i "JavaScript" %]JavaScript[% /i %].
    [% b Endrikat2014 %] found that declaring types does add complexity to
    programs, but it pays off fairly quickly by acting as documentation and by
    making [% i "auto-completion" %][% g auto_completion "auto-completion" %][% /i %]
    more accurate.

The most important thing about a language is its community.
:   Some programming communities work hard to welcome newcomers and treat
    everyone respectfully. Others are more likely to call naïve questions
    "stupid" or to make excuses when [% i "Linux!toxic leadership" %]their
    leaders harass people[% /i %] [% b Cohen2018 %]. As a junior programmer,
    you will learn more from the former than from the latter.

[% b Stefik2017 %] is a good short summary of what we know and why we
believe it's true. If someone disagrees with it, ask them to show you their
evidence.

## Package Management

There is no point building software if you can't install it.  Inspired by the
[% i "Comprehensive TeX Archive Network (CTAN)" %][Comprehensive TeX Archive
Network][ctan][% /i %], most languages now have an online archive from which
developers can download packages.  Each package typically has a name and one or
more version(s); each version may have a list of dependencies, and the package
may specify a version or range of versions for each dependency.

A [% i "package manager" %][% g package_manager "package manager" %][% /i %] is a
program that keeps track of which packages are installed on your computer and
how they depend on each other.  Package managers became popular out of necessity
in the 1990s along with Linux: so many distributions were being updated so often
that people needed tools to keep track of what they had.

Some package managers, like [% i "APT" "package manager!APT" %][APT][apt][% /i %]
for [% i "Linux" %]Linux[% /i %] and [% i "Homebrew" "package
manager!Homebrew" %][Homebrew][homebrew][% /i %] for [% i "MacOS" %]MacOS[% /i %],
can handle many languages. Others, like [% i "pip" "package
manager!pip" %][pip][pip][% /i %] for [% i "Python" %]Python[% /i %] and [% i "NPM" "package manager!NPM" %][NPM][npm][% /i %] for [% i "JavaScript" %]JavaScript[% /i %], are language-specific. No matter which one you
use, the biggest challenge you'll face is finding the packages you need: at the
time of writing, [this search][npm-xml-search] turns up over 700 XML parsers for
a JavaScript. To help narrow the search, NPM allows the results to be sorted by
popularity, quality, and maintenance. This obviously creates a feedback
loop—if NPM labels a package "more popular" then more people will find it,
which raises its popularity score even further—but [% i "NPMS" "package
manager!package ratings" %][NPMS][npms][% /i %] is open about how these scores are
calculated, so package authors can find out what they need to do in order to
improve their scores.

Whatever package manager you use, your project should follow these rules:

Keep a record.
:   NPM automatically updates a project's [% i "Node.js!package.json
    file" %]`package.json`[% /i %] file to show which packages have been installed
    explicitly, and its `package-lock.json` file keeps track of exactly which
    versions of their dependencies have been installed as well, so in theory,
    someone else can duplicate your environment exactly. If you are using pip
    for Python, on the other hand, it's up to you to create a file (typically
    called `requirements.txt`) that lists the packages someone needs to make
    your project work.

To install is beautiful, to uninstall divine.
:   You should install packages to try them out before committing to using them,
    but if you decide that something doesn't do what you want, please remember
    to uninstall it. (I have worked with projects that used less than half of
    their "requirements".)

Keep an eye on security updates.
:   NPM will warn you if there are security problems with things you depend on.
    The world would be a slightly safer place if other package managers did this
    as well.

<blockquote markdown="1">
### Docker

[% i "Docker" %][Docker][docker][% /i %] uses some clever tricks to run one
operating system on top of another to create a
[% i "virtual machine" %][% g "virtual_machine" "virtual machine" %][% /i %]
(VM) that is isolated from everything
beneath it.  It and other tools like it are used by most cloud computing
services and to run continuous integration systems ([% x automation %]), but
they are essentially an admission that we haven't figured out how to manage
packaging reliably.
</blockquote>

## Integrated Development Environment

You are going to spend a lot of time editing code, documentation, and reports,
so choosing a good editor is as important as choosing a comfortable chair.
There are literally thousands to consider, from very small plain-text editors
such as [% i "Notepad" "editor!Notepad" %]Notepad[% /i %] (which comes with [% i "Windows" %]Windows[% /i %]) to very large ones like [% i "Emacs" "editor!Emacs" %]Emacs[% /i %] (which some people claim is actually Lisp-based
operating system in disguise).

<blockquote markdown="1">
### Stuck in the punchcard era

In many ways, programming is still stuck in the punchcard era: we still insist
that source code be represented as lines of characters that are drawn
one-for-one on the screen.  [% g wysiwyg "WYSIWYG" %] editors like
Microsoft Word did away with this model decades ago; they store the file in a
machine-friendly format and then render it in a human-friendly way. There's no
reason we couldn't do the same with programs.  There's no reason we shouldn't be
able to draw a diagram directly in our source code like we can in a Google Doc;
if you are looking for a project to tackle, this would be a good one.
</blockquote>

You might already have a favorite editor. If you're like most programmers, you
will change jobs, languages, operating systems, and nationality before you'll
switch to another, because it has taken weeks or months for your hands to master
the current one. However, if it is not an [% i "IDE" %][% g ide "integrated development environment" %][% /i %] (IDE) that combines an editor with other
programming tools then getting work done will take longer and hurt more than it
needs to.

IDEs were invented in the 1970s, but didn't really catch on until [% i "Borland" %]Borland[% /i %] released [% i "Turbo Pascal" %]Turbo Pascal[% /i %]
in the 1980s.  They usually include these tools:

-   A [% i "console" "IDE!console" %][% g console "console" %][% /i %] so that you can
    type in expressions or call functions and see the results without having to
    start (or restart) your program.

-   A [% i "code browser" %][% g code_browser "code browser" %][% /i %] that helps you
    navigate the packages, classes, methods, and data in your program.

-   A [% i "GUI designer" %][% g gui_designer "GUI designer" %][% /i %] that lets you
    build GUIs by dragging and dropping components;

-   A [% i "test runner" %]test runner[% /i %] to display the results of tests and
    let you jump directly to ones that have failed. This is usually a GUI built
    on top of whatever unit testing framework you are using
    ([% x testing %]), just as graphical interfaces for version control are usually
    built on top of the command-line tools.

The most popular IDE today is probably [% i "VS Code" "Microsoft Visual Studio
Code" "IDE!VS Code" %][Microsoft Visual Studio Code][vs-code][% /i %], often
referred to simply as "VS Code".  Along with all the tools above, it has
hundreds of [% i "plugin!for IDE" %][% g plugin "plugins" %][% /i %] of varying
quality to support database design, reverse engineering, dozens of different
programming languages, and more.  These all make you more productive than their
disconnected counterparts. Since most of these store project data (including
build instructions) in a proprietary format, your team will do much better if
you all adopt the same IDE. This will also let you help one another solve
problems and share plugins.

But calling VS Code is the world's most popular IDE is misleading.  If you open
[% i "IDE!in browser" %]developer tools[% /i %]. in Firefox, Chrome, or Edge, you
will be shown an HTML browser that's smart enough to tell you which bits of CSS
are in effect where, a console that displays messages from the JavaScript
running in the page, a breakpointing debugger, a network
monitor, and much more. It won't help you with your C# or Python—at least, not
yet—but it will make all of your front-end work a lot easier.

## Refactoring

After a debugger, the most under-appreciated power of most IDEs is their ability
to [% i "refactoring" %][% g refactoring "refactor" %][% /i %] code, i.e., to change
its structure without changing what it does [% b Fowler2018 %].  It is just
as much a part of programming as writing code in the first place: nobody gets
things right the first time, and needs or insights can change over time
[% b Brand1995 %].

Some common refactoring patterns include "hoist repeated calculation out of
loop" and "replace repeated test with flag". As [% b Kerievsky2004 %]
showed, many refactorings make code fit a design pattern or move code from one
design pattern to another.  If you highlight a variable name in an IDE like VS
Code and say, "Rename", it parses the code to find all uses of that variable and
changes their names and *only* their names, so that (for example) you don't
accidentally turn `alfred` into `alfblue`. "Extract method" is another favorite
of mine: if a method is getting too long or you want to re-use part of its
implementation, you can highlight a few lines, click, and enter a name, and the
IDE will do the rest of the work for you.

Using refactoring tools doesn't just save you a few seconds of typing: it also
reduces the chances of making a mistake so that you don't lose time later trying
to figure out what's gone wrong.  (The `alfblue` error mentioned in the previous
paragraph cost me about ten minutes.)  It also helps you maintain concentration,
since you don't have to make a mental switch from the code you're writing to the
refactoring you're doing and then back again.

## The Next Level

You and your teammates could use many other tools to make yourselves more
productive. Some aren't part of the standard undergraduate curriculum yet, even
though good developers have been relying on them for a decade or more. Others
may be touched on, but only briefly, so a quick recap won't hurt.

The first is a [% i "documentation generator" %][% g doc_generator "documentation generator" %][% /i %] like [% i "JSDoc" "documentation
generator!JSDoc" %][JSDoc][jsdoc][% /i %]. This is a compiler of a sort, but
instead of translating source code into something executable, it extracts
information from specially-formatted comments and strings, and turns it into
human-readable documentation.  The justification for this is that when code and
documentation are stored separately, programmers won't keep the latter up to
date. Since "rusty" documentation can be worse than no documentation at all, it
makes a lot of sense to keep the source of the documentation right beside the
code. Many introductory courses require students to document their packages,
classes, and methods this way; it's a good habit, and one you should cultivate.

Another set of tools complement the style checkers discussed in [% x automation %].
Style checkers do static analysis, i.e., they look at the
text of your program while it's at rest.  Other tools do [% i "dynamic analysis" %][% g dynamic_analysis "dynamic analysis" %][% /i %]: tools like
[% i "Valgrind" "dynamic analysis!Valgrind" %]Valgrind[% /i %] watch your [% i "C" %]C[% /i %] or [% i "C++" %]C++[% /i %] program run and look for things like
memory leaks, or inconsistent locking that might lead to deadlocks or race
conditions.

Real development projects rely on a lot of other tools as well: schedule
builders like [% i "Microsoft Project" %]Microsoft Project[% /i %], requirements
tracing tools, and so on. Most are bigger hammers than undergraduate projects
really require, but good programmers don't just use tools, they build them.  For
example, I have written two dozen short programs to help me write and maintain
this book and others like it.  These tools do things like check
cross-references, make sure I'm using the right CSS attributes for elements, and
so on.  If you and your teammates find yourselves typing in the same commands
over and over again, write a program to do it for you.

<blockquote markdown="1">
### From seeds to trees

A lot of open source projects and commercial products began with one programmer
solving a problem for themselves and then discovering that other people found it
useful as well. [% i "Grand Perspective" %][Grand
Perspective][grand-perspective][% /i %] displays a tree map to show what's using
disk space on a Mac; [% i "Carnac" %][Carnac][carnac][% /i %] shows what special
keys you're pressing on Windows so that if you're doing a demo, people can see
the keyboard shortcuts you're using, and so on.  Building one small thing well
is a lot more useful, and a lot more likely to be used, than building half of
something larger.
</blockquote>

## Modeling

If you want to go one big step further, you can start using modeling tools like
[% i "Alloy" "modeling tools!Alloy" %][Alloy][alloy][% /i %]
[% b Jackson2016 %] and [% i "TLA+" "modeling
tools!TLA+" %][TLA+][tla-plus][% /i %] [% b Wayne2018 %].  Instead of
analyzing source code, you use these tools to build and analyze a [% g model "model" %] of what the code is supposed to do so that you can look
for flaws in your algorithms.

Alloy focuses on describing complex relationships, such as the integrity of data
structures; TLA+ is designed to help you reason about sequences of concurrent
actions, such as the different ways microservices can exchange messages. Both of
them can find counter-examples, i.e., situations that break the rules you have
described, but both have interfaces that make Git look simple.
[These][gritter-alloy] [articles][gritter-tla-plus] give an idea of what they
can do; you probably won't have time to learn them along the way while working
on a project, but if your school offers a course devoted to them, it will
probably change your view of programming just as much as it changed mine.

## Exercises {: #development-exercises}

-   FIXME
