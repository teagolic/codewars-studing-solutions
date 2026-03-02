def is_pangram(st):
    alphabet = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    st = st.lower()
    for letter in alphabet.split():
        if not letter in st:
            return False
    return True
