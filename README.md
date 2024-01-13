# Python Project Template
[![Squad Badge](https://img.shields.io/badge/squad-p&d-blue)](https://img.shields.io/badge/squad-p&d-blue) 
[![Tech](https://img.shields.io/badge/tech-python-blue)](https://img.shields.io/badge/tech-python-blue)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

### Quickstart

```bash
python3 -m pip install -r requirements-dev.txt
pre-commit install
```

### Check Dependencies Vulnerabilities
```bash
safety check
```

### Using Commitizen

See [documentation](https://commitizen-tools.github.io/commitizen/getting_started/)

```bash
cz init

cz commit
```

### CHANGELOG

All notable changes to this project should be documented in CHANGELOG.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

```
## [0.0.7] - 2015-02-16
### Added
- New feature.
```

* `Added` for new features.
* `Changed` for changes in existing functionality.
* `Deprecated` for soon-to-be removed features.
* `Removed` for now removed features.
* `Fixed` for any bug fixes.
* `Security` in case of vulnerabilities.

### Bumping

The action will parse the new commits since the last tag using the [semantic-release](https://github.com/semantic-release/semantic-release) conventions.

semantic-release uses the commit messages to determine the type of changes in the codebase. Following formalized conventions for commit messages, semantic-release automatically determines the next [semantic version](https://semver.org) number.

By default semantic-release uses [Angular Commit Message Conventions](https://github.com/angular/angular.js/blob/master/DEVELOPERS.md#-git-commit-guidelines).

Here is an example of the release type that will be done based on a commit messages:

```
perf(pencil): remove graphiteWidth option

BREAKING CHANGE: The graphiteWidth option has been removed.
The default graphite width of 10mm is always used for performance reasons.
```

If no commit message contains any information, then **default_bump** will be used.

**Type**

Must be one of the following:

* `feat`: A new feature
* `fix`: A bug fix
* `docs`: Documentation only changes
* `style`: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
* `refactor`: A code change that neither fixes a bug nor adds a feature
* `perf`: A code change that improves performance
* `test`: Adding missing or correcting existing tests
* `build`: Changes to the build process or auxiliary tools and libraries such as documentation generation
