'''HackerRank
Validate List of Email Addresses With Filter
https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem
'''


def fun(s):
    # return True if s is a valid email, else return False
    try:
        username, domain = s.split('@')
        domain_name, extension = domain.split('.')
    except ValueError:
        return False
    
    if not username.replace('-', '').replace('_', '').isalnum():
        return False
    
    if not domain_name.isalnum():
        return False
    
    if len(extension) > 3 or not extension.isalnum():
        return False
    
    return True
    

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())


filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)