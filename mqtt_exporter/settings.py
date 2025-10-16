"""Exporter configuration."""

import os

PREFIX = os.getenv("PROMETHEUS_PREFIX", "mqtt_")
TOPIC_LABEL = os.getenv("TOPIC_LABEL", "topic")
TOPIC = os.getenv("MQTT_TOPIC", "#")
IGNORED_TOPICS = os.getenv("MQTT_IGNORED_TOPICS", "").split(",")
ZWAVE_TOPIC_PREFIX = os.getenv("ZWAVE_TOPIC_PREFIX", "zwave/")
ESPHOME_TOPIC_PREFIXES = os.getenv("ESPHOME_TOPIC_PREFIXES", "").split(",")
HUBITAT_TOPIC_PREFIXES = os.getenv("HUBITAT_TOPIC_PREFIXES", "hubitat/").split(",")
EXPOSE_LAST_SEEN = os.getenv("EXPOSE_LAST_SEEN", "False") == "True"
PARSE_MSG_PAYLOAD = os.getenv("PARSE_MSG_PAYLOAD", "True") == "True"


ZIGBEE2MQTT_AVAILABILITY = os.getenv("ZIGBEE2MQTT_AVAILABILITY", "False") == "True"
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_MQTT_MESSAGE = os.getenv("LOG_MQTT_MESSAGE", "False") == "True"
MQTT_ADDRESS = os.getenv("MQTT_ADDRESS", "127.0.0.1")
MQTT_PORT = int(os.getenv("MQTT_PORT", "1883"))
MQTT_KEEPALIVE = int(os.getenv("MQTT_KEEPALIVE", "60"))
MQTT_USERNAME = os.getenv("MQTT_USERNAME")
MQTT_PASSWORD = os.getenv("MQTT_PASSWORD")
MQTT_V5_PROTOCOL = os.getenv("MQTT_V5_PROTOCOL", "False") == "True"
MQTT_CLIENT_ID = os.getenv("MQTT_CLIENT_ID", "")
MQTT_EXPOSE_CLIENT_ID = os.getenv("MQTT_EXPOSE_CLIENT_ID", "False") == "True"
MQTT_ENABLE_TLS = os.getenv("MQTT_ENABLE_TLS", "False") == "True"
MQTT_TLS_NO_VERIFY = os.getenv("MQTT_TLS_NO_VERIFY", "False") == "True"
PROMETHEUS_ADDRESS = os.getenv("PROMETHEUS_ADDRESS", "0.0.0.0")
PROMETHEUS_PORT = int(os.getenv("PROMETHEUS_PORT", "9000"))

KEEP_FULL_TOPIC = os.getenv("KEEP_FULL_TOPIC", "False") == "True"


# Database settings
USE_DB_TOPICS = os.getenv("USE_DB_TOPICS", "False") == "True"
DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_NAME = os.getenv("DB_NAME", "mqtt_exporter")
DB_TABLE = os.getenv("DB_TABLE", "mqtt_topics")
DB_PREFIXES = os.getenv("DB_PREFIXES", "fleetos/device/status/").split(",")
DB_REFRESH_INTERVAL = int(os.getenv("DB_REFRESH_INTERVAL", "300"))
