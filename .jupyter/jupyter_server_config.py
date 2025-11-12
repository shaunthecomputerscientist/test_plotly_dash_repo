import os

# Force Voilà to bind to Render’s exposed network interface and port
c.ServerApp.ip = "0.0.0.0"
c.ServerApp.port = int(os.environ.get("PORT", 8866))
c.ServerApp.allow_origin = "*"
c.ServerApp.open_browser = False
c.VoilaConfiguration.theme = "dark"
