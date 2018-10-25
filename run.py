from eve import Eve
import ssl

app = Eve()
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain('certificate.pem', 'key.pem')

if __name__ == '__main__':
    app.run(ssl_context=context, debug=True)