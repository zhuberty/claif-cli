import argparse
from .auth_utils import login
from .recordings import (
    review_recording,
    create_recording,
    update_recording,
    list_recordings,
)
from claif_cli.audio_files import create_audio_file

DEFAULT_URL = "http://localhost:8000/v1"


def main():
    parser = argparse.ArgumentParser(description="CLI tool for interacting with FastAPI app.")
    parser.add_argument("--base-url", default=DEFAULT_URL, help="Base URL of the FastAPI app")
    parser.add_argument("--password", help="Don't use this for prod environments. Provide password directly for testing purposes")

    subparsers = parser.add_subparsers(dest="command")

    login_parser = subparsers.add_parser("login", help="Login to the FastAPI app")
    login_parser.add_argument("--password", help="Password for testing purposes")

    review_recording_parser = subparsers.add_parser("review-recording", help="Review a recording")
    review_recording_parser.add_argument("recording_id", type=int, help="ID of the recording to review")
    review_recording_parser.add_argument("--revision-number", type=int, help="Revision number of the recording")

    create_recording_parser = subparsers.add_parser("create-recording", help="Create a new recording")
    create_recording_parser.add_argument("recording_filepath", help="Path to the recording file")
    create_recording_parser.add_argument("recording_title", help="Title of the recording")
    create_recording_parser.add_argument("recording_description", help="Description of the recording")

    update_recording_parser = subparsers.add_parser("update-recording", help="Update an existing recording")
    update_recording_parser.add_argument("recording_id", type=int, help="ID of the recording to update")
    update_recording_parser.add_argument("--recording_filepath", help="Path to the updated recording file")
    update_recording_parser.add_argument("--title", help="New title for the recording")
    update_recording_parser.add_argument("--description", help="New description for the recording")

    list_recordings_parser = subparsers.add_parser("list-recordings", help="List all recordings")

    create_audio_file_parser = subparsers.add_parser("create-audio-recording", help="Create a new audio file")
    create_audio_file_parser.add_argument("audio_filepath", help="Path to the audio file")
    
    args = parser.parse_args()

    base_url = args.base_url

    if args.command == "login":
        login(base_url, password=args.password)
    elif args.command == "review-recording":
        review_recording(base_url, args.recording_id, args.revision_number)
    elif args.command == "create-recording":
        create_recording(
            base_url, 
            args.recording_filepath, 
            args.recording_title, 
            args.recording_description
        )
    elif args.command == "update-recording":
        update_recording(
            base_url, 
            args.recording_id, 
            recording_filepath=args.recording_filepath,
            title=args.title, 
            description=args.description
        )
    elif args.command == "list-recordings":
        list_recordings(base_url)
    elif args.command == "create-audio-recording":
        create_audio_file(base_url, args.audio_filepath)


if __name__ == "__main__":
    main()
