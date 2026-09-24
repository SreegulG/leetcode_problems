class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        s = set()
        for email in emails:
            local_name, domain = email.split("@")
            valid_local_name = local_name.split("+")[0]
            valid_local_name = "".join(valid_local_name.split("."))
            s.add(valid_local_name + domain)
        print(s)
        return len(s)
