#!/bin/bash
mkdir /app/.apt/etc/datadog-agent/conf.d/custom_log_collect.d
touch /app/.apt/etc/datadog-agent/conf.d/custom_log_collect.d/conf.yaml
cat /app/datadog/conf.d/python.d/logs.yaml >> /app/.apt/etc/datadog-agent/conf.d/custom_log_collect.d/conf.yaml
