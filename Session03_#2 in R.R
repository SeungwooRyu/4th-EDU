library(dplyr)
library(magrittr)
library(ggplot2)

data <- read.csv('C:/Users/승우/Desktop/province data.csv', header=T)

data %<>% group_by(id) %>%
  summarise(mean_gdp=mean(gdp, na.rm=T), mean_unem=mean(unemployment, na.rm=T)
            , mean_sex=mean(sexratio, na.rm=T))

category <- ifelse(data$mean_sex>=110, '2', '1')

data2 <- cbind(data, category)

ggplot(data2, aes(x=mean_gdp, y=mean_unem, color=category, shape=category))+
  geom_point()+
  scale_shape_manual(values=c(17,4))+
  xlab('GDP')+
  ylab('UNEMPLOYMENT')+
  theme(legend.title = element_blank())+
  theme(legend.position = 'none')+
  scale_x_continuous(breaks=seq(4.0, 6.0, 0.25))
