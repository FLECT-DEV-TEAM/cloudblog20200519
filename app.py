from flask import Flask, request, jsonify, abort

import logging
import ssl
import json, os, sys, glob

#######################
#### Utilities ########
#######################
app = Flask(__name__, static_folder='./build/', static_url_path="/")

#app = Flask(__name__, static_folder='./public/')
if __name__ == '__main__':
    print(app.url_map)
    #context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    #context.load_cert_chain('server.crt', 'server.key')

    print('start')
    files = glob.glob('./*')
    print(files)
    files = glob.glob('./build/*')
    print(files)

    port = int(os.environ.get("PORT", 38888))
    #app.run(debug=True, use_reloader=False, host='0.0.0.0', port=port,  ssl_context=context, threaded=True)
    app.run(host='0.0.0.0', port=port)

    print('......')
