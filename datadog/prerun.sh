#!/bin/bash

echo "ENABLING LOGS...."
echo "sudo datadog-agent status"
sudo datadog-agent status
echo "logs_enabled: true" >> /app/.apt/etc/datadog-agent/datadog.yaml