def numUniqueEmails(emails: list[str]) -> int:
    unique_emails = set()
    for email in emails:
        local, domain = email.split('@')
        local = local.split('+')[0]  # Remove everything after '+'
        local = local.replace('.', '')  # Remove all '.'
        unique_emails.add(local + '@' + domain)  # Store processed email

    return len(unique_emails)


# **Driver Code 
emails = ["test.email+alex@leetcode.com", 
         "test.e.mail+bob.cathy@leetcode.com", 
         "testemail+david@lee.tcode.com"]
    
result = numUniqueEmails(emails)
print(f"Number of unique emails: {result}")  # Expected Output: 2


#Leetcode - 929

