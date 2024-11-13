# CLAIF CLI
## References
Command Line Interface for the CLAIF API which can be found at https://github.com/claif-api.
This CLI is to be used with the CLAIF Annotator https://github.com/arthurwolf/annotator.

The CLAIF API and CLAIF Annotator are available at https://api-staging.claif.org and https://annotator-staging.claif.org respectively.

## About the project
### Improving the quality of Large Language Models (LLMs) for programming
This project (https://claif.org) aims to improve LLM training data for developers by capturing the data generated during programming sessions. Most LLMs used for programming are trained on code commits and they don't capture live programming sessions. This project aims to capture the data generated during live programming sessions - every character that is input or output in a terminal is captured. This data can be used to create a free and open-source LLM (Large Language Model).

### Actually respecting the copyright of the training data
Most LLMs used for programming are trained on public repositories and they violate the copyright of the code authors by not making it fully tansparent what data was used to train the model and how that constitutes its overall license. This project aims to respect the copyright of the code authors by making the training data fully transparent.

## About the CLAIF CLI
The CLAIF CLI is a command-line tool used to interact with the CLAIF API. It allows users to upload, read, update, and delete terminal recordings and audio recordings. These recordings can be annotated using the CLAIF Annotator.

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
After creating an asciinema recording, you can upload it to the CLAIF API.

Currently this makes the recording available to all users to read/update/delete. Make sure to find/replace any sensitive information in the recording before uploading.

The recording will be preserved in the database and any updates (including ones with annotations) will be associated with the original recording.
```bash
poetry run python -m claif_cli --base-url "https://api-staging.claif.org/v1" create-recording "<asciinema_recording_filepath>" "<title>" "<description>"
```
Example:
```bash
poetry run python -m claif_cli --base-url "https://api-staging.claif.org/v1" create-recording "haskell_llm_2_1.txt" "Haskell LLM - 2.1" "Creating an LLM with Haskell - 2.1"
```
### Upload/Create Audio Recording and Transcription
If you have created an audio recording of your solo or pair-programming session, you can upload it to the CLAIF API where the data will be used to help train the LLM to associate the audio recordings with terminal recordings. After the audio recording is uploaded, it will be audomatically transcribed. The transcription can then be annotated using the CLAIF Annotator (not yet implemented).

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

## Update
### Update Terminal Recording
After annotating or changing title/description of an asciinema recording, you can upload your changes to the CLAIF API.

It will increment the revision number, and create a new set of annotation objects associated with that revision. The original recording will be preserved and only the annotation data will be sent to the CLAIF API.

If you need to update the recording itself, you must create a new recording and make a deletion request for the old one (not yet implemented).
```bash
poetry run python -m claif_cli --base-url "https://api-staging.claif.org/v1" update-recording "<recording_id>" "<recording_filepath:optional>" "<title:optional>" "<description:optional>"
```

## Coming Soon
- Get terminal recording
- More granular access and sharing controls
- Request Deletion of terminal recording
- Get audio recording
- Request Deletion of audio recording
- Get audio transcription
- Update audio transcription
- List all audio recordings
- List all audio transcriptions
- Get a annotation details
- List all annotations for a recording
- Get all annotation reviews for a recording (by revision #)
- Llama.cpp endpoints for general use
- Llama.cpp endpoints for generating training data from audio recordings/transcriptions and terminal recordings/annotations