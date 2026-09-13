# things to do : test out functions and work on next, see what issues arise
class TaskBlocker:
    # initialize sites ip and host path
    def __init__(self, sites: list[str], redirectedIP: str = "127.0.0.1"):
        self.sites = sites
        self.redirectedIP = redirectedIP
        self.hosts_path = r"C:\Windows\System32\drivers\etc\hosts"

    def block_sites(self):
        # read hosts path or history and ip
        with open(self.hosts_path, "r") as file:
            content = file.read()

        # adding websites to block into content
        with open(self.hosts_path, "a") as file:
            for site in self.sites:
                block_entry = self.redirectedIP + " " + site
                if block_entry not in content:
                    file.write(f"{block_entry}\n")
                else:
                    pass

    def unblock_sites(self):
        # reads out each website stored
        with open(self.hosts_path, "r") as file:
            hosts_lines = file.readlines()
        lines_to_keep = []

        # checks if websites in host lines matches hosts path
        for hosts_line in hosts_lines:
            should_remove = False
            for site in self.sites:
                block_entry = self.redirectedIP + " " + site
                if block_entry in hosts_line:
                    should_remove = True
        # if so remove, else keep in new list
            if should_remove is False:
                lines_to_keep.append(hosts_line)

        # overwrite all hosts path with just the lines we keep
        with open(self.hosts_path, "w") as file:
            for hosts_line in lines_to_keep:
                file.write(hosts_line)
