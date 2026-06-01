import requests


class CrossrefService:

    BASE_URL = "https://api.crossref.org/works"

    @staticmethod
    def verify_doi(doi: str):

        try:

            response = requests.get(
                f"{CrossrefService.BASE_URL}/{doi}",
                timeout=2,
            )

            return response.status_code == 200

        except Exception:
            return False