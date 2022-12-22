---
title: "Tooling"
syllabus:
- Choose a programming language based on its libraries and its community.
- Use a package manager and an isolated environment for your project's dependencies.
- Use a version control system to share files and record a project's history.
- Use a build manager to repeat work in a reproducible way.
- Use a test runner to find and execute tests and report their results.
- Use a linter to ensure consistent code style and find common problems.
- Use an IDE rather than a plain text editor when coding.
---

If you know how to work well you can find a way to do it using whatever is available,
but if you don't,
the best tools in the world are useless.
However,
tools are more tangible than processes:
it's easier to tell if someone is using version control or a style checker
than it is to tell if they're designing or estimating sensibly.
This chapter therefore describes tools that you should already be using
by the time you reach a course like this.

> The hand shapes the tool and then the tool shapes the hand.
>
> — various attributed

## Programming Language {: #tooling-language}

Programmers have argued about which language is best for as long as there have *been* programmers.
Twenty years ago there was a pretty clear tradeoff
between how quickly you could get something to run the first time
and how fast it ran.
High-level [%i "programming language!interpreted" %][%g interpreted_language "Interpreted languages" %][%/i%]
like [%i "Perl" %]Perl[%/i%]
optimized programmers' time;
low-level
[%i "programming language!compiled" %][%g compiled_language "compiled languages" %][%/i%]
like [%i "C" %]C[%/i%]
optimized the machine's.

The difference between the two is much smaller now than it used to be:
[%i "Go" %][Go][go][%/i%] is faster than [%i "Python" %][Python][python][%/i%],
but Python runs fast enough for most all needs,
while the Go compiler is so fast that the language feels interactive.
The biggest change,
though,
is that the execution time of modern applications depends less on
squeezing performance out of processors than it used to.
The bottleneck in a web application is almost always network latency
or the time required to perform database operations,
so doubling or tentupling the speed of the software has little effect.

That said, there are three things to keep in mind:

Some languages are [%i "programming language!ease of learning" %]easier to learn[%/i%] than others.
:   [%b Stefik2013 %] did a controlled experiment to see
    how quickly people could learn to recognize correct and incorrect syntax
    in several different languages.
    They found that [%g curly_brace_language "curly-brace languages" %]
    like [%i "Java" %]Java[%/i%] and [%i "Perl" %]Perl[%/i%]
    were as hard for people to learn as a language with a randomly designed syntax.
    (They rolled *Dungeons & Dragons* dice to pick random names and characters
    for a made-up language.)
    Other languages like [%i "Ruby" %][Ruby][ruby][%/i%] and [%i "Python" %][Python][python][%/i%]
    were significantly easier to learn,
    and they are now building a language called [%i "Quorum" %][Quorum][quorum][%/i%]
    by testing the usability of every language feature.

Static typing helps, but only a little.
:   A [%i "static typing" "typing!static" "programming language!statically typed" %][%g static_typing "statically-typed" %][%/i%]
    language like [%i "Java" %]Java[%/i%]
    requires programmers to specify the data type of each variable;
    a [%i "dynamic typing" "typing!dynamic" "programming language!dynamically typed" %][%g dynamic_typing "dynamically-typed" %][%/i%] one like [%i "Python" %]Python[%/i%] doesn't,
    though you can add them if you want.
    [%b Hanenberg2013 Endrikat2014 %] found that declaring types does add complexity to programs,
    but it pays off by acting as documentation
    and by making [%i "auto-completion" %][%g auto_completion "auto-completion" %][%/i%] more accurate.
    More recently,
    [%b Gao2017 %] found that adding TypeScript typing to programs
    would catch 15% of bugs in existing programs,
    which is either not much (one in seven)
    or a lot (more than sales tax here in Ontario).

The most important thing about a language is its community.
:   Some programming communities work hard to welcome newcomers
    and treat everyone respectfully.
    Others are more likely to call naïve questions "stupid"
    or to make excuses when [%i "Linux!toxic leadership" %]their leaders harass people[%/i%]
    [%b Cohen2018 %].
    As a junior programmer,
    you will learn more from the former than from the latter.

[%b Stefik2017 %] is a good short summary of what we know about languages' usability
and why we believe it's true.
If someone disagrees with it,
ask them to show you *their* evidence.

## Package Manager {: #tooling-packman}

There is no point building software if you can't install it.
Inspired by the [%i "Comprehensive TeX Archive Network (CTAN)" %][Comprehensive TeX Archive Network][ctan][%/i%],
most languages now have an online archive from which developers can download packages.
Each package typically has a name and one or more versions;
each version has a list of dependencies,
and the package may specify a version or range of versions for each dependency.

A [%i "package manager" %][%g package_manager "package manager" %][%/i%]
is a program that keeps track of which packages are installed on your computer
and how they depend on each other.
Package managers became widespread in the 1990s to cope with [%i Linux %]Linux[%/i%]:
so many distributions were being updated so often
that people needed tools to keep track of what they had.

Package managers
like [%i "APT" "package manager!APT" %][APT][apt][%/i%] for [%i "Linux" %]Linux[%/i%]
and [%i "Homebrew" "package manager!Homebrew" %][Homebrew][homebrew][%/i%] for [%i "MacOS" %]MacOS[%/i%]
can handle many languages.
Others,
like [%i "pip" "package manager!pip" %][pip][pip][%/i%] for [%i "Python" %]Python[%/i%]
and [%i "NPM" "package manager!NPM" %][NPM][npm][%/i%] for [%i "JavaScript" %]JavaScript[%/i%],
are language-specific.
No matter which one you use,
the biggest challenge you'll face is finding the packages you need:
at the time of writing,
[this search][npm_xml_search] turns up over 700 XML parsers for JavaScript.
To help narrow the results,
NPM allows the results to be sorted by popularity, quality, and maintenance.
Doing this obviously creates a feedback loop:
if NPM labels a package "more popular" then more people will find it,
which raises its popularity score even further.
Unlike most social media,
[%i "NPMS" "package manager!package ratings" %][NPMS][npms][%/i%] is open
about how these scores are calculated,
so package authors can find out what they need to do in order to improve their scores.

Whatever package manager you use,
your project should follow these rules:

Keep a record.
:   NPM automatically updates a project's
    [%i "Node!package.json file" %]`package.json`[%/i%] file
    to show which packages have been installed explicitly,
    and its `package-lock.json` file keeps track of
    exactly which versions of their dependencies have been installed as well.
    In theory,
    someone else can duplicate your environment exactly.
    If you are using `pip` for Python,
    on the other hand,
    it's up to you to create a file (typically called `requirements.txt`)
    that lists the packages someone needs to make your project work.

To install is beautiful, to uninstall divine.
:   You should install packages to try them out before committing to using them,
    but if you decide that something doesn't do what you want,
    please uninstall it.
    (I have worked with projects that used less than half of their "requirements".)

Keep an eye on security updates.
:   NPM will warn you if there are security problems with things you depend on.
    The world would be a slightly safer place if more people paid attention to these warnings.

## Environments {: #tooling-environments}

If you are working on several projects at the same time,
you will need to manage their packages separately
so that a change to one project doesn't break another.
Different languages manage [%i environment %][%g environment environments %][%/i%]
in different ways:

Install everything a project needs in that project.
:   If every project contains everything it depends on,
    updates to one project can't affect others.
    This is NPM's approach;
    it uses much more storage than necessary
    (because a single package can be installed many times on the same machine)
    but ensures isolation.

Change the path.
:   Most languages' runtimes check an environment variable
    called a [%i "search path" %][%g search_path "search path" %][%/i%]
    that lists the directories from which libraries can be loaded.
    Tools like Python's `virtualenv` put an extra directory on the front of this path
    for each [%g virtual_environment "virtual environment" %]
    so that environment-specific libraries are found before system-wide libraries.

Use a virtual machine.
:   [%i "Docker" %][Docker][docker][%/i%] uses some clever tricks
    to run one operating system on top of another to create a
    [%i "virtual machine" %][%g "virtual_machine" "virtual machine" %][%/i%]
    (VM) that is isolated from everything beneath it.
    VMs ensure complete isolation,
    and as a bonus VMs can be deployed to the cloud ([%x devops %]),
    but they are essentially an admission that
    we haven't figured out how to manage packaging reliably.

## Version Control {: #tooling-versioning}

[%i "version control!reasons to use" %]Version control[%/i%]
is the collective memory of the project.
It's what lets you move files from one machine to another
without clobbering stuff you just spent three hours writing
and without worrying about whether you forgot something important.
It also lets you undo your mistakes:
if you spend an hour or two going down the wrong path
and want to get back to where you were,
version control lets you do it reliably with a single command.
If all that wasn't enough,
version control lets you share files reliably with your teammates
and keeps track of who did what
so that you know who to turn to with questions.

Dozens of [%i "version control!systems" %]version control[%/i%] systems exist.
[%i "version control!CVS" "CVS (version control)" %][CVS][cvs][%/i%]
was the workhorse of open source for many years;
it was replaced by
[%i "version control!Subversion" "Subversion (version control)" %][Subversion][subversion][%/i%],
which fixed many of its predecessor's flaws while introducing a few minor ones of its own.
Both of these were [%i "version control!centralized" %][%g centralized_system "centralized systems" %][%/i%]:

1.  One [%i "version control!repository" "repository (version control)" %][%g repository "repository" %][%/i%]
    stored the definitive copy of the project's files.

1.  Nobody ever edited the contents of the main repository directly.
    Instead, everyone worked in a local copy.

1.  In order to share files,
    people would [%g push_git "push" %] the contents of their copy to the main repository.
    To get other people's work,
    they would [%g pull_git "pull" %] changes from the main repository
    and [%g merge_git merge %] them with their own work.

Centralized version control systems have largely been replaced by
[%i "version control!decentralized" %][%g decentralized_system "decentralized" %][%/i%] ones,
and in particular by [%i "version control!Git" "Git" %][Git][git][%/i%].
In theory,
a Git project doesn't need a main repository:
developers can merge the contents of any repository into any other.
In practice,
every project designates one repository as the master copy
so that people know where to look to find the current state of the project.

Unfortunately,
Git has a needlessly complicated interface.
[% b PerezDeRosso2013 %] found that even experienced users'
[%i "mental model!Git" %][%g mental_model "mental model" %][%/i%] of how it works
is inconsistent with its actual operation in important ways.
Each of these inconsistencies produces a steady stream of "what the hell?"  moments.
Other distributed version control systems
like [%i "version control!Mercurial" "Mercurial (version control)" %][Mercurial][mercurial][%/i%]
are proof that this complexity and pain are unnecessary.
(The fact that most people don't immediately realize that
[the random Git manual page generator][git-man-page-generator]
is a [%i "Git!interface (indistinguishable from hoax)" %]hoax[%/i%]
says a lot…)

So why do people keep using [%i "Git!reasons for popularity" %]Git[%/i%]?
Because everyone else is using it,
and because it's the tax they have to pay in order to use [GitHub][github].
At the time of writing
GitHub has over 40 million users and hosts over 28 million public repositories,
including those for many well-known open source projects.
It is easily the most popular [%i "software portal!GitHub" %][%g software_portal "software portal" %][%/i%] in existence,
and offers all of the tools a small software team needs.
Other portals like [%i "Bitbucket" "software portal!Bitbucket" %][Bitbucket][bitbucket][%/i%]
and [%i "GitLab" "software portal!GitLab" %][GitLab][gitlab][%/i%]
are just as usable,
but GitHub's share of the educational market is even larger than its share among professional developers.
If you're using anything in class,
you're almost certainly using it,
and it's probably helping you become a better programmer
[% b Hsing2019 %].

<div class="callout" markdown="1">

### Why can't we fix it?

If Git's interface is a problem, why can't we build a new one?
[% b PerezDeRosso2016 %] tried,
but the gravity of the existing interface is simply too powerful:
as soon as people run into a problem and start searching online for solutions
they are thrown back into the world of original Git.

</div>


This section won't try to teach you Git from scratch:
[GitHub's guides][github-guides] and [the Atlassian Git tutorial][atlassian-git]
do an excellent job of that,
as does [the Carpentries lesson on Git][carpentries-git].
Instead,
we will review the basics that we hope you have learned previously.
We show the commands you would run in the Unix shell,
but we recommend that you use a [%i "Git!graphical interface" %]graphical interface[%/i%]
like [GitKraken][gitkraken],
[SourceTree][sourcetree],
or the one that comes with your IDE (discussed below).
If any of the commands below are unfamiliar,
please take the time to work through one of the Git tutorials linked above.

The first step is to make sure that [%i "Git!configuring" %]Git knows who we[%/i%]
are by configuring our name and email address.

```sh
$ git config --global user.name "Pera DiAngelo"
$ git config --global user.email "pera@secept.org"
```

The `--global` flag tells Git to apply this change across the whole machine,
i.e.,
to set it for every project.
{: .continue}

Next,
let's [%i "Git!creating project" %]set up a project[%/i%].
If we are starting from scratch,
we create a directory,
go into it,
and run `git init`.
This command creates a sub-directory called `.git` inside your project directory.
That sub-directory is what makes something a project:
it stores the data Git uses to keep track of what files you have
and how they've changed.

<div class="callout" markdown="1">

### Don't mess

Don't edit the files in your `.git` directory yourself—it will have
the same unfortunate effect as editing a spreadsheet or an image
as if it was a text file.
If you'd like to know more about what they're for and how Git uses them,
please see [% b Chacon2014 %] or [% b Cook2019 %].

</div>

You won't use `git init`
if your instructor or one of your teammates has already created a project.
Instead,
you will use `git clone` followed by the project's URL
to get a local copy called a [%i "Git!cloning project" %][%g clone_git "clone" %][%/i%].
For example,
this command clones the repository for this book:

```sh
$ git clone https://github.com/gvwilson/secept
```

Cloning creates a directory with the same name as the project
and a `.git` sub-directory inside it.
It also downloads the project's history so that you can start work.
{: .continue}

Regardless of how you create your repository,
you can use `git log` to look at its [%i "Git!history" %]history[%/i%]:

[%excerpt f="git-log.txt" %]

Each entry has:

-   A line labeled `commit` followed by a hexadecimal number.
    This number is a unique [%i "Git!commit ID" %]label[%/i%]
    for the state of the project's files at that point in time.
    We can use this to refer to a particular state of the project;
    it is enough in most cases to use the first half-dozen digits
    such as `1a8fed` so long as they are unique.

-   Two lines showing who saved the state of the project and when.

-   A short [%i "commit message (version control)" "Git!commit message" %][%g commit_message "commit message" %][%/i%]
    describing the change.
    [%x communication %] explains how to write a good commit message;
    for now,
    just remember that if your team makes a hundred changes to the project
    over the course of several months,
    you're going to want something more informative than "Fixed stuff."

A [%i "commit (version control)" "Git!commit" %][%g commit "commits" %][%/i%]
is a snapshot of the project at a particular moment in time.
We create commits using a command like:

```sh
$ git commit -m "Made the status bar display the user name"
```

Before we run `git commit`,
though,
we need to tell Git which files we want to save.
We do this using `git add`:

```sh
$ git add src/tooling.md info/glossary.yml
```

[%i "Git!difference between add and commit" %]One way to think about this[%/i%]
is that `git add` puts things in a box to be shipped
while `git commit` actually sends the package.
Git does this in two steps
because we might change our mind about what we want to save:
for example,
we might `git add` a file,
realize we need to make a few more edits,
`git add` it again,
and only then commit.
Alternatively,
we might add a bunch of files
and then realize that some of them
(like editor backup files or temporary data files)
shouldn't be saved.

<div class="callout" markdown="1">

### Teach us to care and not to care

You can tell Git to [%i "Git!ignoring files" %]ignore certain kinds of files[%/i%]
by putting their names,
or patterns that match multiple names,
in a file called `.gitignore`.
For example, the `.gitignore` file for this project includes:

```txt
*.pyc
*~
.DS_Store
__pycache__
```

Be careful not to put files containing passwords or [%g api_key "API keys" %] for web services
into version control.
Even if the repository is private now,
it might be public in future,
or the team might grow to include someone who shouldn't have access.

</div>

We can keep track of which changes haven't yet been added
and which have using [%i "Git!showing status" %]`git status`[%/i%].
If I run this command right now in this book's project I get:

[%excerpt f="git-status.txt" %]

The first paragraph tells me which files I have added but not yet committed.
The second tells me which files I have changed,
and the third tells me which files have never been saved in version control.
{: .continue}

I can use [%i "Git!recovering old files" %]`git restore`[%/i%]
to recover an old version of a file from any previous commit.
For example,
if I want to get the version of this file from two days ago,
I can use `git log` to find the commit ID `2be70844` and run:

```sh
$ git restore --source 2be70844 src/tooling.md
```

I can also count backward from where I am now.
The most recent commit has the special [%i "Git!HEAD" %]symbolic name `HEAD`[%/i%];
the expression `HEAD~1` means "the one before it",
while `HEAD~2` goes back two commits and so on.
Regardless of how I specify what I want,
restoring an old version doesn't erase any of the ones I have saved since then:
the project's history stays intact.

Finally,
I should make sure there's a copy of my work
so that I don't lose everything I've done
if my drive fails or my laptop is stolen.
If I create the repository by cloning a repository,
Git automatically adds a bookmark called a [%i "Git!remote" "remote (in Git)" %][%g remote_git "remote" %][%/i%]
that points at the original repository.
I can get a list of remotes like this:

```sh
$ git remote -v
```
```out
origin	https://github.com/gvwilson/secept.git (fetch)
origin	https://github.com/gvwilson/secept.git (push)
```

The remote's name is `origin`.
Git lists two URLs for it because in theory you can download (or "fetch") from one
and upload (or "push") to another.
(I have never once needed this feature in the sixteen years I have been using Git
[%b Xu2015 %].)
{: .continue}

One difference between Git and a file backup tool like [Dropbox][dropbox]
is that Git doesn't automatically synchronize local changes to the remote repository.
If I want to [%i "Git!saving changes remotely" %]save[%/i%] everything I've done to GitHub,
I have to push changes explicitly:

```sh
$ git push origin main
```

The word `main` identifies the branch I'm on.
We'll discuss branches in [%x process %];
for now,
you can run `git branch` to see which one you're working in.

The counterpart of `git push` is `git pull`,
which downloads changes from the remote repository:

```sh
$ git pull origin main
```

Pushing and pulling allows you and your teammates to synchronize your work.
They are also often used to deploy software to remote machines
([%x devops %]).

## Build Manager {: #tooling-build}

A [%i "build manager" %][%g build_manager "build manager" %][%/i%]
is a tool that re-runs commands to recompile programs,
rebuild packages,
or anything else a project needs to do repeatedly.
The origin build manager,
[%i "Make" "build manager!Make" %][Make][make][%/i%],
was invented in 1975 by a summer intern at Bell Labs to compile C programs
in which some modules depended on others.
Its configuration files look like this:

[%excerpt f="example.mk" %]

This file tells Make that `game.exe` can't be compiled
until `game.bc`, `graphics.bc`, and `utils.bc` exist,
and that once they do,
the way to create `game.exe` is to run the `tx` compiler with several options.
Below that is a [%i "Make!pattern rule" %][%g pattern_rule "pattern rule" %][%/i%]
telling Make how to create any `.bc` file from a `.grace` file with the same root name;
the cryptic expression `$<` is Make's way of saying "the first thing the target depends on".

Make has been used by hundreds of thousands of programmers for more than forty years,
but has some [%i "Make!shortcomings" %]fundamental flaws[%/i%].
The first is its syntax;
the second is that it runs commands by invoking shell commands,
which make portability a constant headache.
(Quick, should you use `rm` or `del` to delete a file?)
Third, Make doesn't have a debugger:
the only way to track down problems in your configuration
is to tweak things and hope the problems go away.

Programmers have built [hundreds of alternatives to Make][build_tool_list],
but each one has only been adopted within a single language community.
Whatever you choose or are told to use,
please [%i "build manager!rules for using" %]follow these rules[%/i%]:

Choose something that works with your other tools.
:   For example,
    most Java editors and IDEs integrate with a build tool called
    [%i "build manager!Ant" "Ant" "Java!build manager" %][Ant][ant][%/i%],
    which means they can jump directly to compilation errors when they occur.

Be cautious about adding dependencies.
:   "Reduce, re-use, recycle" is as important for software as it is for daily life
    but every library you depend on is one more way for your project
    to accumulate [%i "technical debt" %]technical debt[%/i%].
    We are all biased toward solving problems by adding things
    instead of taking them away [% b Meyvis2021 %];
    checking the packages your project depends on before every release
    and cutting any you can will prevent a lot of future headaches.

Always use the build manager—never build by hand.
:   This isn't just for efficiency's sake:
    if any of the things you need to do
    to get your application up on your web site
    have to be done by hand,
    the odds are that you'll forget a crucial step right before a crucial demo.
    and if you do something by hand,
    one of your teammates might do it differently.
    "But it works on my machine!"
    isn't something you want to hear an hour before a deadline…

Once you have a build system in place,
never commit anything to version control that
[%i "version control!and build manager" "build manager!and version control" %]breaks the build[%/i%].
This is one of the golden rules of working in a team:
if your code won't compile or doesn't pass tests,
putting it into the repository can interrupt everyone else on the team.
It's OK to use version control as a simple file backup tool when you're working on your own,
but do *not* carry this habit over to teamwork.

## Test Runner {: #tooling-test}

A [%i "unit test" %][%g unit_test "unit test" %][%/i%] is one that checks the correctness
of a single piece of software.
Exactly what constitutes a "single piece" is subjective,
but it typically means the behavior of a single function or method in one situation.
Every unit test has:

-   A [%i "fixture (in unit test)" "unit test!fixture" %][%g fixture "fixture" %][%/i%],
    which is the thing being tested.
    The fixture is typically a subset or smaller version of
    the data the function will typically process.

-   The [%i "expected result (in unit test)" "unit test!expected result" %][%g expected_result "expected result" %][%/i%]
    that the code is supposed to produce when given the fixture.

-   The [%i "actual result (in unit test)" "unit test!actual result" %][%g actual_result "actual result" %][%/i%]
    that the code actually produces.

Good programmers frequently run tests interactively when debugging,
but tests are much more valuable when they can be re-run at a moment's notice
to make sure that recent changes haven't [% g regression "regressed" %],
i.e.,
haven't broken anything that used to work.
Every modern programming language has [%i "test runner" "unit test!test runner" %][%g test_runner "test runners" %][%/i%]
to find and run tests and report their results.
The most widely-used test runner for Python is [`pytest`][pytest]:

1.  Tests are put in files whose names begin with `test_`.

2.  Each test is a function whose name also begins with `test_`.

3.  These functions use `assert` to check results.

If running all the tests takes so long that it's disrupting developers' [%i "flow" %]flow[%/i%],
you can tell `pytest` and other test runners to run only one test or a subset of tests.
This speeds up debugging,
but you should always re-run the entire [%i "test suite" "unit test!test suite" %][%g test_suite "test suite" %][%/i%]
before committing your changes to version control.

## Linter {: #tooling-lint}

A [%i "linter" %][%g linter "linters" %][%/i%] is a program
that checks your source code for things that are legal but questionable.
(The name comes from an early tool called `lint` that looked for problems in C code.)
Linters are also called [%i "style checker" %][%g style_checker "style checkers" %][%/i%]
because they check rules like
"no method can be longer than 100 lines"
or "class names must be written in CamelCase".
Code is much easier to read and review when it is formatted consistently,
so everything should be linted and reformatted before being committed to version control.

Modern linters like [%i "linter!ESLint" "ESLint" %][ESLint][eslint][%/i%]
for [%i "JavaScript!linter" %]JavaScript[%/i%],
[%i "Checkstyle" "linter!Checkstyle" %][Checkstyle][checkstyle][%/i%]
for [%i "Java!linter" %]Java[%/i%],
or [%i "linter!Black" "Black" %][Black][black][%/i%] for [%i "Python!linter" %]Python[%/i%]
can do more than just check style.
For example,
they can find code that is never called,
parameters that are never used,
and duplicated code that could be refactored.
This kind of checking is called [%i "static analysis" %][%g static_analysis "static analysis" %][%/i%]
because these tools work by analyzing source code
rather than by watching the program run.
Compilers also do a lot of static analysis;
the warnings they produce are a lot more useful than many students realize,
and a "zero warnings" policy can prevent a lot of subtle bugs.

## Integrated Development Environment {: #tooling-ide}

Programmers spend a lot of time editing code and documentation,
so choosing a good editor is as important as choosing a comfortable chair.
You probably already have one,
and if you're like most programmers,
you will change jobs, operating systems, and nationality
before you'll switch
because it takes weeks or months for your hands to master a new one.
However,
if it is not an [%i "IDE" %][%g ide "integrated development environment" %][%/i%] (IDE)
that combines an editor with other tools,
then everything you do will take longer and hurt more than it needs to.

IDEs were invented in the 1970s,
but didn't really catch on until [%i "Borland" %]Borland[%/i%] released [%i "Turbo Pascal" %]Turbo Pascal[%/i%]
in the 1980s.
IDEs usually included tools:

-   A [%i "console" "IDE!console" %][%g console "console" %][%/i%]
    so that you can type in expressions or call functions and see the results
    without having to start (or restart) your program.

-   A [%i "code browser" %][%g code_browser "code browser" %][%/i%]
    to navigate the packages, classes, methods, and data in your program.

-   [%i "refactoring" %]Refactoring tools[%/i%]
    to reformat and reorganize code.

-   A [%i "test runner" %]test runner[%/i%] to re-run tests,
    display their results,
    and jump directly to ones that have failed.

The most popular IDE today is
[%i "VS Code" "Microsoft Visual Studio Code" "IDE!VS Code" %][Microsoft Visual Studio Code][vs_code][%/i%],
often referred to simply as "VS Code".
Along with all the tools above,
it has hundreds of [%i "plugin!for IDE" %][%g plugin "plugins" %][%/i%]
to support database design,
manage version control,
preview web pages,
and much more.

But calling VS Code is the world's most popular IDE is misleading.
If you open [%i "IDE!in browser" %]developer tools[%/i%]. in Firefox, Chrome, or Edge,
you will see an HTML browser that's smart enough to tell you
which bits of CSS are in effect where,
a console that displays messages from the JavaScript running in the page,
a breakpointing debugger,
a network monitor,
and much more.
It won't help you with your C# or Python—at least, not yet—but
it will make all of your front-end work a lot easier.

<div class="callout" markdown="1">

### Stuck in the punchcard era

In many ways,
programming is still stuck in the punchcard era:
we still insist that source code be represented using characters
that are typed one at a time.
[%g wysiwyg "WYSIWYG" %] editors like Microsoft Word did away with this model decades ago:
they store the file in a machine-friendly format and then render it in a human-friendly way.
Drawing tools, spreadsheets, and almost every other kind of "editor" does the same,
and there's no reason we couldn't do the same with programs.
if you are looking for a project to tackle, this would be a good one.

</div>

## Exercises {: #tooling-exercises}

-   FIXME
