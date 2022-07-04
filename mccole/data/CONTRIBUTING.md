# Contributing

Please follow these guidelines when contributing to this project.

*All contributors are required to abide by our Code of Conduct.*

## Setup

-   Create a conda environment with Python 3.10 using `conda create -n nitinat python=3.9`.
-   Switch to that environment and install all dependencies using `pip install -r requirements.txt`.

## Tracking Work

Use issues in our GitHub repository to manage work.

## Pull Requests

Submit changes as pull requests, and use [conventional commits][conventional-commits]
for commit messages:

-   The first line of the commit message must be `type: details` where `type` is one of:
    -   `feat`: adds a new feature or new content.
    -   `fix`: fixes existing code or content that was wrong.
    -   `refactor`: reorganizes code or restyles content without changing
        its behavior or meaning.
-   The body of the commit message must include a point-form summary of the
    changes, and may optionally explain the background to the change.
-   The footer of the commit message may include `Closes #NNN` if this pull request
    closes one or more open issues.

Please squash the commits included in a pull request if possible.

[conventional-commits]: https://www.conventionalcommits.org/
