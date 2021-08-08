from app import create_app
import config

app = create_app()
app.run(host=config.Config.SERVER, port=config.Config.PORT)