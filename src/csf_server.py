# -*- coding: utf-8 -*-
from server import csfserver
if __name__ == "__main__":
    csfserver.run(debug=True, host="0.0.0.0", port=5000)
