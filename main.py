from stellar_sdk import Server, Keypair, TransactionBuilder, Network

server = Server("https://horizon-testnet.stellar.org")

sender_secret_key = "YOUR_SENDER_SECRET_KEY"

recipient_public_key = "RECIPIENT_PUBLIC_KEY"

amount = "10"

def send_payment(sender_secret_key, recipient_public_key, amount):
    sender_keypair = Keypair.from_secret(sender_secret_key)
    sender_account = server.load_account(sender_keypair.public_key)

    transaction = (
        TransactionBuilder(
            source_account=sender_account,
            network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
            base_fee=100
        )
        .append_payment_op(recipient_public_key, amount, "XLM")
        .set_timeout(30)
        .build()
    )

    transaction.sign(sender_keypair)

    response = server.submit_transaction(transaction)
    print(f"Payment sent! Hash: {response['hash']}")

if __name__ == "__main__":
    send_payment(sender_secret_key, recipient_public_key, amount)
