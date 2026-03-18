#!/bin/bash
set -e
echo "Starting Decentralized Voting System on Web3..."
uvicorn app:app --host 0.0.0.0 --port 9033 --workers 1
