'''
Algorytm Rabina-Karpa
O ( m + n )
'''

def find_pattern(text, pattern):
    d = 256             # dlugosc alfabetu
    prime = 997         # jakas liczba pierwsza do hashowania
    n = len(text)
    m = len(pattern)
    k = pow(d, m-1) % prime
    pattern_hash = 0
    subtext_hash = 0

    for i in range(m):
        pattern_hash = (d*pattern_hash + ord(pattern[i])) % prime
        subtext_hash = (d*subtext_hash + ord(text[i])) % prime

    for i in range(n-m+1):
        if pattern_hash == subtext_hash:
            for j in range(m):
                found_pattern = True
                if text[i+j] != pattern[j]:
                    found_pattern = False
                    break
            if found_pattern:
                print("Pattern found at index: ", i)

        if i < n-m:
            subtext_hash = (d*(subtext_hash - ord(text[i])*k) + ord(text[i+m])) % prime
            if subtext_hash < 0:
                subtext_hash += prime


find_pattern("Twoja staa sra do gara", "ara")