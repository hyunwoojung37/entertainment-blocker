from main import TaskBlocker


user_response = input("Would you like to block or unblock? (B/U) \n")
cleaned_response = user_response.lower()

if cleaned_response == "b":
    print("Enter websites you'd like to block in this format")
    print("(Ex: Youtube.com, Instagram.com, Tiktok.com) \n")
    user_input = input()
    site_list = [site.strip() for site in user_input.split(",")]
    blocked = TaskBlocker(site_list)
    blocked.block_sites()
elif cleaned_response == "u":
    print("Enter websites you'd like to block in this format")
    print("(Ex: Youtube.com, Instagram.com, Tiktok.com) \n")
    user_input = input()
    site_list = [site.strip() for site in user_input.split(",")]
    unblocked = TaskBlocker(site_list)
    unblocked.unblock_sites()
else:
    print("Input wasn't recognized")
