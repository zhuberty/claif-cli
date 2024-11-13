# claif-cli

# Installation
## Install Poetry (Python package manager)
Debian/Ubuntu:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Windows:
```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

## Install claif-cli
```bash
poetry install
```

# Usage
## Log In
```bash
poetry run python -m claif_cli --base-url https://api-staging.claif.org/v1 login

Username: your_username
Password: ********

Login successful! Access token saved.
```
Token is saved in the current directory (`access_token.json`). It expires after 30 minutes and will prompt you to login again.

## Create
### Upload/Create Terminal Recording
```bash
poetry run python -m claif_cli --base-url "https://api-staging.claif.org/v1" create-recording "<recording_filepath>" "<recording_title>" "<recording_description>"
```
Example:
```bash
poetry run python -m claif_cli --base-url "https://api-staging.claif.org/v1" create-recording "haskell_llm_2_1.txt" "Haskell LLM - 2.1" "Creating an LLM with Haskell - 2.1"
```
### Upload/Create Audio Recording and Transcription
```bash
poetry run python -m claif_cli --base-url "https://api-staging.claif.org/v1" create-audio "<audio_filepath>"
```
Example:
```bash
poetry run python -m claif_cli --base-url "https://api-staging.claif.org/v1" create-audio "haskell_session.wav"
```

## Read
### List All Terminal Recordings
```bash
poetry run python -m claif_cli --base-url "https://api-staging.claif.org/v1" list-recordings
```
Example:
```bash
poetry run python -m claif_cli --base-url "https://api-staging.claif.org/v1" list-recordings

+------+------------+------------+---------+--------+------------+-----------+
|   ID | Title      |   Revision |   Annos | Size   | Duration   | Creator   |
+======+============+============+=========+========+============+===========+
|    1 | Example    |          6 |      84 | 15KB   | 1527s      | some_user |
+------+------------+------------+---------+--------+------------+-----------+
```

### Get Terminal Recording
```bash
poetry run python -m claif_cli --base-url "https://api-staging.claif.org/v1" get-recording "<recording_id>"
```
