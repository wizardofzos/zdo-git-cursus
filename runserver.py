#
# This is the startup of the app
#

import os
from app import app

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 80))
    print port
    app.run(host='0.0.0.0', port=port)
