# Discrete Element Modeling to Robotic Fabrication using the COMPAS framework

[📃 COMPAS docs](https://compas.dev)

## Requirements

* Minimum OS: Windows 10 Pro or Mac OS Sierra 10.12
* [Anaconda 3](https://www.anaconda.com/distribution/)
* [Visual Studio Code](https://code.visualstudio.com/) with the `Python` and `Pylance` extensions from Microsoft.
* [Rhino 7/8](https://www.rhino3d.com/download) (Optional :))
* [Blender 4.1](https://www.blender.org/download/) (Optional)

## Help

If you need help with the installation process, please post a note on the workshop Slack channel: [Join Slack](https://join.slack.com/t/slack-hnb7978/shared_invite/zt-2imngbpna-IaENmF68m85vPmAFhcbamA)

## Installation

> **IMPORTANT**: If you're on Windows, all commands below have to be executed in the *Anaconda Prompt* (NOT the *Command Prompt*)

We use `conda` to make sure we have clean, isolated environment for dependencies.

First time using <code>conda</code>? Make sure to run this at least once:

    conda config --add channels conda-forge

Then create the workshop environment and install the dependencies:

    conda env create -f https://raw.githubusercontent.com/compas-Workshops/BFH24/main/env_win.yml

> **IMPORTANT**: If you're on Windows, use `env_win.yml`. On Mac, use `env_osx.yml`.

### Verify installation

Activate the environment

    conda activate bfh24

> **NOTE**: You should see that your prompt changed from `(base)` to `(bhf24)`

Run the verification command `python -m compas`:

    (bfh24) python -m compas

    Yay! COMPAS is installed correctly!

    COMPAS: 2.1.0
    Python: 3.10.0 (CPython)
    Extensions: ['compas-assembly', 'compas', 'compas-fea2', 'compas-model', 'compas-ifc', 'compas-viewer', 'compas-fea2-opensees', 'compas-dr', 'compas-fd', 'compas-occ', 'compas-cra', 'compas-notebook', 'compas-gmsh']
