#!/bin/bash
cd object
gcloud compute scp detect.py instance-1:~
cd ..