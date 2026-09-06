class TaskBlocker:
    # Initializing sites and IP of OS
    def __init__(self, sites: list[str], redirectedIP: str = "127.0.0.1"):
        self.sites = sites
        self.redirectedIP = redirectedIP
        self.hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
    # Access files and read
    def block_sites(self):
    # open file to read 
        with open(self.hosts_path, "r") as file:
            content = file.read()

        with open(self.hosts_path, "a") as file:
            for site in self.sites:
                modifiedLine = self.redirectedIP + " " + site
                if modifiedLine not in content:
                    file.write(f"{modifiedLine}\n")
                else:
                    pass
                    
        
""""function block_sites():
    open hosts_path for reading
    read all existing lines into a list (call it existing_lines)
    close file

    open hosts_path in append mode
    for each site in self.sites:
        line_to_add = self.redirectedIP + " " + site

        if line_to_add is NOT already in existing_lines:
            write line_to_add to file (with a newline at the end)
        else:
            skip it (already blocked, don't duplicate)
    close file

"""