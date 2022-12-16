import number_theory_functions

class RSA():
    def __init__(self, public_key, private_key = None):
        self.public_key = public_key
        self.private_key = private_key

    @staticmethod
    def generate(digits = 10):
        """
        Creates an RSA encryption system object

        Parameters
        ----------
        digits : The number of digits N should have

        Returns
        -------
        RSA: The RSA system containing:
        * The public key (N,e)
        * The private key (N,d)
        """
        while(True):
            m_p_prime = number_theory_functions.generate_prime(digits//2)
            m_q_prime = number_theory_functions.generate_prime(digits//2 + digits%2)
            m_N = m_p_prime * m_q_prime
            if len(str(m_N)) == digits :
                break
        m_K = (m_p_prime-1) * (m_q_prime-1)
        m_e = number_theory_functions.randrange(1,m_K)
        while number_theory_functions.extended_gcd(m_e, m_K)[0] != 1:
            m_e = number_theory_functions.randrange(1,m_K)
        m_d = number_theory_functions.modular_inverse(m_e,m_K)
        public_key = (m_N, m_e)
        private_key = (m_N, m_d)
        return RSA(public_key, private_key)

    def encrypt(self, m):
        """
        Encrypts the plaintext m using the RSA system

        Parameters
        ----------
        m : The plaintext to encrypt

        Returns
        -------
        c : The encrypted ciphertext
        """
        c = number_theory_functions.modular_exponent(m, self.public_key[1], self.public_key[0])
        return c


    def decrypt(self, c):
        """
        Encrypts the plaintext m using the RSA system

        Parameters
        ----------
        m : The plaintext to encrypt

        Returns
        -------
        c : The encrypted ciphertext
        """
        m = number_theory_functions.modular_exponent(c, self.private_key[1], self.private_key[0])
        return m
