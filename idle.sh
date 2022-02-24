#!/usr/bin/env bash
while true; do
        # out to stdout
        echo "stdout at $(date)"
        # out to stderr
        echo "stderr at $(date)" > &2
        sleep 1
done
