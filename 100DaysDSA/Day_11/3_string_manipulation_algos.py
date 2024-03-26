### String manipulation algorithms involve processing and transforming strings to achieve specific goals. 
    ## These algorithms can be used for tasks such as string searching, pattern matching, string comparison, and string hashing

## 1. Rabin-Karp Algorithm:
    ## The Rabin-Karp algorithm is a string searching algorithm that utilizes hashing to find occurrences of a pattern string within a larger text string. 
    
    ## It is particularly useful when searching for multiple patterns or when the pattern is relatively long compared to the text.

    ## The key idea behind the Rabin-Karp algorithm is to compute a hash value for the pattern and then compare it with the hash values of substrings of the text. 

    ## If the hash values match, the algorithm performs a character-by-character comparison to verify if the substring is an actual match.

def rabin_karp_search(pattern, text, prime=101):
    m = len(pattern)
    n = len(text)
    pattern_hash = 0
    text_hash = 0
    h = 1

    for i in range(m - 1):
        h = (h * 256) % prime

    for i in range(m):
        pattern_hash = (256 * pattern_hash + ord(pattern[i])) % prime
        text_hash = (256 * text_hash + ord(text[i])) % prime

    for i in range(n - m + 1):
        if pattern_hash == text_hash:
            if pattern == text[i:i+m]:
                print("Pattern found at index", i)

        if i < n - m:
            text_hash = (256 * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
            if text_hash < 0:
                text_hash += prime

# Example usage
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
rabin_karp_search(pattern, text)

## The algorithm starts by computing the hash values of the pattern and the first substring of the text using a rolling hash function. 

  ## It then compares the hash values and performs a character-by-character comparison if the hash values match.    ## If a match is found, it prints the index where the pattern occurs in the text.

## Time compelxity
    ## The Rabin-Karp algorithm has a time complexity of O(m + n) in the average