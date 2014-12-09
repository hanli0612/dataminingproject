library(caret)
library(tree)
library(gbm)
library(e1071)
library(kernlab)
library(plyr)
# linear regression y = Food.Truck.Num, x = 4 
ft <- read.csv("C:/Users/Jasper7/Desktop/clusters_final_2.csv")
FTR <- ft[, -c(1, 3:21)]
dat <- subset(FTR, FTR[, 1] != 0)
dat_1 <- subset(FTR, FTR[, 1] == 0)

# dat <- dat[, c(3:6, 24)]
## Split dataset into training and test set where training data is 80% of the total data
smp_size <- floor(0.8 * nrow(dat))
set.seed(3)
train_ind <- sample(seq_len(nrow(dat)), size = smp_size)
train <- dat[train_ind, ]
test <- dat[-train_ind, ]
train_y <- train$Review.Per.Food.Truck
test_y <- test$Review.Per.Food.Truck
#train <- dat
#test_dat <- read.csv("C:/Users/Jasper7/Desktop/demo_data.csv")
#test <- test_dat[, -c(1:12)]


# Linear Regression Model
fit.lm <- lm(Review.Per.Food.Truck ~., data = train)
#- X8pm.Food.Truck.Checkin - X0am.Food.Checkin - X4am.Food.Checkin
#- X8am.Food.Checkin - X12pm.Food.Checkin - X4pm.Food.Checkin - X8pm.Food.Checkin
#- X0am.No.Food.Checkin - X4am.No.Food.Checkin - X8am.No.Food.Checkin
#- X12pm.No.Food.Checkin - X4pm.No.Food.Checkin - X8pm.No.Food.Checkin
#- X12pm.No.Food.Checkin, data = train)

# par(mfrow=c(2,2))
# plot(fit.lm)

# Regression Tree Model
set.seed(3)
fit.rt <- tree(Review.Per.Food.Truck ~ ., data = train)
summary(fit.rt)
# plot tree
plot(fit.rt)
text(fit.rt, pretty = 0, cex=.7)

# fit a boosting model with 1000 trees and 0.01 for shrinkage value
set.seed(3)
fit.bst <- gbm(Review.Per.Food.Truck ~ ., data = train, n.trees = 1000, shrinkage = 0.01, distribution = "gaussian")
summary(fit.bst)

## svm
set.seed(3)
fit.svm <- svm(Review.Per.Food.Truck ~ ., data = train, cost = 100, gamma = 1)
summary(fit.svm)
plot(fit.svm)

###### SVR #######
## do a quick grid search on the C
Csearch <- ldply(c(0.01, 0.1, 1, 10), function(x) {
  fit.svr <- ksvm(Review.Per.Food.Truck ~ ., C = x, data = train, type = "eps-svr",kernel ="vanilladot",
             kpar = "automatic", cross = 5, method = "anova")
  return(data.frame(C = x, err = slot(fit.svr, "cross")))
})
fit.svr <- ksvm(Review.Per.Food.Truck ~ .,data = train, type = "eps-svr",kernel ="vanilladot",
            kpar = "automatic", C = 1, method="anova")
pred.svr <- predict(fit.svr, test)
pred.svr.train <- predict(fit.svr, train)



pred.lm <- predict(fit.lm, test)
pred.lm.train <- predict(fit.lm, train)
pred.rt <- predict(fit.rt, test)
pred.rt.train <- predict(fit.rt, train)
pred.bst <- predict(fit.bst, test, n.trees = 1000, type = "response")
pred.bst.train <- predict(fit.bst, train, n.trees = 1000, type = "response")
pred.svm <- predict(fit.svm, test)
pred.svm.train <- predict(fit.svm, train)


lm <- (pred.lm - min(pred.lm))/(max(pred.lm) - min(pred.lm))
rt <- (pred.rt - min(pred.rt))/(max(pred.rt) - min(pred.rt))
bst <- (pred.bst - min(pred.bst))/(max(pred.bst) - min(pred.bst))
svm <- (pred.svm - min(pred.svm))/(max(pred.svm) - min(pred.svm))
data.frame(lm, rt, bst, svm)
df <- data.frame(lm, rt, bst, svm)


train.err.lm <- sqrt(mean((pred.lm.train - train_y)^2))/(max(train_y) - min(train_y))
test.err.lm <- sqrt(mean((pred.lm - test_y)^2))/(sd(test_y))
train.err.rt <- sqrt(mean((pred.rt.train - train_y)^2))/(max(train_y) - min(train_y))
test.err.rt <- sqrt(mean((pred.rt - test_y)^2))/(sd(test_y))
train.err.bst <- sqrt(mean((pred.bst.train - train_y)^2))/(max(train_y) - min(train_y))
test.err.bst <- sqrt(mean((pred.bst - test_y)^2))/(sd(test_y))
train.err.svm <- sqrt(mean((pred.svm.train - train_y)^2))/(max(train_y) - min(train_y))
test.err.svm <- sqrt(mean((pred.svm - test_y)^2))/(sd(test_y))
train.err.svr <- sqrt(mean((pred.svr.train - train_y)^2))/(max(train_y) - min(train_y))
test.err.svr <- sqrt(mean((pred.svr - test_y)^2))/(sd(test_y))

cat("The RMSE for linear model is: ", train.err.lm, test.err.lm)
cat("The RMSE for regression tree model is: ", train.err.rt, test.err.rt)
cat("The RMSE for boosting model is: ", train.err.bst, test.err.bst)
cat("The RMSE for svm model is: ", train.err.svm, test.err.svm)
cat("The RMSE for svr model is: ", train.err.svr, test.err.svr)

# err <- rbind(test.err.lm, test.err.rt, test.err.bst, test.err.svm)
# mat <- matrix(c(test.err.lm, test.err.rt, test.err.bst, test.err.svm))
# barplot(mat)
