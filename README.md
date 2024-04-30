# deployed-hello-world
An extraordinarily simple hello-world application which mostly serves to demonstate a functional app+infrastructure pipeline deployment to our sandbox cluster. 

# Usage as a template
1. Fork this Repo and clone it locally, using your git method of choice
2. (Mac/Linux Users) run ./local-setup.sh
3. Follow the link in your terminal, appending /hello-world (i.e. http://127.0.0.1:5000/hello-world)
4. Modify as required

# Configuring the deployment elements

(Note: You'll need to establish your artefact registry details prior to completing this step.)

1. Define the following Github variables
1.1. APP_NAME : E.g. my-hello-world-app (lowercase with optional dashes only)
1.2. ARTEFACT_REGISTRY_HOSTNAME: E.g. europe-west2.docker.pkg.dev
1.3. ARTEFACT_REGISTRY_ROOT: E.g. europe-west2.docker.pkg.dev/something/my-hello-world-app
1.4. GCP_ZONE: E.g. europe-west2
1.5. GCP_PROJECT_NAME: E.g. my-project

2. Define the following Github Secrets
(Note: You'll need to establish a suitable service-account prior to completing these steps. It's possible to be more granular, but roles/iam.serviceAccountUser, roles/run.admin, roles/storage.admin, roles/artefactregistry.writer and roles/artefactregistry.reader will allow this pipeline to function.
)
2.1 GCP_CREDENTIALS: The JSON representation of your Service Account key
2.2 GCP_CREDENTIALS_BASE64: The base64 encoded version of your Service Account key

# The basic functionality of the Github Actions is described below
1. Builds a gunicorn-based python container image
2. Uploads that image to your defined container registry
3. Creates a GCP CloudRun instance in unauthenticated mode. 