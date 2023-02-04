from flask import Flask, request

app = Flask(__name__)

@app.route('/.well-known/acme-challenge/<token>')
def acme_challenge(token):
    return "QDGx_vbCWQp18g05Zt03qivnjxsZyEGepPU-z8Ko8fs.T8FB3aRhNtUW0M9QjmY_biiW_CMX-X3uk3K9BvaRIU0"

if __name__ == '__main__':
    app.run(port=10000)
