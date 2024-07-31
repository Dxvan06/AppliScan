import dns.resolver

def enumerate_subdomains(domain):
    subdomains = []
    try:
        answers = dns.resolver.resolve(domain, 'A')
        for answer in answers:
            subdomains.append(answer.to_text())
    except Exception as e:
        print(f"Error: {e}")
    return subdomains
