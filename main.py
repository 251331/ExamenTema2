from AppiClient import Client
from ui import HITMusicApp

def main():
    app = HITMusicApp()
    api_client = Client()  # Cambié AppiClient a api_client para mayor claridad

    data = api_client.get_data()
    app.load_data(data)  # Carga los datos solo si no hay errores

    app.run()

if __name__ == '__main__':
    main()
