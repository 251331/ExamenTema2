import requests

class Client:
    """Clase para manejar la conexión y recuperación de datos desde una API."""

    BASE_URL = "https://671be4322c842d92c381a5dc.mockapi.io/Music"

    def get_data(self):
        """Obtiene los datos de la API.

        Returns:
            list: Lista de registros en formato JSON, o None si hay un error.
        """
        try:
            response = requests.get(self.BASE_URL)
            response.raise_for_status()  # Levanta un error si la respuesta fue un código de estado de error
            return response.json()
        except requests.exceptions.ConnectionError:
            print("Error de conexión. Verifica tu conexión a internet.")
        except requests.exceptions.Timeout:
            print("La solicitud ha caducado.")
        except requests.exceptions.RequestException as e:
            print(f"Error de conexión: {e}")

        return []
