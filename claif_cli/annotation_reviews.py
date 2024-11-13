from .api_requests import api_request


def create_review(base_url, annotation):
    print(f"Annotation text: {annotation['annotation_text']}")

    # Prompt the user for answers
    q_does_anno_match_content = input("Does the annotation match the content? (yes/no): ").strip().lower() == 'yes'
    q_can_anno_be_halved = input("Can the annotation be halved? (yes/no): ").strip().lower() == 'yes'
    q_how_well_anno_matches_content = int(input("How well does the annotation match the content (1-10): ").strip())
    q_can_you_improve_anno = input("Can you improve the annotation? (yes/no): ").strip().lower() == 'yes'
    q_can_you_provide_markdown = input("Can you provide markdown? (yes/no): ").strip().lower() == 'yes'

    payload = {
        "annotation_id": annotation['id'],
        "q_does_anno_match_content": q_does_anno_match_content,
        "q_can_anno_be_halved": q_can_anno_be_halved,
        "q_how_well_anno_matches_content": q_how_well_anno_matches_content,
        "q_can_you_improve_anno": q_can_you_improve_anno,
        "q_can_you_provide_markdown": q_can_you_provide_markdown,
    }
    return api_request(base_url, f"/annotation_reviews/create", method="POST", json=payload)
