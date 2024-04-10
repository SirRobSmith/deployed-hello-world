provider "google" {
  credentials = "${file("/Users/rob/Downloads/ab-architecture-eba1ad488d71.json")}"
  project     = "ab-architecture"
  region      = "europe-west1"
  zone        = "europe-west1-c"
}

resource "google_storage_bucket" "static" {
  name          = "robsmith-new-bucket"
  location      = "EU"
  storage_class = "COLDLINE"

  uniform_bucket_level_access = true
}