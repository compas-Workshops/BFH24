# Discrete Element Modeling to Robotic Fabrication using the COMPAS framework

[📃 COMPAS docs](https://compas.dev)

## Requirements

* Minimum OS: Windows 10 Pro or Mac OS Sierra 10.12
* [Anaconda 3](https://www.anaconda.com/distribution/)
* [Rhino 7/8](https://www.rhino3d.com/download)
* [Visual Studio Code](https://code.visualstudio.com/)

## Help

If you need help with the installation process, please post a note on the workshop Slack channel: [Join Slack](https://join.slack.com/t/slack-hnb7978/shared_invite/zt-2imngbpna-IaENmF68m85vPmAFhcbamA)

## Installation

> **IMPORTANT**: If you're on Windows, all commands below have to be executed in the *Anaconda Prompt* (NOT the *Command Prompt*)

We use `conda` to make sure we have clean, isolated environment for dependencies.

First time using <code>conda</code>? Make sure to run this at least once:

    (base) conda config --add channels conda-forge

Then create the workshop environment and install the dependencies:

    (base) conda env create -f https://raw.githubusercontent.com/compas-Workshops/BFH24/main/env_win.yml

> **IMPORTANT**: If you're on Windows, use `env_win.yml`. On Mac, use `env_osx.yml`.

### Verify installation

    (base) conda activate bfh24
    (bfh24) python -m compas

    Yay! COMPAS is installed correctly!

    COMPAS: 2.1.0
    Python: 3.9.0 (CPython)
    Extensions: ['compas-model', 'compas-viewer', 'compas-occ', 'compas-cra', 'compas-assembly', 'compas-notebook']
