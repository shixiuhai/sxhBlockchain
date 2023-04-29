import hashlib
def valid_proof(transactions, last_hash, nonce, difficulty=1):
        """
        Check if a hash value satisfies the mining conditions. This function is used within the proof_of_work function.
        """
        guess = (str(transactions)+str(last_hash)+str(nonce)).encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:difficulty] == '0'*difficulty
if __name__=="__main__":
    nonce=0
    while valid_proof("[]", '278b8bca466', '11',1) is False:
        print('--')
        nonce += 1
    print(nonce)