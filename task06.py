def find_palindromes(sentence):
    words = sentence.split()
    palindromes = [word for word in words if word == word[::-1]]
    return palindromes
input_sentence = "olol radar makka non"
output_palindromes = find_palindromes(input_sentence)
print(output_palindromes)

