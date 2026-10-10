from main import TaskBlocker
from submission import read_submission


cleaned_response = None

while cleaned_response != "":
    user_response = input("Block, Unblock, View All, or Submit? (B/U/V/S) \n")
    cleaned_response = user_response.lower()

    if cleaned_response == "b":
        print("Enter websites you'd like to block in this format")
        print("(Ex: Youtube.com, Instagram.com, Tiktok.com) \n")
        user_input = input()
        site_list = [site.strip().lower() for site in user_input.split(",")]
        blocked = TaskBlocker(site_list)
        blocked.block_sites()
    elif cleaned_response == "u":
        print("Enter websites you'd like to block in this format")
        print("(Ex: Youtube.com, Instagram.com, Tiktok.com)\n")
        print("If you want to unblock all, type CLEAR")
        user_input = input()
        if user_input.lower() == "clear":
            cleared = TaskBlocker([])
            cleared.clear_unblocked_sites()
        else:
            site_list = [site.strip().lower() for site in user_input.split(",")]
            unblocked = TaskBlocker(site_list)
            unblocked.unblock_sites()
    elif cleaned_response == "v":
        viewed = TaskBlocker([])
        blocked_list = viewed.view_blocked_sites()
        print(blocked_list)
    elif cleaned_response == "s":
        assignment_instructions = input("What were the instructions\n")
        submitted_work = input("Submit your work here\n")
        submission_content = read_submission(submitted_work)
        cleaned_submission_content = submission_content.strip()
        if cleaned_submission_content == "":
            print("File is empty")
            exit

        print("Assignment instructions:")
        print(assignment_instructions)
        print("submitted Work:")
        print(submission_content)

    else:
        print("Input wasn't recognized")
