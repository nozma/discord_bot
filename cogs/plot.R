library(RSQLite)
library(dplyr)
library(dbplyr)
library(lubridate)
library(ggplot2)
library(tidyr)
library(patchwork)


con <- dbConnect(RSQLite::SQLite(), "/home/rito/db/remoData.db")

tbl(con, "remo") %>%
  select(time, mode, button) %>%
  rename(
    `運転モード` = mode,
    `エアコン` = button
  ) %>%
  collect() %>%
  mutate(
    time = as_datetime(time),
    `エアコン` = ifelse(エアコン == "power-off", "切", "入")
  ) %>%
  gather(key, value, -time) %>%
  ggplot(aes(x = time, y = value, col = value)) +
  geom_line(size = 5) +
  scale_x_datetime(date_labels = "%m/%d\n%H:%M") +
  facet_grid(key ~ ., scales = "free_y") +
  labs(x = "", y = "") +
  theme_minimal() +
  theme(
    axis.text.x = element_blank(),
    axis.ticks.x = element_blank(),
    legend.position = 'none'
    )  -> p1


tbl(con, "remo") %>%
  select(time, temperature, humidity, illumination) %>%
  rename(
      `気温(℃)` = temperature,
      `相対湿度(%)` = humidity,
      `明るさ` = illumination
  ) %>%
  collect() %>%
  mutate(time = as_datetime(time)) %>%
  gather(key, value, -time) %>%
  ggplot(aes(x = time, y = value, col = key)) +
  geom_line() +
  scale_x_datetime(date_labels = "%m/%d\n%H:%M") +
  facet_grid(key ~ ., scales = "free_y") +
  labs(x = "", y = "") +
  theme_minimal() +
  theme(
    legend.position = "none"
  ) -> p2

p <- p1 / p2 + plot_layout(heights = c(2, 3))

ggsave("/home/rito/image/plot.png", p, width = 5, height = 5)
