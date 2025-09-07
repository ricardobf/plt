# import requests
# from .project import Project
# from .repository import Repository
# from plt.config import Settings


# class BitbucketError(Exception):
#   pass

# class Bitbucket:
#   def __init__(self):
#     """
#     Initialize Bitbucket client with the access token
#     """
#     self.access_token = Settings.BITBUCKET_ACCESS_TOKEN
#     if not self.access_token:
#       raise BitbucketError("Access token must be provided")

#     self.base_url = "https://api.bitbucket.org/2.0"

#     # Initialize session
#     self.session = requests.Session()
#     self.session.headers.update({
#       "Accept": "application/json",
#       "Content-Type": "application/json",
#       "Authorization": f"Bearer {self.access_token}"
#     })

#     # Initialize API resources
#     self.project = Project(self.session, self.base_url)
#     self.repository = Repository(self.session, self.base_url)
