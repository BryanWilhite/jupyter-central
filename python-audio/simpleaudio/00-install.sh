#!/bin/bash

if [ `printenv CONDA_DEFAULT_ENV` == 'pip-only-env' ]
then
    pip install simpleaudio
fi
