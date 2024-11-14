import os
from app import app

if_name_ == "_main_":
port = int(os.environ.get("PORT", 4000)) # Get the port from envi
app.run(host="0.0.0.0", port=port)
