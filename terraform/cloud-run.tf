provider "google" {
  credentials = "${var.GCP_CREDENTIALS}"
  project     = "ab-architecture"
  region      = "europe-west1"
  zone        = "europe-west1-c"
}

variable SERVICE_NAME {
}
variable DOCKER_IMAGE_LOCATION {
}

resource "google_cloud_run_v2_service" "default" {
  name     = var.SERVICE_NAME
  location = "europe-west1"
  ingress = "INGRESS_TRAFFIC_ALL"

  template {
    containers {
      image = var.DOCKER_IMAGE_LOCATION
    }
  }
}