#!/bin/bash

mkdir /etc/datadog-agent/conf.d/custom_log_collect.d
touch /etc/datadog-agent/conf.d/custom_log_collect.d/conf.yaml
cat /app/datadog/conf.d/python.d/logs.yaml >> /etc/datadog-agent/conf.d/custom_log_collect.d/conf.yaml
# echo "logs_enabled: true" >> /app/.apt/etc/datadog-agent/datadog.yaml