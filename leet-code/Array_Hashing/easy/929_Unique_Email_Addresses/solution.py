class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        email_set = set()
        for email in emails:
            email_formated = ""
            for i, c in enumerate(email):
                if c =="+" or c == "@":
                    email_formated += email[email.find("@"):  len(email)]
                    break
                if c.isalpha():
                    email_formated += c
                
            print(email_formated)
            email_set.add(email_formated)
        return len(email_set)

def main():
    solution = Solution()
    emails = [ "test.email+alex@leetcode.com", "test.email@leetcode.com"]

    result = solution.numUniqueEmails(emails)
    print('result',result)
    
if __name__ == "__main__":
    main()