---
title: Consistent Configuration
---

-   Got into a state during the previous changes where `isort` and `black` disagreed with each other
-   Solution is to tell `isort` to use the `black` profile (i.e., its style rules)
-   Can be done with `--profile black`
-   Or put configuration values in `setup.cfg`
    -   While we're here, tell `flake8` that we're OK with 80-character lines

```
[flake8]
max-line-length = 80

[isort]
profile = black
```

-   Use a configuration file because people are more likely to look there than in a task description
-   Not all (Python) tools know how to read from `setup.cfg`
