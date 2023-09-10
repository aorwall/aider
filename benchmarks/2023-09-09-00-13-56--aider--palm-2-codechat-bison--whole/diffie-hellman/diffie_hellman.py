import random

def private_key(p):
  """Generates a private key between 1 and p-1.

  Args:
    p: A prime number.

  Returns:
    A private key.
  """
  # Generate a random number between 1 and p-1.
  private = random.randint(1, p - 1)

  # Return the private key.
  return private


def public_key(p, g, private):
  """Generates a public key from a private key.

  Args:
    p: A prime number.
    g: A generator.
    private: A private key.

  Returns:
    A public key.
  """
  # Calculate the public key.
  public = pow(g, private, p)

  # Return the public key.
  return public


def secret(p, public, private):
  """Generates a shared secret from a public key and a private key.

  Args:
    p: A prime number.
    public: A public key.
    private: A private key.

  Returns:
    A shared secret.
  """
  # Calculate the shared secret.
  secret = pow(public, private, p)

  # Return the shared secret.
  return secret
