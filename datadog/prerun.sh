#!/bin/bash

echo "ENABLING LOGS...."
echo "datadog-agent status"
datadog-agent status
echo "logs_enabled: true" >> /app/.apt/etc/datadog-agent/datadog.yaml