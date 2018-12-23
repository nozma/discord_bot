library(RSQLite)
library(dplyr)
library(dbplyr)
library(lubridate)
library(ggplot2)
library(tidyr)


con <- dbConnect(RSQLite::SQLite(), "/home/rito/db/remoData.db")

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
  ggplot(aes(x = time, y = value)) +
  geom_line() +
  facet_grid(key ~ ., scales = "free_y") +
  labs(x = "", y = "") +
  theme_bw() -> p

ggsave("/home/rito/image/plot.png", p)