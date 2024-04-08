class Email:
    def __init__(self, content: str):
        if not isinstance(content, str):
            raise TypeError("Please provide a string")
        
        if "@" not in content:
            raise TypeError("Doesn't have an '@' sign")
        
        # Ends with .com/.edu/.net/.org
        valid_tlds: list[str] = [".com", ".edu", ".net", ".net", "org"]
        
        tld = content[-4:]
        if tld not in valid_tlds:
            raise TypeError("Invalid TLD")

        # Check for domain (stuff betweeen @ and .com)
        at_sign_index = content.find("@") + 1
        domain_start = content[at_sign_index:-4]
        if domain_start == "":
            raise TypeError("Invalid domain")
        
        # Make sure there is stuff before @
        if content.find("@") == 0:
            raise TypeError("Invalid user")

        self.content = content

    def __str__(self) -> str:
        return self.content

        
