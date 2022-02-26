<p style="text-align: center;">
<img src="docs/logo/Logo_TransForLight.png" height="120px"/>

![](https://img.shields.io/github/repo-size/TSURIS/cli-assistant?style=for-the-badge) ![](https://img.shields.io/github/license/TSURIS/cli-assistant?style=for-the-badge)

</p>
  
# TSURIS CLI Assistant

The Command Line Interface (CLI) to the **T**echnologically **S**ufficient **U**ser **R**eaction **I**nformation **S**ystem (TSURIS) personal assistant.

## Developer Workstation Set Up

Below are the steps a developer should take to get his/her project set up locally.

## STEP 0: Clone this repository

This might be obvious, but:

```bash
git clone git@github.com:TSURIS/cli-assistant.git
```

Optionally, upgrade pip and wheel too:

```bash
python -m pip install --upgrade pip setuptools wheel
```

## STEP 1: Add an `.env` file.

In your `src` folder, add an `.env` file with the various values used by this system. Below is an empty starter as a template:

```text
USERNAME=Rob
USER_EMAIL=rob@example.com
BOTNAME=TSURIS
EMAIL_ACCOUNT=None
EMAIL_PASSWORD=None
NEWS_API_KEY=None
OPENWEATHER_APP_ID=None
TMDB_API_KEY=None
```

> ### NOTE:
> The product owner will provide these values to you offline. The `.env` file is for your workstation. That sensitive data is NOT stored in github.

## STEP 2: Create a Python "virtual environment"

We want to create a localized Python environment where we can install out 3rd-party components. From the `src` folder, run the following:

```powershell
python -m venv venv
```

This will create a virtual envirment in `/src/venv/`. To "activate" that virtual environment:

### Windows

```powershell
.\venv\Scripts\Activate.ps1
```

### Linux or macOS

```bash
source ./venv/bin/activate
```

## STEP 3: Install 3rd Party Dependencies

From that same `src` folder, run:

```bash
pip install -r ./requirements.txt
```

## STEP 4: Run

Finally, run the program with:

```bash
python ./main.py
```
